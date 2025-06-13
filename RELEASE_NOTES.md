# Frequenz Electricity Trading API Release Notes

## Upgrading

- The minimum allowed version of `protobuf` and `grpcio` has been updated to 6.31.1 and 1.72.1 respectively, you might also need to bump your dependencies accordingly.

## New Features

- Made `OrderType` optional in `PublicOrderBookRecord` to handle cases where the order type is unknown.
