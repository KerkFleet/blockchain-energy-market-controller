#!/usr/bin/python3
from brownie import DemandReduction, accounts
import os
from dotenv import load_dotenv, find_dotenv, set_key

accounts.load('test-rinkeby')
env = find_dotenv()
load_dotenv(env)

def main():
    # dr = DemandReduction.deploy({'from': accounts[0]})
    dr = DemandReduction.deploy({'from': accounts[0]}, publish_source=True)
    set_key(env, "CONTRACT_ADDRESS", dr.address)
    return dr
    
