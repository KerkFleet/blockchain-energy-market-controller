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
* ** For convenience, set a password for your account. ** Not setting a password will result in `brownie` prompting for a password on each script execution.
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


** Note: Use the `--remote` argument with all of the scripts above when utilizing multiple devices. The scripts are set for local development only by default. **


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

** Note: the flask app is hardcoded to execute `scripts/consumer.py` with the `--remote` argument.


## Testing

To run the tests:

```bash
brownie test
```

** Note, there are no working tests for this software, but the preset tests have been left for reference for adding tests in the future **


## Resources

https://gist.github.com/plembo/6bc141a150cff0369574ce0b0a92f5e7

## License

This project is licensed under the [MIT license](LICENSE).

