from brownie import web3, accounts
from dotenv import load_dotenv, find_dotenv
from . import utils
import os

accounts.load('test-rinkeby')
env = find_dotenv()
load_dotenv(env)



def main():
    energy = []
    value = []
    count = 0
    while True:
        count = count + 1
        print(f"Block {count}:")
        e = input("Energy amount: ")
        v = input("Energy value: ")
        energy.append(e)
        value.append(v)
        cont = input("Add another?(y/n): ")
        if cont == 'n' or cont == 'N':
            break

    print("Your bids input: ")
    print("Energy: ", energy)
    print("Values: ", value)
    
    print("Setting up contract connection. . .")

    # load contract data
    contract_address = os.environ.get('CONTRACT_ADDRESS')
    contract_abi = utils.load_contract_abi("DemandReduction")

    # load contract
    contract = web3.eth.contract(address=contract_address, abi=contract_abi) # example of getting contract using web3
    print("Connection created.")

    print("Now waiting for a demand response request. . .")
    # create filter for event to listen to
    event_filter = contract.events.notify_consumer.createFilter(fromBlock='latest')
    while True:
        utils.listen_for_event(event_filter)
        print("Time to submit bids")
        #call bid submitting function here



    



