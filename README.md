## Repo Description

This is the Blockchain Energy Market Controller Repo. This repo contains code which allows an energy utlity to request an energy reduction which will notify the consumer's machine. The consumer is running a script which will automatically submit bids to the smart contract. After a time set by the utility (60 seconds in the utility script currently) the utility will execute the select_winners function of the smart contract and winners will be selected with those consumers being notified of winning bids and ethereum being dispersed into their wallets.


## Utility Scripts

The utility has two scripts, both of which reside in the bemc-python/scripts folder. The first script is the deploy.py script which allows the utility to deploy a smart conctract onto the block chain. The second is the utiliy.py script which should be ran every time the utility wants to request a demand reduction from the consumers. 

## Consumer Scripts

The consumer has one script in the bemc-python/scripts folder titled consumer.py which when ran will connect to the smart contract and wait for a demand reduction notification. Upon being notified the consumer.py script will grab the bids from the bemc-python/database/bids.json file and submit them to the contract. 

The consumer also has a front end flask app located in the bemc-python/flaskapp folder which was created by the Fall2021/Spring2022 Senior Design team for demonstration purposes. The App allows the user to enter in bids and observe winning bids.

## Smart contract

Smart contracts are deployed once and connot be modified or deleted from the chain. If the smart contract's functionality or code must be updated the utility will need to deploy a new smart contract and all consumers on the system will need to update their CONTRACT_ADDRESS in the .env file. 

The smart contract is located in the bemc-python/contracts folder titled Demand_Reduction.sol.

## Environment setup

I would recommend setting up a python virtual environment first by executing:

```bash
python3 -m venv .venv
```

and to activate:

```bash
source .venv/bin/activate
```
## Adding ETH accounts to pay for transactions:

* First, execute:

  ```bash
  brownie accounts new <name_of_account>
  ```

* Paste the private key for your wallet in when prompted.
* **For convenience, set a password for your account.** Not setting a password will result in `brownie` prompting for a password on each script execution.
* Paste your password into the `.env` file for `CONSUMER_ACCOUNT_PASS`
* Paste `<name of account>` into the `.env` file for `CONSUMER_ACCOUNT`
* Keep in mind this demo runs on the rinkeby test network, so you must have eth in your rinkeby account. 


## Running Brownie Scripts

* Start by deploying the smart contract:
  ```bash
  brownie run scripts/deploy.py
  ```
* Fill out consumer Bid data in `database/bids.json` with the desired data
* Start the consumer script with: 
  ```bash
  brownie run scripts/consumer.py
  ```
* In a separate terminal, start the utility script with:
  ```bash
  brownie run scripts/utility.py
  ```
* Follow the prompts to make a reduction request.
* Results will appear in `database/results.json`, and be printed to the screen as well.


**Note: Use the `--remote` argument with all of the scripts above when utilizing multiple devices. The scripts are set for local development only by default.**


## Flask App

A basic form has been created utilizing flask to create a demonstration front end for the `scripts/consumer.py`.

To run this proof of concept using the Flask app, a script has been written. 

* First make the script executable:

```bash
chmod +x run_flask.sh
```

* Then, run the script:

```bash
./run_flask.sh
```

* An alternative option to the above is to run the three commands below:

```bash
export FLASK_APP=flaskapp/consumerapi.py
export FLASK_ENV=development
flask run
```

* Lastly, click the local server link on screen. Fill in the front end form as desired.

A separate terminal must still be used to execute the utility script and make a demand reduction request, either on the same device, or a separate one.

**Note: the flask app is hardcoded to execute `scripts/consumer.py` with the `--remote` argument.**


## Testing

To run the tests:

```bash
brownie test
```

**Note, there are no working tests for this software, but the preset tests have been left for reference for adding tests in the future**


## Resources

https://gist.github.com/plembo/6bc141a150cff0369574ce0b0a92f5e7

## License

This project is licensed under the [MIT license](LICENSE).

