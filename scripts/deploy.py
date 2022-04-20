#!/usr/bin/python3
from brownie import DemandReduction, accounts
from . import utils
import os
from dotenv import load_dotenv, find_dotenv, set_key

env = find_dotenv()
load_dotenv(env)
utils.load_account("UTILITY_ACCOUNT")

def main():
    # Deploy Locally -- if deploying locally, update consumer and utility scripts to read locally as well
    # dr = DemandReduction.deploy({'from': accounts[0]})
    dr = DemandReduction.deploy({'from': accounts[0]}, publish_source=True)
    set_key(env, "CONTRACT_ADDRESS", dr.address)
    return dr
    
