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

## Bug Fixes

* Remove `frequenz-api-common` files now that dependency conflict is solved
* Fix DeliveryArea from and to pb methods
* Use HasFields method on protobuf messages
