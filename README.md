### How to set up a SmartContract deployment server (with Brownie)

Check pipx's installtion with python3 -m pipx --version
Check Brownie's installtion with brownie --version

If pipx is not installed:
    python3 -m pip install --user pipx
    python3 -m pipx ensurepath
        Whatever paths get listed here, check your system's environment variables.
        To make sure they were added.
        Otherwise, copy-paste them.

If brownie is not installed:
    python3 -m pipx install eth-brownie
        Ensure the following folder exists and that the path is also added to your system's environment variables.
        C:\Users\USERNAME\.local\pipx\venvs\eth-brownie\Scripts

Set up environment variables (omitted for security reasons).
Set up a brownie-config.yml file (omitted for security reasons).

SmartContract.sol should be located in the contracts folder (not build\contracts).
deploy.py should be located in the scripts folder.

To deploy your SmartContract on the Rinkeby Testnet execute: brownie run scripts/deploy.py --network rinkeby

```py
scripts/deploy.py example:
from brownie import accounts, network, config, SomeContract

def get_account():
    if(network.show_active() == "development"):
        return accounts[0]
    return accounts.add(config["wallets"]["from_key"])

def deploy_smart_contract():
    account = get_account()
    SomeContract.deploy({"from": account}) # deploy SomeContract.

def main():
    deploy_smart_contract()
```




