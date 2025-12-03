// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimplePayment {
    address public owner;  // adres wlasciciela

    constructor() {
        owner = msg.sender;  // ustawienie wlasciciela
    }

    // przyjmowanie eth
    receive() external payable {}

    // wplacanie eth
    function deposit() external payable {}

    // wypłata dla wlasciciela
    function withdraw(uint amount) public {
        require(msg.sender == owner, "Tylko wlasciciel moze wyplacac");
        require(address(this).balance >= amount, "Za malo srodkow");

        payable(owner).transfer(amount);
    }

    // sprawdzenie balansu
    function getBalance() public view returns (uint) {
        return address(this).balance;
    }
}
