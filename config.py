from typing import Dict

from dotenv import load_dotenv
from pydantic import BaseSettings


load_dotenv(".env")


class UriSettings(BaseSettings):
    base_uri: str
    generate_uri: str
    result_uri: str


class SimpleTestSettings(BaseSettings):
    data: Dict = {"prompt": "My name is"}
    interval: int = 2
    max_attempts: int = 5


class ManyRequestTestSettings(BaseSettings):
    data: Dict = {"prompt": "Hi. Let's start to"}
    num_of_request: int = 100
    max_attempts: int = 5


uri_settings = UriSettings()
simple_test_settings = SimpleTestSettings()
many_request_test_settings = ManyRequestTestSettings()
