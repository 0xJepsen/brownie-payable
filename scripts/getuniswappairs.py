from brownie import Contract
from scripts.tooling import FACTORY_ADDRESS, UNISWAP_BATCH_SIZE, BATCH_COUNT_LIMIT
import os

blacklistTokens = ["0xD75EA151a61d06868E31F8988D28DFE5E9df57B4"]


def get_contract():
    uniswap_price_feeds = Contract.from_explorer(
        "0x5EF1009b9FCD4fec3094a5564047e190D72Bd511"
    )
    for i in BATCH_COUNT_LIMIT * UNISWAP_BATCH_SIZE:
        pairs = [
            uniswap_price_feeds.getPairsByIndexRange(
                FACTORY_ADDRESS, i, i + UNISWAP_BATCH_SIZE
            )[0]
        ]
        for pair in pairs:
            marketAddress = pair[2]
            tokenAddress = ""
            if pair[0] == os.getenv("WETH_ADDRESS"):
                tokenAddress == pair[1]
            elif pair[1] == os.getenv("WETH_ADDRESS"):
                tokenAddress = pair[0]

            if tokenAddress not in blacklistTokens:
                pass
    #     if (!blacklistTokens.includes(tokenAddress)) {
    #       const uniswappyV2EthPair = new UniswappyV2EthPair(marketAddress, [pair[0], pair[1]], "");
    #       marketPairs.push(uniswappyV2EthPair);
    #     }
    #   }
    uniswap_price_feeds.getPairsByIndexRange(FACTORY_ADDRESS, i, i + UNISWAP_BATCH_SIZE)


def main():
    get_contract()
