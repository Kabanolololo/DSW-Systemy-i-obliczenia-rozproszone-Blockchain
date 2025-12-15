// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract ConstructorOptimized {
    // dane inicjalizowane bez petli w konstruktorze
    uint[] public values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
}
