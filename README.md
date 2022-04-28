# Repo Description

This is the Blockchain Energy Market Controller Repo. This repo contains code which allows an energy utlity to request an energy reduction which will notify the consumer's machine. The consumer is running a script which will automatically submit bids to the smart contract. After a time set by the utility (60 seconds in the utility script currently) the utility will execute the select_winners function of the smart contract and winners will be selected with those consumers being notified of winning bids and ethereum being dispersed into their wallets.


## Utility Scripts

The utility has two scripts, both of which reside in the bemc-python/scripts folder. The first script is the deploy.py script which allows the utility to deploy a smart conctract onto the block chain. The second is the utiliy.py script which should be ran every time the utility wants to request a demand reduction from the consumers. 

## Consumer Scripts

The consumer has one script in the bemc-python/scripts folder titled consumer.py which when ran will connect to the smart contract and wait for a demand reduction notification. Upon being notified the consumer.py script will grab the bids from the bemc-python/database/bids.json file and submit them to the contract. 

The consumer also has a front end flask app located in the bemc-python/flaskapp folder which was created by the Fall2021/Spring2022 Senior Design team for demonstration purposes. The App allows the user to enter in bids and observe winning bids.

## Smart contract

Smart contracts are deployed once and connot be modified or deleted from the chain. If the smart contract's functionality or code must be updated the utility will need to deploy a new smart contract and all consumers on the system will need to update their CONTRACT_ADDRESS in the .env file. 

The smart contract is located in the bemc-python/contracts folder titled Demand_Reduction.sol.

# **Project Build**

## **Environment Setup**
This code was setup using Python version 3.8.10 running in Ubuntu 20.04. It requires some of the developer tools to use. Other versions of Python have been known to cause issues. The best way of installing python and the related tools on Ubuntu has been to use the instructions found at the following [gist]( 
https://gist.github.com/plembo/6bc141a150cff0369574ce0b0a92f5e7).

Be sure to replace `Python3.9` with `Python3.8` throughout the instructions. 
First, set up a virtual environment:
```bash
python3.8 -m venv .venv
```
Activate the virtual environment:
```bash
source .venv/bin/activate
```
Install dependencies:
```bash
pip install -r requirements.txt
```
## **Environment Variables**
The `.env` file must be filled out to some extent to run this project.
Make a copy of the template:
```bash
cp .env.template .env
```

#### **API Keys**
This project relies on a few external tools that facilitate in connecting to the smart contract on the blockchain network. The default network that this project is set to run on is the rinkeby test network. This can be altered - see [brownie's documentation](https://eth-brownie.readthedocs.io/en/stable/).


An API key from both Infura (a node provider) and Etherscan are needed and can be pasted into the corresponding variable in the `.env` file. Be sure to use the api key provided for the network being used(in this case, rinkeby).

#### **Contract Address**

`CONTRACT_ADDRESS` will be filled in automatically upon first smart contract deploy.

#### **Ethereum accounts**
Ethereum wallets are required to provide funds for transactions.

Add an account for both consumer and utility:
  ```bash
  brownie accounts new <name_of_account>
  ```
* Paste the private key for your wallet in when prompted.
* **For convenience, set a password for your account.** Not setting a password will result in `brownie` prompting for a password on each script execution.
* Paste your password into the `.env` file for `CONSUMER_ACCOUNT_PASS`
* Paste `<name of account>` into the `.env` file for `CONSUMER_ACCOUNT`
* Keep in mind this demo runs on the rinkeby test network, so you must have eth in your rinkeby account. 

# **Project Usage**

 Start by deploying the smart contract:
  ```bash
  brownie run scripts/deploy.py
  ```
 Fill out consumer Bid data in `database/bids.json` with the desired data

 Start the consumer script with: 
  ```bash
  brownie run scripts/consumer.py
  ```
 In a separate terminal(or device), start the utility script with:
  ```bash
  brownie run scripts/utility.py
  ```
Follow the prompts to make a reduction request.

 Results will appear in `database/results.json`, and be printed to the screen as well.


**Note:** When working with multiple devices using this project, use:
 ```bash
 brownie run scripts/<script_name> main remote 
```

# **Flask App**

A basic form has been created utilizing flask to create a demonstration front end for the `scripts/consumer.py`.

To run this proof of concept using the Flask app, a script has been written. 

Make the script executable:

```bash
chmod +x run_flask.sh
```

Run the script:

```bash
./run_flask.sh
```

An alternative option to the above is to run the three commands below:

```bash
export FLASK_APP=flaskapp/consumerapi.py
export FLASK_ENV=development
flask run
```

Click the local server link on screen. Fill in the front end form as desired.

A separate terminal must still be used to execute the utility script and make a demand reduction request, either on the same device, or a separate one.

**Note:** The flask app is hardcoded to execute `scripts/consumer.py` with the `main remote` argument.


# **Testing**

To run the tests:

```bash
brownie test
```

**Note**: there are no working tests for this software, but the preset tests have been left for reference for adding tests in the future

# **Running on IOT Devices**

Many IOT devices run on ARM64 architecture. Unfortunately, there is not much support regarding solidity compilers for this architecture. There are some unofficial repos where binaries for such a compiler have been made.

We had success making this project work on an Nvidia Jetson Nano utilizing binaries from the following [repo](https://github.com/nikitastupin/solc).

From the above repo, download `solc-v0.8.13`

Move `solc-v0.8.13` into the `~/.solcx` directory.

Navigate to the `~/.solcx` directory.

Make the binary executable:
```bash
chmod +x ./solc-v0.8.13
```
Test if it works(a help menu should appear):
```bash
./solc-v0.8.13
```

From here, continue to run brownie scripts as usual.
## Resources

Setting up Python: https://gist.github.com/plembo/6bc141a150cff0369574ce0b0a92f5e7

Brownie Docs: https://eth-brownie.readthedocs.io/en/stable/

Solidity aarch64 binaries: https://github.com/nikitastupin/solc

## License

This project is licensed under the [MIT license](LICENSE).

