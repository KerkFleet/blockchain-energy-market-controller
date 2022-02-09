//SPDX-License-Identifier: Unlicense
pragma solidity ^0.8.0;

import "OpenZeppelin/openzeppelin-contracts@4.4.1/contracts/access/Ownable.sol";


contract DemandReduction is Ownable{
    struct Bid {
        uint power;
        uint price;
    }

    // To keep track of who has registered
    mapping(address => bool) registered;
    address [] registrants;

    // Mapping to map consumer address to array of Bid structs
    mapping(address => Bid[]) bids;
    uint reward_amount;
    uint power_reduction;

    event notify_consumer();

    function request_reduction(uint reduction_amount) public onlyOwner {
        power_reduction = reduction_amount;
        emit notify_consumer();
    }

    function optimze_bids() private {

    }

    function submit_bids(uint[] memory power, uint[] memory price) public {
        require(registered[msg.sender] == true);
        require(power.length == price.length, "Each bid must have a reduction amount and an associated price");
        Bid memory bid;
        for(uint i = 0; i < power.length; i++){
            bid = Bid(power[i], price[i]);
            bids[msg.sender].push(bid);
        }

    }

    function disperse_rewards() private {

    }

    function register() public {
        require(registered[msg.sender] == false);
        registrants.push(msg.sender);
        registered[msg.sender] = true;
    }

}
