from brownie import FundMe, MockV3Aggregator, config, network
from scripts.tooling import get_account, deploy_mocks, LOCAL_DEVELOPMENT_ENVIRONEMENTS


def deploy_fund_me():
    account = get_account()
    if network.show_active() not in LOCAL_DEVELOPMENT_ENVIRONEMENTS:
        print(config["networks"][network.show_active()])
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"FundMe.sol Deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
