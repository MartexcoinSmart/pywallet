import requests
from lxml import html
import sys

#https://blockchain.info/address/121a2C6kbqaPDrRDsbfZFNafcLBDZMum3p
#<td id="final_balance">
#   <font color="green">
#       <span data-c="0">0 BTC</span>
#   </font>
#</td>

#
# Ex: python3 addrep.py ~/tmp/wallet_dump.txt
# 121a2C6kbqaPDrRDsbfZFNafcLBDZMum3p: 0 BTC
# 129oeaukHtXR8xiPqV8Mnb7p6hs9Ev3VwX: 0 BTC
# 12F9DRQRw2wmGrFUiZRQFk9cG2NtEBxYDv: 0 BTC
# 137wgZG4TSNw7Zqt4WrEHS7w2bgfeqXkkZ: 0 BTC
# 13PNjSy4b372f2jMVrHHLZnXXqgAArhwD8: 0 BTC
#

coin_addr_fn = sys.argv[1]
coin_addr_fp = open(coin_addr_fn)
total_balance = 0.0
for coin_addr in coin_addr_fp:
    url = "https://blockchain.info/address/{0}".format(coin_addr)
    page = requests.get(url)
    tree = html.fromstring(page.content)
    td = tree.xpath('//td[@id="final_balance"]')
    balance = td[0][0][0].text
    fbalance = float(balance.split(" ")[0])
    total_balance += fbalance
    print("{0}:\t{1} = {2}".format(coin_addr.rstrip(),balance,total_balance))

coin_addr_fp.close()
