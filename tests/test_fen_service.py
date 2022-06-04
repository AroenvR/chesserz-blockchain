from brownie import accounts, chain, FenService, FenBoard

# UnitTest.
# Execute: brownie test | brownie test -s | test -s has less clutter in terminal.
# To test a single function execute (function name): brownie test -k test_deploy 
# To debug a single executed test: brownie test --pdb
# Then you can enter variables or methods to check their return values.
# https://docs.pytest.org/en/6.2.x/contents.html

INITIAL_BOARD_STATE = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

def test_deploy():
    # Arrange
    account = accounts[0]
    fen_service_contract = FenService.deploy({"from": account})
    
def test_create_new_board():
    # Arrange
    account = accounts[0]
    fen_service_contract = FenService.deploy({"from": account})

    account_white = accounts[1]
    account_black = accounts[2]

    # Creating new board
    board_transaction = fen_service_contract.createNewBoard(account_white, account_black, {"from": account_white})
    board_transaction.wait(1)

    # Grabbing the new board's address
    find_board_by_addresses = fen_service_contract.findBoardByAddresses(account_white, account_black)
    print(find_board_by_addresses)

    # Grabbing the board's state
    board_state = fen_service_contract.getBoardState(account_white, account_black)

    # Asserting the board's state
    assert board_state == INITIAL_BOARD_STATE

    # Updating the board's state
    update_transaction = fen_service_contract.updateBoardState("NEW STATE", account_white, account_black, {"from": account_white})
    update_transaction.wait(1)

    # Grabbing the board's state
    board_state = fen_service_contract.getBoardState(account_white, account_black)

    # Asserting the board's state
    assert board_state == "NEW STATE"