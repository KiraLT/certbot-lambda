#!/usr/bin/env python3

import shutil
from certbot._internal.plugins import disco as plugins_disco
from os import environ

from app.settings import load_settings
from app.services.certbot import obtain_certbot_certs
from app.services.aws import upload_certs_as_secrets


def handler(_event, _context):
    if environ.get("TESTMODE") == "true":
        plugins = list(plugins_disco.PluginsRegistry.find_all())
        dns_plugins = [v for v in plugins if v.startswith("dns-")]

        if len(dns_plugins) != 14:
            raise Exception("Failed to discover all certbot DNS plugins")

        return
    else:
        settings = load_settings()

        try:
            shutil.rmtree(str(settings.CERTBOT_DIR), ignore_errors=True)

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
                description=settings.AWS_SECRET_DESCRIPTION,
            )
        finally:
            shutil.rmtree(str(settings.CERTBOT_DIR), ignore_errors=True)

    return "Certificates obtained and uploaded successfully."


if __name__ == "__main__":
    handler(None, None)
