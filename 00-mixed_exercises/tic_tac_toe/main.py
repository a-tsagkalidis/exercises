import random
from termcolor import colored
game_is_over = False
draw_list = [1]

pos_dict = {"1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9"}

row1 = [pos_dict["1"], pos_dict["2"], pos_dict["3"]]
row2 = [pos_dict["4"], pos_dict["5"], pos_dict["6"]]
row3 = [pos_dict["6"], pos_dict["7"], pos_dict["8"]]

board = [row1, row2, row3]

def display_board(board):
  print("+———————————+")
  print("| "+pos_dict["1"] +" | "+ pos_dict["2"] +" | "+ pos_dict["3"]+" |")
  print("+———+———+———+")
  print("| "+pos_dict["4"] +" | "+ pos_dict["5"] +" | "+ pos_dict["6"]+" |")
  print("+———+———+———+")
  print("| "+pos_dict["7"] +" | "+ pos_dict["8"] +" | "+ pos_dict["9"]+" |")
  print("+———————————+")


random_pc_start = str(random.randint(1, 9))
pos_dict[random_pc_start] = colored ("X", "blue")
print(f"PC selects position '{random_pc_start}'")
display_board(board)


def user_pick():
  user_tile = (input("\nSelect a position: "))
  if user_tile not in pos_dict.values():
    print (colored ("\nNot a valid position!", "magenta"))
    user_pick()
  elif pos_dict[user_tile] == colored ("X", "blue") or pos_dict[user_tile] == colored("O", "green"):
    print(colored("\nPick another position. This one is occupied!", "magenta"))
    user_pick()
  else:
    pos_dict[user_tile] = colored("O", "green")
    draw_list.append(1)


def pc_pick():
  pc_tile = str(random.randint(1, 9))
  if pos_dict[pc_tile] == colored ("X", "blue") or pos_dict[pc_tile] == colored("O", "green"):
    pc_pick()
  else:
    pos_dict[pc_tile] = colored ("X", "blue")
    draw_list.append(1)
    print(f"\nPC selects position '{pc_tile}'")


def win_conditions():
  global you_win
  you_win = False
  if pos_dict["1"] == colored("O", "green") and pos_dict["4"] == colored("O", "green") and pos_dict["7"] == colored("O", "green") \
  or pos_dict["1"] == colored("O", "green") and pos_dict["2"] == colored("O", "green") and pos_dict["3"] == colored("O", "green") \
  or pos_dict["3"] == colored("O", "green") and pos_dict["6"] == colored("O", "green") and pos_dict["9"] == colored("O", "green") \
  or pos_dict["7"] == colored("O", "green") and pos_dict["8"] == colored("O", "green") and pos_dict["9"] == colored("O", "green") \
  or pos_dict["2"] == colored("O", "green") and pos_dict["5"] == colored("O", "green") and pos_dict["8"] == colored("O", "green") \
  or pos_dict["4"] == colored("O", "green") and pos_dict["5"] == colored("O", "green") and pos_dict["6"] == colored("O", "green") \
  or pos_dict["1"] == colored("O", "green") and pos_dict["5"] == colored("O", "green") and pos_dict["9"] == colored("O", "green") \
  or pos_dict["3"] == colored("O", "green") and pos_dict["5"] == colored("O", "green") and pos_dict["7"] == colored("O", "green"):
    you_win = True


def lose_conditions():
  global you_lose
  you_lose = False
  if pos_dict["1"] == colored ("X", "blue") and pos_dict["4"] == colored ("X", "blue") and pos_dict["7"] == colored ("X", "blue") \
  or pos_dict["1"] == colored ("X", "blue") and pos_dict["2"] == colored ("X", "blue") and pos_dict["3"] == colored ("X", "blue") \
  or pos_dict["3"] == colored ("X", "blue") and pos_dict["6"] == colored ("X", "blue") and pos_dict["9"] == colored ("X", "blue") \
  or pos_dict["7"] == colored ("X", "blue") and pos_dict["8"] == colored ("X", "blue") and pos_dict["9"] == colored ("X", "blue") \
  or pos_dict["2"] == colored ("X", "blue") and pos_dict["5"] == colored ("X", "blue") and pos_dict["8"] == colored ("X", "blue") \
  or pos_dict["4"] == colored ("X", "blue") and pos_dict["5"] == colored ("X", "blue") and pos_dict["6"] == colored ("X", "blue") \
  or pos_dict["1"] == colored ("X", "blue") and pos_dict["5"] == colored ("X", "blue") and pos_dict["9"] == colored ("X", "blue") \
  or pos_dict["3"] == colored ("X", "blue") and pos_dict["5"] == colored ("X", "blue") and pos_dict["7"] == colored ("X", "blue"):
    you_lose = True


while game_is_over == False:
  user_pick()
  display_board(board)
  win_conditions()
  if you_win == True:
    print("\nYou Win!")
    game_is_over = True
  else:
    pc_pick()
    display_board(board)
    lose_conditions()
    if you_lose == True:
      print("\nYou Lose!")
      game_is_over = True
  if len(draw_list) == 9 and game_is_over == False:
    print("\nIt's a Draw!")
    game_is_over = True
