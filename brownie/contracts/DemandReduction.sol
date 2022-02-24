//SPDX-License-Identifier: Unlicense
pragma solidity ^0.8.0;

//This is marked as an error for me but i don't think it's actually an error. IDK.
import "OpenZeppelin/openzeppelin-contracts@4.4.1/contracts/access/Ownable.sol";


contract DemandReduction is Ownable{
    struct Bid {
        uint power;
        uint price;
        address consumer;
    }

    // To keep track of who has registered
    mapping(address => bool) registered;
    address [] registrants;

    // Mapping to map consumer address to array of Bid structs
    Bid[] bids;
    uint reward_amount;
    uint power_reduction;

    // selected winners
    address [] winners;

    event notify_consumer();

    function request_reduction(uint reduction_amount) public payable onlyOwner{
        require(msg.value >= 0.01 ether, "Must pay at least 0.01 ether");
        power_reduction = reduction_amount;
        emit notify_consumer();
    }

    // ---------- Optimize Functions -----------
    // Optimize Bids is called by the utility in one of their scripts
    function select_winners() public {
        bidInsertionSort();
        uint lastWinningBid = 0;
        lastWinningBid = optimize_bids(power_reduction);
        disperse_rewards(lastWinningBid);
        delete bids;
    }


    function bidInsertionSort() public {
        for (uint i = 0;i < bids.length;i++){
            uint temp = bids[i].price;
            uint j;
            for (j = i -1; j >= 0 && temp < bids[j].price; j--)
            bids[j+1] = bids[j];
            bids[j + 1].price = temp;
        }
    }

    function optimize_bids(uint reduction)internal returns(uint){
        uint totalPower = 0;
        uint lastWinningBid;
        for (uint i = 0; totalPower < reduction && i < bids.length; i++){
            totalPower += bids[i].power;
            reward_amount = bids[i].price;
            lastWinningBid = i;
        }
        return lastWinningBid;
    }
    // ---------- Optimize Functions -----------


    function submit_bids(uint[] memory power, uint[] memory price) public {
        require(registered[msg.sender] == true);
        require(power.length == price.length, "Each bid must have a reduction amount and an associated price");
        for(uint i = 0; i < power.length; i++){
            bids.push(Bid(power[i], price[i], msg.sender)); 
        }

    }

    function disperse_rewards(uint last_bid) public {
        for(uint i = 0; i < last_bid; last_bid++){
            address payable winner = payable(bids[i].consumer);
            winner.transfer(reward_amount * 1 wei);
        }
        address payable _owner = payable(owner());
        _owner.transfer(address(this).balance);
    }

    function register() public {
        require(registered[msg.sender] == false, "Already registered");
        registrants.push(msg.sender);
        registered[msg.sender] = true;
    }

    function check_registered(address consumer) public view returns(bool){
        return registered[consumer];
    }

}
