// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract Modifiers {
    uint private data = 42;

    // brak modyfikatora obniaza koszt wywolania
    function getData() external view returns (uint) {
        return data;
    }
}
