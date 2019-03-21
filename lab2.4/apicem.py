import requests
import json
from pprint import pprint
from flask import Flask, render_template, jsonify

hosts = dict()
devices = dict()
topologies = dict()

app = Flask(__name__)

def get_ticket():
    url = 'https://sandboxapic.cisco.com/api/v1/ticket'
    payload = {"username": "devnetuser",
               "password": "Cisco123!"}
    header = {"content-type": "application/json"}
    response = requests.post(url, data=json.dumps(payload), headers=header, verify=False)
    return response.json()['response']['serviceTicket']

def get_request(url, ticket):
    url = f"https://devnetapi.cisco.com/sandbox/apic_em{url}"
    header = {"content-type": "application/json",
              "X-Auth-Token": ticket}
    responce = requests.get(url, headers=header, verify=False)
    return responce.json()

@app.route("/")
def index():
    return render_template("topology.html")

@app.route("/api/topology")
def topology():
    return jsonify(topologies["response"])


if __name__ == "__main__":
    ticket = get_ticket()
    hosts = get_request("/api/v1/host?limit=1&offset=1", ticket)
    devices = get_request("/api/v1/network-device?limit=1&offset=1", ticket)
    topologies = get_request("/api/v1/topology/physical-topology?limit=1&offset=1", ticket)

    # pprint(hosts)
    # pprint(devices)
    # pprint(topologies)

    app.run(debug=True)
