from brownie import network, accounts, exceptions
from scripts.tooling import get_account, LOCAL_DEVELOPMENT_ENVIRONEMENTS
from scripts.deploy import deploy_fund_me
import pytest


def test_can_fund_and_withdraw():
    account = get_account()
    fund_me = deploy_fund_me()
    entrance_free = fund_me.getEntranceFee()
    tx = fund_me.fund({"from": account, "value": entrance_free})
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == entrance_free
    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0


def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_DEVELOPMENT_ENVIRONEMENTS:
        pytest.skip("only for local testing")
    fund_me = deploy_fund_me()
    bad_actor = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": bad_actor})
