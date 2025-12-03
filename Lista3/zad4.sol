// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ToDoList {
    struct Task {
        string description;  // tekst zadania
        bool completed;      // czy zrobione
    }

    Task[] public tasks;     // lista zadan

    // dodaj zadanie
    function addTask(string memory _description) public {
        tasks.push(Task(_description, false));
    }

    // oznacz jako zrobione
    function completeTask(uint index) public {
        require(index < tasks.length, "Zly numer zadania");
        tasks[index].completed = true;
    }

    // pobierz wszystkie zadania
    function getTasks() public view returns (Task[] memory) {
        return tasks;
    }
}
