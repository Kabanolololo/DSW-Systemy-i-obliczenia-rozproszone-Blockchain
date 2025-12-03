// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleToken {
    string public name = "SimpleToken";   // nazwa tokena
    string public symbol = "STK";         // symbol tokena
    uint8 public decimals = 18;           // miejsca dziesietne

    mapping(address => uint) public balanceOf;  // saldo uzytkownikow

    constructor(uint initialSupply) {
        balanceOf[msg.sender] = initialSupply;  // cale saldo dla twórcy
    }

    // wysylanie tokenow
    function transfer(address to, uint amount) public returns (bool) {
        require(balanceOf[msg.sender] >= amount, "Za malo tokenow");

        balanceOf[msg.sender] -= amount;
        balanceOf[to] += amount;

        return true;
    }
}
