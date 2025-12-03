// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract NumberStorage {
    uint public storedNumber;     // zmienna przechowująca liczbę

    function setNumber(uint _number) public {
        storedNumber = _number;   // zapisuje liczbę do storedNumber
    }

    function getNumber() public view returns (uint) {
        return storedNumber;      // zwraca aktualnie zapisaną liczbę
    }
}
