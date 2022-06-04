// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

contract FenBoard {

    // private final address address_white
    address private _address_white; //immutable?

    // private final address address_black
    address private _address_black; //immutable?

    // private String boardState
    string private _boardState;

    // public constructor
    constructor(address address_white, address address_black) public {
        _address_white = address_white;
        _address_black = address_black;

        _boardState = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1";
    }

    // public contract address getter
    // function getContractAddress() public view returns (address) {
    //     return address(this);
    // }

    // public getter for white address
    function getWhiteAddress() public view returns (address) {
        return _address_white;
    }

    // public getter for black address
    function getBlackAddress() public view returns (address) {
        return _address_black;
    }

    // public getter for board state
    function getBoardState() public view returns (string memory) {
        return _boardState;
    }

    // public setter for board state
    function setBoardState(string memory boardState) public {
        _boardState = boardState;
    }

}