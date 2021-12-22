from brownie import accounts, FundMe, config
from scripts.tooling import get_account


def deploy_fund_me():
    account = get_account()
    fund_me = FundMe.deploy({"from": account})
    print(f"FundMe.sol Deployed to {fund_me.address}")


def main():
    deploy_fund_me()
