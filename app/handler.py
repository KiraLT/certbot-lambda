#!/usr/bin/env python3

import shutil

from app.settings import settings
from app.services.certbot import obtain_certbot_certs
from app.services.aws import list_secret_names, upload_certs_as_secrets


def handler(_event, _context):
    try:
        shutil.rmtree(str(settings.CERTBOT_DIR), ignore_errors=True)
        # Load secret names yearly to check if aws client is configured correctly
        secret_names = list_secret_names()

        # Obtain certs
        certs = obtain_certbot_certs(
            emails=settings.CERTBOT_EMAILS,
            domains=settings.CERTBOT_DOMAINS,
            dns_plugin=settings.CERTBOT_DNS_PLUGIN,
            certbot_dir=settings.CERTBOT_DIR,
            certbot_server=settings.CERTBOT_SERVER,
        )

        upload_certs_as_secrets(
            certs, name=settings.AWS_SECRET_NAME, available_secrets=secret_names
        )
    finally:
        shutil.rmtree(str(settings.CERTBOT_DIR), ignore_errors=True)

    return "Certificates obtained and uploaded successfully."


if __name__ == "__main__":
    handler(None, None)
