from . import utils
from brownie import Contract, accounts, web3
from dotenv import load_dotenv, find_dotenv
import os

accounts.load('test-rinkeby')
env = find_dotenv()
load_dotenv(env)

def main():
    contract_address = os.environ.get("CONTRACT_ADDRESS")

    contract = Contract(contract_address) # an example of getting a contract using Brownie

    # energy_reduction = input("Desired energy reduction amount: ")
    # contract.disperse_rewards({"from": accounts[0]})
    # contract.request_reduction(energy_reduction, {"from": accounts[0], "amount": 0.01e18})
    contract.select_winners({"from": accounts[0]})
    # tx = contract.getBids.call({"from": accounts[0]})

    # print(tx)
    # print(txt)
    # print(txt.return_value)
    
    # Does not work
    # gas_limit: 6721975
    # contract.optimize_bids({"from": accounts[0]})

