import os
import time
import json
from dotenv import load_dotenv, find_dotenv
from brownie import accounts, web3

def load_contract_abi(contract_name : str):
    f = open(f"./build/contracts/{contract_name}.json")
    abi = json.load(f)["abi"]
    return abi

def listen_for_event(event_filter, contract, poll_interval=2):
    latest = web3.eth.get_block('latest')["number"]
    while True:
        event = event_filter.get_new_entries()
        if event:
            return event
        time.sleep(poll_interval)
        # if web3.eth.get_block('latest')["number"] > latest+5:
        #     latest = web3.eth.get_block('latest')["number"]
        #     event_filter = contract.events.notify_rewards.createFilter(fromBlock='latest')
        #     print(latest)

def load_env():
    env = find_dotenv()
    load_dotenv(env)
    return env

def load_account(account_type : str):
    account_name = os.environ.get(account_type)
    password = os.environ.get(account_type + "_PASS")
    return(accounts.load(account_name, password=password))


