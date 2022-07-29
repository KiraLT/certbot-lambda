#!/usr/bin/env python3

import shutil

from app.settings import load_settings
from app.services.certbot import obtain_certbot_certs
from app.services.aws import list_secret_names, upload_certs_as_secrets


def handler(_event, _context):
    settings = load_settings()

    try:
        shutil.rmtree(str(settings.CERTBOT_DIR), ignore_errors=True)

        # Load secret names early to check if aws client is configured correctly
        secret_names = list_secret_names()

        certs = obtain_certbot_certs(
            emails=settings.CERTBOT_EMAILS,
            domains=settings.CERTBOT_DOMAINS,
            dns_plugin=settings.CERTBOT_DNS_PLUGIN,
            certbot_dir=settings.CERTBOT_DIR,
            certbot_server=settings.CERTBOT_SERVER,
            preferred_chain=settings.CERTBOT_PREFERRED_CHAIN,
            extra_args=settings.CERTBOT_EXTRA_ARGS,
            credentials=settings.CERTBOT_CREDENTIALS,
            propagation_seconds=settings.CERTBOT_PROPAGATION_SECONDS,
        )

        upload_certs_as_secrets(
            certs,
            name=settings.AWS_SECRET_NAME,
            secret_names=secret_names,
            description=settings.AWS_SECRET_DESCRIPTION,
        )
    finally:
        shutil.rmtree(str(settings.CERTBOT_DIR), ignore_errors=True)

    return "Certificates obtained and uploaded successfully."


if __name__ == "__main__":
    handler(None, None)
