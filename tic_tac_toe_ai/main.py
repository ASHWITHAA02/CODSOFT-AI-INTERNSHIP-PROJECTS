from board import Board
from ai import best_move

game = Board()

print("TIC TAC TOE - Human vs AI")
print("You are X, AI is O")

while True:

    game.display()

    try:
        move = int(input("Enter position (1-9): ")) - 1
    except:
        print("Invalid input")
        continue

    if not game.make_move(move, "X"):
        print("Position already taken!")
        continue

    if game.winner("X"):
        game.display()
        print("🎉 You win!")
        break

    if game.is_full():
        game.display()
        print("Draw!")
        break

    ai_move = best_move(game)
    game.make_move(ai_move, "O")

    print(f"AI chooses position {ai_move+1}")

    if game.winner("O"):
        game.display()
        print("🤖 AI wins!")
        break

    if game.is_full():
        game.display()
        print("Draw!")
        break