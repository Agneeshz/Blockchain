from web3 import Web3

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# print(web3.isConnected())
# print(web3.eth.blockNumber)

account_1 = "0xFa3e7F5B899b0B39448905f43E23E49552b7fD81"
account_2 = "0x215BE891BD7f65d4bF7D4773925B620f4C239a85"

# first acc pvt key
private_key = "884d89c0064eb713c42a538239d2a5b2cd14f5565442871ae73051c98d55cbc5"

# get the nonce
nonce = web3.eth.getTransactionCount(account_1)
# build a transaction
tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.toWei(1, 'ether'),
    # amount of money we need to pay the network for the transaction (to the miners)
    'gas': 200000,
    'gasPrice': web3.toWei('50', 'gwei')
}
# sign the transaction
signed_tx = web3.eth.account.signTransaction(tx, private_key)
# send transaction
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
# get transaction hash (successful)
# print(tx_hash)
print(web3.toHex(tx_hash))