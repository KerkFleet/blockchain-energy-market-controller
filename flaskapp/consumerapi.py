import subprocess
import json
from pathlib import Path
import sys
from flask import Flask, request, render_template
app = Flask(__name__)


global pid 
pid = None

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def submit():
    f = open(Path(__file__).parent.parent / 'database' / 'bids.json', "w")
    energy = []
    price = []
    for e, p in zip(request.form.getlist("energy"), request.form.getlist("price")):
        energy.append(float(e))
        price.append(float(p))
    data = json.dumps({"energy": energy, "price": price})
    f.write(data)
    f.close()
    global pid
    if not pid:
        pid = subprocess.Popen(["brownie", "run", "../scripts/consumer.py", "main", "remote", "--network", "rinkeby"], 
                                        text=True,
                                        stdout=sys.stdout
                                        )
    results, bids = read_data()
    t = results["time"]
    pdata=[]
    for e, p, i in zip(bids["energy"], bids["price"], range(len(bids["energy"]))):
        pdata.append("Bid " + str(i) + ": Energy: " +  str(e) + ", Price: " + str(p))

    return render_template("results.html", results=results, bids=pdata, time=t)

@app.route('/results', methods=['GET'])
def refresh():
    results, bids = read_data()
    t = results["time"]
    pdata=[]
    for e, p, i in zip(bids["energy"], bids["price"], range(len(bids["energy"]))):
        pdata.append("Bid " + str(i) + ": Energy: " +  str(e) + ", Price: " + str(p))
    return render_template("results.html", results=results, bids=pdata, time=t)
    

def read_data():
    f = open(Path(__file__).parent.parent / 'database' / 'results.json', "r")
    results = json.load(f)
    f.close()
    f = open(Path(__file__).parent.parent / 'database' / 'bids.json', "r")
    bids = json.load(f)
    f.close()
    return results, bids


if __name__ == '__main__':
    app.debug = True
    app.run()