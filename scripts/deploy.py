#!/usr/bin/python3
from brownie import DemandReduction, accounts
from dotenv import load_dotenv, find_dotenv, set_key

from . import utils

env = find_dotenv()
load_dotenv(env)
account = utils.load_account("UTILITY_ACCOUNT")

def main():
    dr = DemandReduction.deploy({'from': account})
    set_key(env, "CONTRACT_ADDRESS", dr.address)
    return dr
    
