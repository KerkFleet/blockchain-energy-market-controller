import time
import json
from brownie import Contract, web3, accounts
from . import utils
import os
import pathlib

utils.load_dotenv()
account = utils.load_account("CONSUMER_ACCOUNT")


def submit_bids(contract, energy, value, account, user_input):
    #read bids from file
    contract.submit_bids(energy, value, {"from": account})
    pass


def main():
    user_input = False
    energy = []
    value = []


    print("Setting up contract connection. . .")
    contract_address = os.environ.get('CONTRACT_ADDRESS')
    contract_abi = utils.load_contract_abi("DemandReduction")
    web3_contract = web3.eth.contract(address=contract_address, abi=contract_abi) # example of getting contract using web3
    
    # Connect Externally
    # brownie_contract = Contract.from_explorer(contract_address)

    # Connect Locally
    brownie_contract = Contract(contract_address) # example of using a brownie contract instance
    
    print("Connection created.")

    while True:
        # input("Press enter when 'bids.json' file is ready to submit. . .")

        # create filter for event to listen to
        submit_event_filter = web3_contract.events.notify_consumer.createFilter(fromBlock='latest')
        rewards_event_filter = web3_contract.events.notify_rewards.createFilter(fromBlock='latest')

        print("Now waiting for a energy reduction request. . .")
        utils.listen_for_event(submit_event_filter, web3_contract)
        print("Energy reduction requested. Submitting bids!")

        # load bids
        f = open(pathlib.Path(__file__).parent.parent / 'database' / 'bids.json', "r")
        data = json.load(f)
        f.close()
        temp_energy = data['energy']
        temp_value = data['price']
        energy = [i * 10**3 for i in temp_energy]
        value = [i * 10**18 for i in temp_value]

        submit_bids(brownie_contract, energy, value, account, user_input)
        print("Waiting selection. . .")

        # awaiting contract optimizations and selections
        tx = utils.listen_for_event(rewards_event_filter, web3_contract)

        # check if we have been selected or not
        selected = False
        print("Retrieving winning bids...")
        winners = brownie_contract.getWinners.call({"from": account})
        print("Winning bids: ")
        num_selected = 0
        f = open(pathlib.Path(__file__).parent.parent / 'database' / 'results.json', "w")
        data = {"results": []}
        for i in winners:
            if(str(i[2]) == account):
                print("Bid selected: ", i) # each selected bid would contain the device id or something to push your control signal to
                data["results"].append({ "Energy": str(i[0] / 10**3), "Price": str(i[1] / 10**18)})
                selected = True
                num_selected = num_selected + 1
        if not selected:
            print("No bids were selected.")
            data["results"].append({"Bid": "No bids selected"})
        else:
            reward_amount = brownie_contract.getRewardAmount.call({"from": account})
            print("You have been rewarded ", num_selected * (reward_amount / 10**18), " ETH.")
        data["time"] = time.ctime()
        results = json.dumps(data)
        f.write(results)
        f.close()
