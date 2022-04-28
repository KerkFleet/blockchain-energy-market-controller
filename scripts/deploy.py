#!/usr/bin/python3
from brownie import DemandReduction, accounts
from . import utils
import os
from dotenv import load_dotenv, find_dotenv, set_key

env = find_dotenv()
load_dotenv(env)
utils.load_account("UTILITY_ACCOUNT")

def main(remote=None):
    dr = None
    if remote:
        # Deploy remotely
        print("Publishing contract remotely")
        dr = DemandReduction.deploy({'from': accounts[0]}, publish_source=True)
    else:
        # Deploy Locally -- if deploying locally, update consumer and utility scripts to read locally as well
        print("Publishing contract locally")
        dr = DemandReduction.deploy({'from': accounts[0]})
    set_key(env, "CONTRACT_ADDRESS", dr.address)
    return dr
    
