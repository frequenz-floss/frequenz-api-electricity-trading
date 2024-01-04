# License: MIT
# Copyright © 2023 Frequenz Energy-as-a-Service GmbH

"""Configuration file for nox."""

from frequenz.repo.config import nox
from frequenz.repo.config.nox import default

config = default.api_config.copy()
config.source_paths = ["py/frequenz/client/electricity_trading"]
nox.configure(config)
