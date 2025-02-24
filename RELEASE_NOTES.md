# Frequenz Electricity Trading API Release Notes

## Summary

<!-- Here goes a general summary of what this release is about -->

## Upgrading

* Remove the `ListPublicTrades` RPC endpoint.
* Refactor `ReceivePublicTradesStream` to handle real-time and historical trades.
    * Use `start_time` to retrieve past trades from a specific timestamp. 
      If omitted the stream starts from the time the connection was established.
    * Use `end_time` to stop the stream at a defined point.
      If omitted it will keep streaming new trades indefinitely.


## New Features

<!-- Here goes the main new features and examples or instructions on how to use them -->

## Bug Fixes

<!-- Here goes notable bug fixes that are worth a special mention or explanation -->
