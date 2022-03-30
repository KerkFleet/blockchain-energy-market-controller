import json
from brownie import Contract, web3, accounts
from . import utils
import os

utils.load_dotenv()
account = utils.load_account("CONSUMER_ACCOUNT")


def submit_bids(contract, energy, value, account, user_input):
    #read bids from file
    contract.submit_bids(energy, value, {"from": account})
    pass


def main():
    user_input = False
    while True:
        energy = []
        value = []
        count = 0
        if user_input:
            count = count + 1
            print(f"Block {count}:")
            e = int(float(input("Energy amount: ")) * 10**3)
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
            print("Energy(kWh): [", end =" ")
            for i in energy:
                print(i/10**3, end =" ")
            print("]")
            # print("Values: ", value)
            print("Prices(ETH): [", end =" ")
            for i in value:
                print(i/10**18, end =" ")
            print("]")
        else:
            input("Press enter to continue. . .")
            f = open("bids.json")
            data = json.load(f)
            temp_energy = data['energy']
            temp_value = data['value']
            energy = [i * 10**3 for i in temp_energy]
            value = [i * 10**18 for i in temp_value]

        print("Setting up contract connection. . .")

        # load contract data
        contract_address = os.environ.get('CONTRACT_ADDRESS')
        contract_abi = utils.load_contract_abi("DemandReduction")


        # load contract
        web3_contract = web3.eth.contract(address=contract_address, abi=contract_abi) # example of getting contract using web3
        
        # Connect Externally
        # brownie_contract = Contract.from_explorer(contract_address)

        # Connect Locally
        brownie_contract = Contract(contract_address)

        print("Connection created.")

        # create filter for event to listen to
        submit_event_filter = web3_contract.events.notify_consumer.createFilter(fromBlock='latest')
        rewards_event_filter = web3_contract.events.notify_rewards.createFilter(fromBlock='latest')
        print("Now waiting for a energy reduction request. . .")
        utils.listen_for_event(submit_event_filter)
        print("Energy reduction requested. Submitting bids!")
        submit_bids(brownie_contract, energy, value, account, user_input)
        print("Waiting selection. . .")
        tx = utils.listen_for_event(rewards_event_filter)
        selected = False
        print("Retrieving winning bids...")
        winners = brownie_contract.getWinners.call({"from": account})
        print("Winning bids: ")
        num_selected = 0
        for i in winners:
            if(str(i[2]) == account):
                print("Bid selected: ", i)
                selected = True
                num_selected = num_selected + 1
        if not selected:
            print("No bids were selected.")
        else:
            reward_amount = brownie_contract.getRewardAmount.call({"from": account})
            print("You have been rewarded ", num_selected * (reward_amount / 10**18), " ETH.")

        #call bid submitting function here



    







    



