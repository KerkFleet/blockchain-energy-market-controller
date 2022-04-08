## Getting started with Brownie

I would recommend setting up a python virtual environment first by executing:

```bash
python3 -m venv .venv
```

and to activate:

```bash
source .venv/bin/activate
```

## Packages to install

Requirements.txt must still be worked on, but for now just manually install the packages below...

* eth-brownie
* Flask
* web3
* python-dotenv

## Adding ETH accounts to pay for transactions:

```bash
brownie accounts new <name_of_account>
```

Then, paste your private key in for your wallet when prompted. Set a password, then puth that password in your local

.env file to avoid being prompted for a password each time you run the scripts. Leaving a blank password will result in 

begin prompted to enter your password on each script execution.

Keep in mind this demo runs on the rinkeby test network, so you must have eth in your rinkeby account. 


## Running Brownie Scripts

Start by deploying the smart contract:
```bash
brownie run scripts/deploy.py
```

Fill out consumer Bid data in database/bids.json with the desired data

Start the consumer script with: 
```bash
brownie run scripts/consumer.py
```

In a separate terminal, start the utility script with:
```bash
brownie run scripts/utility.py
```
and follow the prompts to make a reduction request.

Results will appear in database/results.json, and be printed to the screen as well.


## Flask App

A basic form has been created utilizing flask to create a demonstration front end for the consumer script.

To run this proof of concept using the Flask app, execute the following commands:

```bash
export FLASK_APP=flaskapp/consumerapi.py
export FLASK_ENV=development
flask run
```

and then click the local server link on screen. Fill in the front end form as desired.

A separate terminal must still be used to execute the utility script and make a demand reduction request.


## Testing

To run the tests:

```bash
brownie test
```

The unit tests included in this mix are very generic and should work with any ERC20 compliant smart contract. To use them in your own project, all you must do is modify the deployment logic in the [`tests/conftest.py::token`](tests/conftest.py) fixture.

## Resources

To get started with Brownie:

* Check out the other [Brownie mixes](https://github.com/brownie-mix/) that can be used as a starting point for your own contracts. They also provide example code to help you get started.
* ["Getting Started with Brownie"](https://medium.com/@iamdefinitelyahuman/getting-started-with-brownie-part-1-9b2181f4cb99) is a good tutorial to help you familiarize yourself with Brownie.
* For more in-depth information, read the [Brownie documentation](https://eth-brownie.readthedocs.io/en/stable/).


Any questions? Join our [Gitter](https://gitter.im/eth-brownie/community) channel to chat and share with others in the community.

## License

This project is licensed under the [MIT license](LICENSE).
