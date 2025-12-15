// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract FunctionTypes {
    uint private value = 10;

    // external jest tansze niz public
    function getValue() external view returns (uint) {
        return value;
    }
}
