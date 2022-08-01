from loguru import logger

from config import many_request_test_settings, simple_test_settings, uri_settings
from many_request import many_request_test
from simple import simple_test


if __name__ == "__main__":
    logger.debug("Start Test Code")
    base_uri = uri_settings.base_uri
    generate_uri = base_uri + uri_settings.generate_uri
    result_uri = base_uri + uri_settings.result_uri

    simple_test(
        simple_test_settings.data,
        simple_test_settings.interval,
        simple_test_settings.max_attempts,
        generate_uri,
        result_uri,
    )
    many_request_test(
        many_request_test_settings.data,
        many_request_test_settings.num_of_request,
        many_request_test_settings.max_attempts,
        generate_uri,
        result_uri,
    )
    logger.debug("End of Test")
