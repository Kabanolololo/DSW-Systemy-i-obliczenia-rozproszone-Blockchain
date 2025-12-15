// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract ShortText {
    // bytes zajmuja mniej miejsca niz string
    bytes2 public constant OK = "OK";
    // constant nie zapisuje danych do storage
    bytes3 public constant ERR = "ERR";
}
