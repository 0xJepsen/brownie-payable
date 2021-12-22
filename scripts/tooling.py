from brownie import accounts, config, network, MockV3Aggregator
from web3 import Web3
import os

UNISWAP_BATCH_SIZE = 1000
FACTORY_ADDRESS = [
    os.getenv("CRO_FACTORY_ADDRESS"),
    os.getenv("ZEUS_FACTORY_ADDRESS"),
    os.getenv("LUA_FACTORY_ADDRESS"),
    os.getenv("SUSHISWAP_FACTORY_ADDRESS"),
    os.getenv("UNISWAP_FACTORY_ADDRESS"),
]
BATCH_COUNT_LIMIT = 100

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork"]
DECIMALS = 8
STARTING_PRICE = 200000000000
LOCAL_DEVELOPMENT_ENVIRONEMENTS = ["development", "ganache-local"]


def get_account():
    if (
        network.show_active() in LOCAL_DEVELOPMENT_ENVIRONEMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The active netowrk is {network.show_active()}")
    print("Deploying Mocks...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
    print("Mocks Deployed!")
