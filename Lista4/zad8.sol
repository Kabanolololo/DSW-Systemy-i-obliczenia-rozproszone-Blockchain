// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract Events {
    uint public value;

    // event jest emitowany tylko przy zmianie wartosci
    event ValueChanged(uint newValue);

    function set(uint v) external {
        if (value != v) {
            value = v;
            emit ValueChanged(v);
        }
    }
}
