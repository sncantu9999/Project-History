import random


def create_board():
    return [' ' for i in range(9)]


def print_board(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-+-+-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-+-+-")
    print(board[6] + "|" + board[7] + "|" + board[8])
    print()


def board_not_full(board):
    return ' ' in board


def remaining_spots(board):
    lst = []
    for i in range(len(board)):
        if board[i] == ' ':
            lst.append(i)
    return lst


def select_move(letter, board):
    available_spot = False
    while available_spot == False:
        spot_invalid = True
        while (spot_invalid):
            spot = input(
                f"Player {letter}'s turn. Please select your spot (0 to 8) ")
            if spot.isdigit():
                spot = int(spot)
                if spot >= 0 and spot < 9:
                    if board[spot] == ' ':
                        spot_invalid = False
        available_spot = True
    return spot


def place_move(letter, board, move):
    if board[move] == ' ':
        board[move] = letter
        return True
    return False


def is_list_same_letter(lst):
    if lst[0] == ' ':
        return False
    letter = lst[0]
    matching_letter = True
    for i in lst:
        if i != letter:
            matching_letter = False
    if matching_letter == True:
        return True
    return False


def winner_exists(board):
    for row_number in range(3):
        row = board[row_number*3: (row_number+1)*3]
        if is_list_same_letter(row):
            return row[0]
    for col_num in range(3):
        col = [board[col_num+i*3] for i in range(3)]
        if is_list_same_letter(col):
            return col[0]
    diag1 = [board[0], board[4], board[8]]
    diag2 = [board[2], board[4], board[6]]
    if is_list_same_letter(diag1):
        return diag1[0]
    elif is_list_same_letter(diag2):
        return diag2[0]
    return False


def computer_selects_move(letter, board):
    if len(remaining_spots(board)) == 9:
        return random.randint(0, 9)
    else:
        res = minimax(letter, letter, board)
        return res


def minimax(computer_letter, player, board):
    max_player = computer_letter
    min_player = 'O' if max_player == 'X' else 'X'
    empty_spots = remaining_spots(board)
    if (winner_exists(board) == max_player):
        return 10
    elif winner_exists(board) == min_player:
        return -10
    elif len(empty_spots) == 0:
        return 0
    moves = []
    for i in range(len(empty_spots)):
        move = {}
        move['index'] = empty_spots[i]
        board[empty_spots[i]] = player
        if player == max_player:
            temp_score = minimax(computer_letter, min_player, board)
            move['score'] = temp_score
        else:
            temp_score = minimax(computer_letter, max_player, board)
            move['score'] = temp_score
        board[empty_spots[i]] = ' '
        moves.append(move)
    if player == computer_letter:
        bestscore = -100000000
        for i in range(len(moves)):
            if ((moves[i])['score'] > bestscore):
                bestscore = moves[i]['score']
                bestmove = i
    else:
        bestscore = 100000000
        for i in range(len(moves)):
            if ((moves[i])['score'] < bestscore):
                bestscore = moves[i]['score']
                bestmove = i
    return moves[bestmove]['index']


def play_game(player_letter, computer_letter, board):
    print_board(board)
    letter_to_move = 'X'
    while board_not_full(board):
        if letter_to_move == player_letter:
            move = select_move(letter_to_move, board)
        else:
            move = computer_selects_move(letter_to_move, board)
        if place_move(letter_to_move, board, move):
            print_board(board)
            result = winner_exists(board)
            if result != False:
                print(f"Player {result} won!")
                play_again = input(
                    "Would you like to play again? Y/N ").lower()
                while play_again != 'y' and play_again != 'n':
                    print("Sorry, that is not a valid choice!")
                    play_again = input(
                        "Would you like to play again? Y/N ").lower()
                return play_again
        letter_to_move = 'O' if letter_to_move == 'X' else 'X'
    print("It's a tie!")
    play_again = input("Would you like to play again? Y/N ").lower()
    while play_again != 'y' and play_again != 'n':
        print("Sorry, that is not a valid choice!")
        play_again = input("Would you like to play again? Y/N ").lower()
    return play_again


def main():
    play_again = True
    while play_again == True:
        player_letter = input(
            "Which would you like to choose? O or X? ").lower()
        while player_letter != 'o' and player_letter != 'x':
            print("Sorry, that is not a valid choice!")
            player_letter = input(
                "Which would you like to choose? O or X? ").lower()
        player_letter = player_letter.upper()
        computer_letter = 'X' if player_letter == 'O' else 'O'
        board = create_board()
        play_again = play_game(player_letter, computer_letter, board)
        play_again = True if play_again == 'y' else False
    print("Thank you for playing!")


main()
