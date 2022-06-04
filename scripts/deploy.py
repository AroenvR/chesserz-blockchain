from brownie import accounts, network, config, FenService

def get_account():
    if(network.show_active() == "development"):
        return accounts[0]  # quick test account.
    return accounts.add(config["wallets"]["from_key"]) # actual wallet account.

def deploy_smart_contract():
    account = get_account()
    FenService.deploy({"from": account}) # deploy FenService contract.

# def test_deploy():
#     print("-----------------")

#     account = accounts[0]
#     fen_service_contract = FenService.deploy({"from": account})

#     account_white = accounts[1]
#     account_black = accounts[2]

#     board_transaction = fen_service_contract.createNewBoard(account_white, account_black, {"from": account_white})
#     board_transaction.wait(1)

#     find_board_by_addresses = fen_service_contract.findBoardByAddresses(account_white, account_black)
#     print(find_board_by_addresses)

#     print("Get board state by address")
#     board_state = fen_service_contract.getBoardState(account_white, account_black)
#     print(board_state)

#     update_transaction = fen_service_contract.updateBoardState("NEW STATE", account_white, account_black, {"from": account_white})
#     update_transaction.wait(1)

#     print("Get board state by address")
#     board_state = fen_service_contract.getBoardState(account_white, account_black)
#     print(board_state) 

# Execute: brownie run scripts/deploy.py --network rinkeby
def main():
    deploy_smart_contract()
    # test_deploy()

# Live contract: 0xa43B65D1E6EF7955b954808B3a1E34c036Ae2093