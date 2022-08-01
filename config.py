from dotenv import load_dotenv
from pydantic import BaseSettings


load_dotenv(".env")


class UriSettings(BaseSettings):
    base_uri: str = "http://"
    generate_uri: str = "generate"
    result_uri: str = "result/"


uri_settings = UriSettings()
