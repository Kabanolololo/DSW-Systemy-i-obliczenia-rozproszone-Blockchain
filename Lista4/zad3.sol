// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract Counter {
    uint public counter;

    // jeden zapis do storage zamiast kilku
    function increment() external {
        counter += 3;
    }
}
