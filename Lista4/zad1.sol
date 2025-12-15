// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract UserStorage {
    // mapping szybszy niz tablica
    mapping(address => bool) private users;

    // dodaje uzytkownika
    function addUser(address user) external {
        users[user] = true;
    }

    // sprawdza czy uzytkownik istnieje
    function userExists(address user) external view returns (bool) {
        return users[user];
    }
}
