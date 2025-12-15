// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract StoragePacking {
    // dwa uint128 mieszcza sie w jednym slocie storage
    uint128 a;
    uint128 b;

    // uint256 zajmuje osobny slot
    uint256 c;
}
