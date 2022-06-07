import json
from web3 import Web3

infura_url="https://mainnet.infura.io/v3/1dcd4c1b8977447f9cf7b925ba7a57e4"
web3=Web3(Web3.HTTPProvider(infura_url))

print(web3.isConnected())
njnjn