from brownie import Contract, web3, accounts
from dotenv import load_dotenv, find_dotenv
from . import utils
import os

accounts.load('test-rinkeby-2')
env = find_dotenv()
load_dotenv(env)



def main():
    energy = []
    value = []
    count = 0
    while True:
        count = count + 1
        print(f"Block {count}:")
        e = int(input("Energy amount: "))
        v = int(float(input("Energy value: ")) * 10**18)

        energy.append(e)
        value.append(v)
        cont = input("Add another?(y/n): ")
        if cont == 'n' or cont == 'N':
            break

    # INSERTION SORT decending order
    for step in range(1, len(value)):
        key = value[step]
        energyKey = energy[step]
        j = step - 1
        
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key > value[j]:
            value[j + 1] = value[j]
            energy[j + 1] = energy[j]
            j = j - 1
        
        # Place key at after the element just smaller than it.
        value[j + 1] = key
        energy[j + 1] = energyKey
    # INSERTION SORT decending order


    print("Your bids input: ")
    print("Energy: ", energy)
<<<<<<< HEAD
    # print("Values: ", value)
    print("Values: [", end =" ")
    for i in value:
        print(i/10**18, end =" ")
    print("]")
=======
    print("Values: ", value)
    # print("Values: [", end =" ")
    # for i in value:
    #     print(i/10**18, end =" ")
    # print("]")
>>>>>>> 263479ea253401352c98699b0712c28604cb361b

    print("Setting up contract connection. . .")

    # load contract data
    contract_address = os.environ.get('CONTRACT_ADDRESS')
    contract_abi = utils.load_contract_abi("DemandReduction")


    # load contract
    contract = web3.eth.contract(address=contract_address, abi=contract_abi) # example of getting contract using web3
<<<<<<< HEAD
    brownie_contract = Contract.from_explorer(contract_address)
=======
    
    # Connect Externally
    # brownie_contract = Contract.from_explorer(contract_address)

    # Connect Locally
    brownie_contract = Contract(contract_address)

>>>>>>> 263479ea253401352c98699b0712c28604cb361b
    print("Connection created.")

    # create filter for event to listen to
    while True:
        submit_event_filter = contract.events.notify_consumer.createFilter(fromBlock='latest')
        rewards_event_filter = contract.events.notify_rewards.createFilter(fromBlock='latest')
        print("Now waiting for a energy reduction request. . .")
        utils.listen_for_event(submit_event_filter)
        print("Energy reduction requested. Submitting bids!")
        brownie_contract.submit_bids(energy, value, {"from": accounts[0]})
        print("Waiting selection. . .")
        utils.listen_for_event(rewards_event_filter)
        selected = False
        print("Retrieving winning bids...")
        winners = brownie_contract.getWinners.call({"from": accounts[0]})
        print("Winning bids: ")
        for i in winners:
            if(str(i) == accounts[0]):
                print("Bid selected: ", i)
                selected = True
        if not selected:
            print("No bids were selected.")
        else:
            reward_amount = brownie_contract.getRewardAmount.call({"from": accounts[0]})
<<<<<<< HEAD
            print("You have been rewarded ", reward_amount/10**18, " ETH.")
=======
            print("You have been rewarded ", reward_amount / 10**18, " ETH.")
>>>>>>> 263479ea253401352c98699b0712c28604cb361b

        #call bid submitting function here



    







    



