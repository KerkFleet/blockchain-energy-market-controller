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
    function optimize_bids() public {

        // Set Reduction Resquest
        uint reductionExample = 4;
        // ------- Create Test Data --------

        // Sort the bids from Cheapest to most expensive
        // bidsExample = bidInsertionSort(bidsExample);
        bidInsertionSort();

        // Array Address of last winning bid
        uint lastWinningBid = 0;
        // Add up bids unitl you find a winner
        lastWinningBid = findWinningBids(reductionExample);

        // Disperse Rewards
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

    function findWinningBids(uint reduction)internal returns(uint){
    uint totalPower = 0;
    uint lastWinningBid;
    for (uint i = 0;totalPower < reduction || i < bids.length;i++){
        totalPower += bids[i].power;
        lastWinningBid = i;
    }
    return lastWinningBid;
    }
    // ---------- Optimize Functions -----------


    function submit_bids(uint[] memory power, uint[] memory price) public {
        delete bids[msg.sender];
        require(registered[msg.sender] == true);
        require(power.length == price.length, "Each bid must have a reduction amount and an associated price");
        for(uint i = 0; i < power.length; i++){
            bids[msg.sender].push(Bid(power[i], price[i], msg.sender)); 
        }

    }

    function disperse_rewards() public {
        for(uint i = 0; i < winners.length; i++){
            address payable winner = payable(winners[i]);
            winner.transfer(reward_amount);
        }
        address payable _owner = payable(owner());
        _owner.transfer(address(this).balance);

    }

    function register() public {
        require(registered[msg.sender] == false);
        registrants.push(msg.sender);
        registered[msg.sender] = true;
    }

}
