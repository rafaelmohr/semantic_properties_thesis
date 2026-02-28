// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

/**
 * @title Storage
 * @dev Store & retrieve value in a variable
 */
contract Storage {

    // SEM-ANALYZER #Getter #SimpleGetter #ReturnSize32
    uint256 public number;

    /**
     * @dev Store value in variable
     * @param num value to store
     */
    // SEM-ANALYZER #Setter #SimpleSetter
    function store(uint256 num) public {
        number = num;
    }
}
