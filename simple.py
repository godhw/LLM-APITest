from time import sleep, time
from typing import Dict

import requests
from loguru import logger


def simple_test(request: Dict, interval: int, attempts: int, generate_uri: str, result_uri: str):
    """Very simple API test.
    Just request and get response.

    Arguments:
        request (Dict): Request form for the post.
        interval (int): Polling interval for get the result.
        attempts (int): Number of the get result request.
    """
    logger.info("Start Simple Test")
    logger.info(f"request content: {request}")
    logger.info(f"get request interval(sec): {interval}")
    logger.info(f"max attempts: {attempts}")

    task = requests.post(generate_uri, json=request)
    task_id = task.json()["task_id"]
    result_uri = result_uri + "/" + task_id
    start = time()
    logger.info("send post method")
    result = None

    i = 0
    while i < attempts:
        i += 1
        result_response = requests.get(result_uri)
        if result_response.status_code == 200:
            status = result_response.json()["status"]
            if status == "pending":
                logger.info(f"Not assigned. Ex Time(s) after post method: {time() - start}")
            elif status == "assigned":
                logger.info(f"Not ready for the result. Ex Time(s) after post method: {time() - start}")
            else:
                result = result_response.json()["result"]
                break
        else:
            logger.error("http error code :", result_response.status_code)

        sleep(interval)
    if i == attempts:
        logger.error(f"Out of attempts. Ex Time(s) after post method: {time() - start}")
    else:
        logger.info(f"Get result:{result} Ex time(s): after post method: {time() - start}")
    logger.info("End Simple Test")
