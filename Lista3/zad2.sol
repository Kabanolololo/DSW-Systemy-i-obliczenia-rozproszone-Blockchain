// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Counter {
    int public count;            // przechowywana wartość licznika

    constructor() {
        count = 0;               // ustawia licznik na 0 przy starcie
    }

    function increment() public {
        count += 1;              // zwiększa licznik o 1
    }

    function decrement() public {
        require(count > 0, "Nie mozna zejsc ponizej 0 !!!");  // nie pozwala dostac sie poniżej 0
        count -= 1;                                          // zmniejsza licznik o 1
    }

    function reset() public {
        count = 0;               // ustawia licznik z powrotem na 0
    }
}
