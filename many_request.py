from time import sleep, time
from typing import Dict

import requests
from loguru import logger


def get_request(result_uri: str) -> bool:
    def get_request_inner(task_id: str):
        sleep(0.05)
        current_result_uri = result_uri + "/" + task_id
        result_response = requests.get(current_result_uri)
        if result_response.status_code == 200:
            status = result_response.json()["status"]
            if status == "completed":
                return False
            else:
                return True
        else:
            logger.error(f"http error code :{result_response.status_code}")
            logger.error(f"Current task_id: {task_id}")
            return False


def many_request_test(request: Dict, number_of_request: int, max_attempts: int, generate_uri: str, result_uri: str):
    """Many Request API test.
    Many requests to server in very short time
    Default attempt interval is 3 seconds
    Default each get request interval is 50ms

    Arguments:
        request (Dict): Request form for the post.
        number_of_request (int): Number of requests in very short time.
        attempts (int): Number of the get result request.
        generate_uri (str): Request uri.
        result_uri (str): Result request uri. use in this code like: result_uri/{task_id}
    """
    logger.info("Start Many Requests Test")
    logger.info(f"request content: {request}")
    logger.info(f"Num of Get Request: {number_of_request}")
    logger.info(f"max attempts: {max_attempts}")
    task_id_list = []
    request_count = 0
    logger.info("Request start")
    request_start = time()
    while request_count < number_of_request:
        request_count += 1
        task = requests.post(generate_uri, json=request)
        task_id_list.append(task.json()["task_id"])
    request_end = time()
    logger.info(f"Request end. execution Time(s): {request_start - request_end}")

    logger.info("Request get result start")
    attempt_count = 0
    get_request_curry = get_request(result_uri)
    while attempt_count < max_attempts:
        if len(task_id_list) == 0:
            break
        attempt_count += 1
        logger.info(f"attempts count : {attempt_count}")
        logger.info(f"left task : {len(task_id_list)}")
        task_id_list = filter(get_request_curry, task_id_list)
        sleep(3)
    if len(task_id_list) == 0:
        logger.info(f"Test Finished. Execution Time of get method(sec): {time() - request_end}")
    else:
        logger.error(f"Out of attempts. Execution Time of get method(s): {time() - request_end}")
        logger.error(f"Left task : {len(task_id_list)}")
    logger.info("End Many Request Test")
