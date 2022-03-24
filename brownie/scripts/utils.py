import os
import time
import json
from dotenv import load_dotenv, find_dotenv
from brownie import accounts

def load_contract_abi(contract_name : str):
    f = open(f"./build/contracts/{contract_name}.json")
    abi = json.load(f)["abi"]
    return abi

def listen_for_event(event_filter, poll_interval=2):
    while True:
        event = event_filter.get_new_entries()
        if event:
            return event
        time.sleep(poll_interval)

def load_env():
    env = find_dotenv()
    load_dotenv(env)

def load_account(account_type : str):
    account_name = os.environ.get(account_type)
    return(accounts.load(account_name))


