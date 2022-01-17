from pydantic import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    EMAILS: list[str]
    DOMAINS: list[str]
    DNS_PLUGIN: str
    CERTBOT_SERVER: str = 'https://acme-v02.api.letsencrypt.org/directory'
    CERTBOT_DIR: Path = Path('/tmp/certbot')
    AWS_SECRET_NAME = 'certbot-{domain}'

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        env_nested_delimiter = '__'


settings = Settings()
