// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract CustomErrors {
    // custom error jest tanszy niz require z napisem
    error InvalidValue();

    // sprawdza czy wartosc jest poprawna
    function check(uint x) external pure {
        if (x == 0) {
            revert InvalidValue();
        }
    }
}
