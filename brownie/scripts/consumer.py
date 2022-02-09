from brownie import Contract
import os
from dotenv import load_dotenv, find_dotenv

env = find_dotenv()
load_dotenv(env)

def main():
    contract = Contract(os.environ.get("CONTRACT_ADDRESS"))
    print(contract)