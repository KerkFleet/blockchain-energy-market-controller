#!/usr/bin/python3
from brownie import DemandReduction, accounts
from dotenv import load_dotenv, find_dotenv, set_key

env = find_dotenv()
load_dotenv(env)
accounts.load('test-rinkeby')

def main():
    dr = DemandReduction.deploy({'from': accounts[0]})
    set_key(env, "CONTRACT_ADDRESS", dr.address)
    return dr
    
