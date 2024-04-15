# Frequenz Electricity Trading API Release Notes

## Summary

<!-- Here goes a general summary of what this release is about -->

## Upgrading

<!-- Here goes notes on how to upgrade from previous versions, including deprecations and what they should be replaced with -->

## New Features

* Make a distinction between Order and Trade in the protobuf definitions
* Introduction of new endpoints to retrieve gridpool trades
* Addition of new definitions and support for trade state filters and streaming
* Refactor DeliveryPeriod to take in a timedelta duration attribute instead of the DeliveryDuration Enum type
* Public trades renamed from public_trade_lists to public trades and all _lists suffixes removed
* Remove ORDER_EXECUTION_OPTION_NONE from OrderExecutionOption
* Add unit tests for the client types and functions
* Add error handling in the client for the gRPC errors that could be raised by the service


## Bug Fixes

* Remove `frequenz-api-common` files now that dependency conflict is solved
* Fix DeliveryArea from and to pb methods
* Use HasFields method on protobuf messages
* Make the `DeliveryPeriod` and all `Filter` types hashable
* Force all timestamps to be timezone aware and UTC
* Refactor some protofub timestamps that were falsly returning None values in the client
