from brownie import Contract, web3, accounts
from dotenv import load_dotenv, find_dotenv
from . import utils
import os

accounts.load('test-rinkeby-2')
env = find_dotenv()
load_dotenv(env)


def main(remote=None):
    # load contract data
    contract_address = os.environ.get('CONTRACT_ADDRESS')

    contract = None
    if remote:
        # connect to remote contract
        print("Creating remote contract connection.")
        contract = Contract.from_explorer(contract_address)
    else:
        # connect to local contract
        contract = Contract(contract_address)

    contract.register({"from": accounts[0]})