from brownie import web3, accounts
from dotenv import load_dotenv, find_dotenv
from . import utils
import os

accounts.load('test-rinkeby')
env = find_dotenv()
load_dotenv(env)


def main():
    # load contract data
    contract_address = os.environ.get('CONTRACT_ADDRESS')
    contract_abi = utils.load_contract_abi("DemandReduction")

    # load contract
    contract = web3.eth.contract(address=contract_address, abi=contract_abi) # example of getting contract using web3
    print("Connection created.")

    contract.functions.register().call()