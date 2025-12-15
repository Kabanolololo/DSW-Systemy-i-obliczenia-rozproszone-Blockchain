// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract ArraySum {
    // calldata jest tansze niz memory
    // length jest zapisany do zmiennej lokalnej
    function sum(uint[] calldata arr) external pure returns (uint) {
        uint s;
        uint len = arr.length;

        for (uint i; i < len; ) {
            s += arr[i];
            // unchecked usuwa sprawdzanie overflow
            unchecked { i++; }
        }

        return s;
    }
}
