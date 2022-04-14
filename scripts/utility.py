import time
import json
from . import utils
from brownie import Contract, accounts, web3
import os


def main():
    utils.load_dotenv()
    account = utils.load_account("UTILITY_ACCOUNT")
    contract_address = os.environ.get("CONTRACT_ADDRESS")
    contract_abi = utils.load_contract_abi("DemandReduction")

    # Connect Externally
    # brownie_contract = Contract.from_explorer(contract_address)

    # Connect Locally
    brownie_contract = Contract(contract_address) # an example of getting a contract using Brownie
    
    web3_contract = web3.eth.contract(address=contract_address, abi=contract_abi) # example of getting contract using web3
    reduction_event_filter = web3_contract.events.notify_reduction.createFilter(fromBlock='latest') # using web3 contract instance for events

    while True:
        # request energy reduction
        energy_reduction = int(float(input("Desired energy reduction amount: ")) * 10**3)
        # amount: give a threshold amount of eth to disperse for rewards, as we don't know ahead of time what the reward value will be
        brownie_contract.request_reduction(energy_reduction, {"from": account, "amount": 0.01e18}) 

        # input("Press when bids have been submitted. . .")
        time.sleep(30)

        # select winners
        brownie_contract.select_winners({"from": account}) # using brownie contract instance for calling functions

        # display results
        print("Awaiting results. . .")
        tx = utils.listen_for_event(reduction_event_filter, web3_contract)
        results = web3.toJSON(tx[0]) 
        results = json.loads(results)
        print("Total energy reduction: ", results["args"]["power"] / 10**3, " kWh")
        print("Total reward dispersed: ", results["args"]["reward"] / 10**18, " ether")