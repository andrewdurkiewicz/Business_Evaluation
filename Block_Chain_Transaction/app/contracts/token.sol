pragma solidity ^0.4.8;

contract Deed {

  bytes32 public prop_addr; // the address of the property
  bool public forSale;  // if true, that property is owned
  address public owner; // person who owns property
  uint public value;   // value of the property (in wei)

  function Deed(bytes32 _prop_addr) {
    prop_addr = _prop_addr;
    forSale = false;
    owner = msg.sender;
    value = 0;
  }
  function declareSale(uint _value) returns(bytes32 message) {
    value = _value;
    forSale = true;
    return "Property Listed :)";
  }
  function newOwner(address new_owner) returns (bool success) {
    if(owner == msg.sender) {
      owner = new_owner;
      return true;
    }
    throw;
  }
  function getValue() constant returns (uint _value) {
    return value;
  }
  function getOwner() constant returns (address _owner) {
    return owner;
  }
}
