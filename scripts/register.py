from brownie import Contract
from . import utils
import os

utils.load_env()
account = utils.load_account("CONSUMER_ACCOUNT")


def main():
    # load contract data
    contract_address = os.environ.get('CONTRACT_ADDRESS')
    contract_abi = utils.load_contract_abi("DemandReduction")

    # load contract
    contract = Contract(contract_address)
    print("Connection created.")

    contract.register({"from": account})

    # test = contract.check_registered(accounts[0])
    # print(test)