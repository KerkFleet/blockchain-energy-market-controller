from sqlite3 import connect
from brownie import web3 
import time

import json

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