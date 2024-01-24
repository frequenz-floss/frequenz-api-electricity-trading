# Frequenz Electricity Trading API Release Notes

## Summary

This API interface's client requires the SDK, which depends on
frequenz-api-common in the version range of 0.3.0 to < 0.4.0. However,
electricity_trading.proto needs some proto files from frequenz-api-common,
which are only available from version 0.5.0. This discrepancy creates
a dependency conflict. To resolve this, the current PR incorporates
the required protos directly from the frequenz-api-common repository and
stores them locally. This approach eliminates the dependency on the common
repository for the time being, until the SDK is updated to a newer version
of frequenz-api-common.

A couple of additions were also made to the `__init__` and  `_types.py` files.


## Upgrading

<!-- Here goes notes on how to upgrade from previous versions, including deprecations and what they should be replaced with -->

## New Features

* Addition of missing types to the `__init__` file
* Addition of missing `to_pb()` methods in the `_types.py` file

## Bug Fixes

* Remove dependency conflict on `frequenz-api-common` by adding it locally
* Add a py.typed file
