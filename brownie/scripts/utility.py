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

    brownie_contract = Contract(contract_address) # an example of getting a contract using Brownie
    web3_contract = web3.eth.contract(address=contract_address, abi=contract_abi) # example of getting contract using web3

    while True:
        # request energy reduction
        energy_reduction = int(float(input("Desired energy reduction amount: ")) * 10**3)
        brownie_contract.request_reduction(energy_reduction, {"from": account, "amount": 0.01e18})

        input("Press enter to continue. . .")

        # select winners
        reduction_event_filter = web3_contract.events.notify_reduction.createFilter(fromBlock='latest') # using web3 contract instance for events
        brownie_contract.select_winners({"from": account}) # using brownie contract instance for calling functions

        # display results
        print("Awaiting results. . .")
        tx = utils.listen_for_event(reduction_event_filter)
        results = web3.toJSON(tx[0]) 
        results = json.loads(results)
        print("Total energy reduction: ", results["args"]["power"] / 10**3, " kWh")
        print("Total reward dispersed: ", results["args"]["reward"] / 10**18, " ether")


    # tx = contract.getBids.call({"from": accounts[0]})