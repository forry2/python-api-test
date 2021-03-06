#!/usr/bin/env python3

from logging import basicConfig
from logging.config import dictConfig
from os.path import isfile

import connexion
import yaml


def configure_logger(log_config="logging.yaml"):
    """Configure the logging subsystem."""
    if not isfile(log_config):
        return basicConfig()

    with open(log_config) as fh:
        log_config = yaml.safe_load(fh)
        return dictConfig(log_config)


def main():
    configure_logger()

    app = connexion.App(__name__, specification_dir="./openapi/")
    app.add_api("store.yaml", arguments={"title": "Ora esatta."})
    app.run(port=8443, ssl_context="adhoc", debug=True)


if __name__ == "__main__":
    main()
