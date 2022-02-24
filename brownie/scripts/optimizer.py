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

    contract.optimize_bids({"from": accounts[0]})