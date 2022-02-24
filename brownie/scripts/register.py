from brownie import Contract, web3, accounts
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
    contract = Contract(contract_address)
    print("Connection created.")

    # test = contract.check_registered(accounts[0])
    contract.register({"from": accounts[0]})
    # print(test)