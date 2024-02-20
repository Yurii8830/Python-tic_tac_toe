def print_board(board):
    # Функція для виведення поточного стану дошки з пронумерованими рядками та стовпцями
    print("   0   1   2")
    for i, row in enumerate(board):
        print(f"{i}  {' | '.join(row)}")
        if i < 2:
            print("  " + "-" * 11)

def check_win(board, player):
    # Перевіряє, чи виграв гравець
    for row in board:
        if all([cell == player for cell in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

def is_board_full(board):
    # Перевіряє, чи заповнена вся дошка
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def tic_tac_toe():
    # Ініціалізує пусту дошку та початкових гравців
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']

    player1_name = input("Введіть ім'я першого гравця: ")
    player2_name = input("Введіть ім'я другого гравця: ")

    print(f"Гра 'Хрестики-нулики' між {player1_name} та {player2_name} починається!")
    print("Кожен гравець по черзі вводить номер рядка (від 0 до 2) та стовпця (від 0 до 2) для свого ходу.")

    for i in range(9):
        current_player = players[i % 2]
        print_board(board)
        row = int(input(f"{current_player}, введіть номер рядка (0, 1, 2): "))
        col = int(input(f"{current_player}, введіть номер стовпця (0, 1, 2): "))

        if board[row][col] != " ":
            print("Ця клітинка вже зайнята! Оберіть іншу.")
            continue

        board[row][col] = current_player

        if check_win(board, current_player):
            print_board(board)
            print(f"Гравець {current_player} ({player1_name if current_player == 'X' else player2_name}) переміг!")
            break

        if is_board_full(board):
            print_board(board)
            print("Нічия!")
            break

    print("Гра завершена.")

if __name__ == "__main__":
    tic_tac_toe()
