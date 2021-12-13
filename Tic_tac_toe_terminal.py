"""
https://en.wikipedia.org/wiki/Box-drawing_character
https://en.wikipedia.org/wiki/List_of_Unicode_characters

https://www.w3schools.com/python/python_ref_set.asp
https://www.w3schools.com/python/python_for_loops.asp
https://www.w3schools.com/python/module_random.asp
https://www.w3schools.com/python/ref_random_choices.asp
https://www.w3schools.com/python/python_for_loops.asp

https://student.cs.uwaterloo.ca/~cs452/terminal.html
https://tldp.org/HOWTO/Bash-Prompt-HOWTO/x361.html

symbols = {'~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/'}

# Backup grid and X, O icons, menu and bot variations.
a = "┌──────────┬──────────┬──────────┐"
b = "│          │          │          │"
c = "│          │          │          │"
d = "│          │          │          │"
f = "│          │          │          │"
g = "├──────────┼──────────┼──────────┤"
h = "│          │          │          │"
i = "│          │          │          │"
j = "│          │          │          │"
k = "│          │          │          │"
m = "├──────────┼──────────┼──────────┤"
n = "│          │          │          │"
p = "│          │          │          │"
q = "│          │          │          │"
r = "│          │          │          │"
s = "└──────────┴──────────┴──────────┘"

# X value 8 spaces, 4 rows
b1 = "  ╲  ╱  "
b2 = "   ╲╱   "
b3 = "   ╱╲   "
b4 = "  ╱  ╲  "

# O value 8 spaces, 4 rows
a1 = "╭──────╮"
a2 = "│      │"
a3 = "│      │"
a4 = "╰──────╯" 


   ┌───────────────────────────┐
   │ 1 = Player vs Player      │
   ├───────────────────────────┤
   │ 2 = Player vs Bot         │
   ├───────────────────────────┤
   │ 3 = Player vs Hard Bot    │
   ├───────────────────────────┤
   │ X = Exit game             │
   ├───────────────────────────┤
   │ Pick your poison:         │
   └───────────────────────────┘


# Loss variations
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[1, 4, 7],
[2, 5, 8],
[3, 6, 9],
[1, 5, 9],
[3, 5, 7]

# One missing loss variations for bot.
1-2, 2-3, 1-3, 4-5, 5-6, 4-6, 7-8, 8-9, 7-9, 1-4, 4-7, 1-7, 2-5, 5-8, 2-8, 3-6, 6-9, 3-9, 1-5, 5-9, 1-9, 3-5, 5-7, 3-7

"""
# Game starts here!
# Imports,os, random, time: os to clear terminal, random for bot, time for delay in commands.
import os
import random as rand
import time
# X value 8 spaces, 4 rows
b1 = "  ╲  ╱  "
b2 = "   ╲╱   "
b3 = "   ╱╲   "
b4 = "  ╱  ╲  "

# O value 8 spaces, 4 rows
a1 = "╭──────╮"
a2 = "│      │"
a3 = "│      │"
a4 = "╰──────╯" 

# Loading menu variables

c1 ="┌───────────────────────────┐"
c2 ="│    Initializing game      │"
c3 ="└───────────────────────────┘"

d1 ="┌───────────────────────────┐"
d2 ="│    Loading variables      │"
d3 ="└───────────────────────────┘"
c4 = "█"

init_num = 1
init_num2 = 2
load_num = 1
load_num2 = 2

# Game menu variables
def game_menu():
   print("""
   ┌───────────────────────────┐
   │  A Game of Tic-Tac-Toe    │ 
   │───────────────────────────│
   │ 1 = Player vs Player      │
   ├───────────────────────────┤
   │ 2 = Player vs Bot         │
   ├───────────────────────────┤
   │ 3 = Player vs Sneaky Bot  │
   ├───────────────────────────┤
   │ X = Exit game             │
   ├───────────────────────────┤
   │                           │
   └───────────────────────────┘
                  """, end='\033[F\033[A   │ Pick your poison: ')

def fresh_grid():
   os.system("cls")
   print(f"{a}\n{b}\n{c}\n{d}\n{f}\n{g}\n{h}\n{i}\n{j}\n{k}\n{m}\n{n}\n{p}\n{q}\n{r}\n{s}")

# Class Box() to fill the grid based on answers
class Box():
   """
   Class Box(integer, string) takes 2 variables:
   integer with value 1-9 to choose a box from the grid
   string with value X or O to insert the value to choosen box
   
   """

   def __init__(self, box_num, player):
      self.player = player
      self.box_num = box_num
      if self.box_num == 1:
         self.box_1()
      if self.box_num == 2:
         self.box_2()
      if self.box_num == 3:
         self.box_3()
      if self.box_num == 4:
         self.box_4()
      if self.box_num == 5:
         self.box_5()
      if self.box_num == 6:
         self.box_6()
      if self.box_num == 7:
         self.box_7()
      if self.box_num == 8:
         self.box_8()
      if self.box_num == 9:
         self.box_9()

   # 1st box function to switch value to O or X
   def box_1(self):
      global b, c, d, f
      if self.player == "O":
         b = b[:2] + a1[0:8] + b[10:]
         c = c[:2] + a2[0:8] + c[10:]
         d = d[:2] + a3[0:8] + d[10:]
         f = f[:2] + a4[0:8] + f[10:]
      if self.player == "X":
         b = b[:2] + b1[0:8] + b[10:]
         c = c[:2] + b2[0:8] + c[10:]
         d = d[:2] + b3[0:8] + d[10:]
         f = f[:2] + b4[0:8] + f[10:]

   # 2nd box function to switch value to O or X
   def box_2(self):
      global b, c, d, f
      if self.player == "O":
         b = b[:13] + a1[:8] + b[21:]
         c = c[:13] + a2[:8] + c[21:]
         d = d[:13] + a3[:8] + d[21:]
         f = f[:13] + a4[:8] + f[21:]
      if self.player == "X":
         b = b[:13] + b1[:8] + b[21:]
         c = c[:13] + b2[:8] + c[21:]
         d = d[:13] + b3[:8] + d[21:]
         f = f[:13] + b4[:8] + f[21:]

   # 3rd box function to switch value to O or X
   def box_3(self):
      global b, c, d, f
      if self.player == "O":
         b = b[:24] + a1[:8] + b[32:]
         c = c[:24] + a2[:8] + c[32:]
         d = d[:24] + a3[:8] + d[32:]
         f = f[:24] + a4[:8] + f[32:]
      if self.player == "X":
         b = b[:24] + b1[:8] + b[32:]
         c = c[:24] + b2[:8] + c[32:]
         d = d[:24] + b3[:8] + d[32:]
         f = f[:24] + b4[:8] + f[32:]

   # 4th box function to switch value to O or X
   def box_4(self):
      global h, i, j, k
      if self.player == "O":
         h = h[:2] + a1[0:8] + h[10:]
         i = i[:2] + a2[0:8] + i[10:]
         j = j[:2] + a3[0:8] + j[10:]
         k = k[:2] + a4[0:8] + k[10:]
      if self.player == "X":
         h = h[:2] + b1[0:8] + h[10:]
         i = i[:2] + b2[0:8] + i[10:]
         j = j[:2] + b3[0:8] + j[10:]
         k = k[:2] + b4[0:8] + k[10:]

   # 5th box function to switch value to O or X
   def box_5(self):
      global h, i, j, k
      if self.player == "O":
         h = h[:13] + a1[:8] + h[21:]
         i = i[:13] + a2[:8] + i[21:]
         j = j[:13] + a3[:8] + j[21:]
         k = k[:13] + a4[:8] + k[21:]
      if self.player == "X":
         h = h[:13] + b1[:8] + h[21:]
         i = i[:13] + b2[:8] + i[21:]
         j = j[:13] + b3[:8] + j[21:]
         k = k[:13] + b4[:8] + k[21:]

   # 6th box function to switch value to O or X
   def box_6(self):
      global h, i, j, k
      if self.player == "O":
         h = h[:24] + a1[:8] + h[32:]
         i = i[:24] + a2[:8] + i[32:]
         j = j[:24] + a3[:8] + j[32:]
         k = k[:24] + a4[:8] + k[32:]
      if self.player == "X":
         h = h[:24] + b1[:8] + h[32:]
         i = i[:24] + b2[:8] + i[32:]
         j = j[:24] + b3[:8] + j[32:]
         k = k[:24] + b4[:8] + k[32:]

   # 7th box function to switch value to O or X
   def box_7(self):
      global n, p, q, r
      if self.player == "O":
         n = n[:2] + a1[0:8] + n[10:]
         p = p[:2] + a2[0:8] + p[10:]
         q = q[:2] + a3[0:8] + q[10:]
         r = r[:2] + a4[0:8] + r[10:]
      if self.player == "X":
         n = n[:2] + b1[0:8] + n[10:]
         p = p[:2] + b2[0:8] + p[10:]
         q = q[:2] + b3[0:8] + q[10:]
         r = r[:2] + b4[0:8] + r[10:]

   # 8th box function to switch value to O or X
   def box_8(self):
      global n, p, q, r
      if self.player == "O":
         n = n[:13] + a1[:8] + n[21:]
         p = p[:13] + a2[:8] + p[21:]
         q = q[:13] + a3[:8] + q[21:]
         r = r[:13] + a4[:8] + r[21:]
      if self.player == "X":
         n = n[:13] + b1[:8] + n[21:]
         p = p[:13] + b2[:8] + p[21:]
         q = q[:13] + b3[:8] + q[21:]
         r = r[:13] + b4[:8] + r[21:]

   # 9th box function to switch value to O or X
   def box_9(self):
      global n, p, q, r
      if self.player == "O":
         n = n[:24] + a1[:8] + n[32:]
         p = p[:24] + a2[:8] + p[32:]
         q = q[:24] + a3[:8] + q[32:]
         r = r[:24] + a4[:8] + r[32:]
      if self.player == "X":
         n = n[:24] + b1[:8] + n[32:]
         p = p[:24] + b2[:8] + p[32:]
         q = q[:24] + b3[:8] + q[32:]
         r = r[:24] + b4[:8] + r[32:]

for i in range(11):
   c2 = c2[:init_num]+c4+c2[init_num2:]
   init_num += 1
   init_num2 +=1
   time.sleep(0.05)
   os.system("cls")
   print(f"{c1}\n{c2}\n{c3}\n")
os.system("cls")

for i in range(27):
   d2 = d2[:load_num]+c4+d2[load_num2:]
   c2 = c2[:init_num]+c4+c2[init_num2:]
   load_num += 1
   load_num2 +=1
   if init_num <27:
      init_num += 1
   else:
      pass
   if init_num2 < 28:
      init_num2 += 1
   else:
      pass

   time.sleep(rand.uniform(0, 1)/5)
   os.system("cls")
   print(f"{c1}\n{c2}\n{c3}\n")
   print(f"{d1}\n{d2}\n{d3}\n")
time.sleep(1)
os.system("cls")
print("""
   ┌───────────────────────────┐
   │  A Game of Tic-Tac-Toe    │ 
   └───────────────────────────┘
""")
time.sleep(0.1)
os.system("cls")
print("""
   ┌───────────────────────────┐
   │  A Game of Tic-Tac-Toe    │ 
   │───────────────────────────│
   │ 1 = Player vs Player      │
   └───────────────────────────┘
""")
time.sleep(0.1)
os.system("cls")
print("""
   ┌───────────────────────────┐
   │  A Game of Tic-Tac-Toe    │ 
   │───────────────────────────│
   │ 1 = Player vs Player      │
   ├───────────────────────────┤
   │ 2 = Player vs Bot         │
   └───────────────────────────┘
""")
time.sleep(0.1)
os.system("cls")
print("""
   ┌───────────────────────────┐
   │  A Game of Tic-Tac-Toe    │ 
   │───────────────────────────│
   │ 1 = Player vs Player      │
   ├───────────────────────────┤
   │ 2 = Player vs Bot         │
   ├───────────────────────────┤
   │ 3 = Player vs Sneaky Bot  │
   └───────────────────────────┘
""")
time.sleep(0.1)
os.system("cls")
print("""
   ┌───────────────────────────┐
   │  A Game of Tic-Tac-Toe    │ 
   │───────────────────────────│
   │ 1 = Player vs Player      │
   ├───────────────────────────┤
   │ 2 = Player vs Bot         │
   ├───────────────────────────┤
   │ 3 = Player vs Sneaky Bot  │
   ├───────────────────────────┤
   │ X = Exit game             │
   └───────────────────────────┘
""")
time.sleep(0.1)
os.system("cls")

# Game loop
while True:
   # Coordinates grid
   a = "┌──────────┬──────────┬──────────┐"
   b = "│          │          │          │"
   c = "│          │          │          │"
   d = "│    1     │    2     │    3     │"
   f = "│          │          │          │"
   g = "├──────────┼──────────┼──────────┤"
   h = "│          │          │          │"
   i = "│          │          │          │"
   j = "│    4     │    5     │    6     │"
   k = "│          │          │          │"
   m = "├──────────┼──────────┼──────────┤"
   n = "│          │          │          │"
   p = "│          │          │          │"
   q = "│    7     │    8     │    9     │"
   r = "│          │          │          │"
   s = "└──────────┴──────────┴──────────┘"
   
   # Winning combinations
   winners = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],
              [1, 4, 7],
              [2, 5, 8],
              [3, 6, 9],
              [1, 5, 9],
              [3, 5, 7]]

   # Available numbers to pick
   game_mode_options = ["1", "2", "3", "X"] # Available game modes being checked
   hard_positions = [1, 2, 3, 4, 5, 6, 7, 8, 9] # Bot random choises list.
   positions = [1, 2, 3, 4, 5, 6, 7, 8, 9] # Available numbers to be picked by players/bot
   str_positions = ["1", "2", "3", "4", "5", "6", "7", "8", "9"] # Valid answers that code accepts
   # Player reserved numbers
   player_1 = [] # Positions gets filled into players lists and compared to winners list
   player_2 = [] # Positions gets filled into players lists and compared to winners list
   win_var = 0
   os.system("cls")
   game_menu()
   game_mode_var = input()
   if str(game_mode_var) not in game_mode_options:
      print("\n Please choose a correct game mode!")
      time.sleep(2)
      os.system("cls")
   elif str(game_mode_var) in game_mode_options:
      game_mode = str(game_mode_var)
      fresh_grid()
      # 2 player mode
      if game_mode == "1":

         while len(positions) > 0:
         # Player 1 picking
            if len(player_1) <= len(player_2):
               answer_str = input("Player 1 please choose a box to occupy: ")
               if answer_str not in str_positions:
                  print("Please enter valid numbers only!")
                  time.sleep(1)
                  fresh_grid()
               elif int(answer_str) in positions:
                  answer_int = int(answer_str)
                  positions.remove(answer_int)
                  player_1.append(answer_int)
                  Box(answer_int, "X")
                  fresh_grid()
               else:
                  print("Number has already been taken: ")
                  time.sleep(1)
                  fresh_grid()

            # Score keeper checking X players winning combinations vs score.
               set_x = set(player_1)
               for lists in winners:
                  value = set(lists)
                  if value.issubset(set_x):
                     win_var = 1
                     print("Player 1 has won!")
                     positions.clear()
                     print("Entering Game menu in: ")
                     time.sleep(1)
                     print("3")
                     time.sleep(1)
                     print("2")
                     time.sleep(1)
                     print("1")
                     time.sleep(1)

         # Player 2 picking
            elif len(player_1) > len(player_2):
               answer_str = input("Player 2 please choose a box to occupy: ")
               if answer_str not in str_positions:
                  print("Please enter valid numbers only!")
                  time.sleep(1)
                  fresh_grid()
               elif int(answer_str) in positions:
                  answer_int = int(answer_str)
                  positions.remove(answer_int)
                  player_2.append(answer_int)
                  Box(answer_int, "O")
                  fresh_grid()
               else:
                  print("Number has already been taken: ")
                  time.sleep(1)
                  fresh_grid()

            # Score keeper checking O players winning combinations vs score.
               set_o = set(player_2)
               for lists in winners:
                  value = set(lists)
                  if value.issubset(set_o):
                     win_var = 1
                     print("Player 2 has won!")
                     positions.clear()
                     print("Entering Game menu in: ")
                     time.sleep(1)
                     print("3")
                     time.sleep(1)
                     print("2")
                     time.sleep(1)
                     print("1")
                     time.sleep(1) 

         if len(positions) == 0 and len(player_1) + len(player_2) == 9 and win_var == 0:
            print("You have a DRAW\n Entering Game menu in: ")
            time.sleep(1)
            print("3")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("1")
            time.sleep(1)     
      # Player 1 vs  bot mode.
      elif game_mode == "2":

         while len(positions) > 0:
         # Player 1 picking
            if len(player_1) <= len(player_2):
               answer_str = input("Human, please choose a box to occupy: ")
               if answer_str not in str_positions:
                  print("Please enter valid numbers only!")
                  time.sleep(1)
                  fresh_grid()
               elif int(answer_str) in positions:
                  answer_int = int(answer_str)
                  positions.remove(answer_int)
                  player_1.append(answer_int)
                  Box(answer_int, "X")
                  fresh_grid()
               else:
                  print("Number has already been taken: ")
                  time.sleep(1)
                  fresh_grid()

            # Score keeper checking X players winning combinations vs score.
               set_x = set(player_1)
               for lists in winners:
                  value = set(lists)
                  if value.issubset(set_x):
                     win_var = 1
                     print("Human, u have won against the machines!\n")
                     positions.clear()
                     print("Entering Game menu in: ")
                     time.sleep(1)
                     print("3")
                     time.sleep(1)
                     print("2")
                     time.sleep(1)
                     print("1")
                     time.sleep(1)  

         # Bot picking
            elif len(player_1) > len(player_2):
               answer = rand.randint(1, 9)
               
               if answer in positions:
                  positions.remove(answer)
                  player_2.append(answer)
                  Box(answer, "O")
                  time.sleep(1)
                  print(f"Bot has picked {answer}.")
                  time.sleep(2)
                  fresh_grid()

            # Score keeper checking Bots winning combinations vs score.
               set_o = set(player_2)
               for lists in winners:
                  value = set(lists)
                  if value.issubset(set_o):
                     print("Matrix has won, time for the blue pill!")
                     win_var = 1
                     positions.clear()
                     print("Entering Game menu in: ")
                     time.sleep(1)
                     print("3")
                     time.sleep(1)
                     print("2")
                     time.sleep(1)
                     print("1")
                     time.sleep(1)
         if len(positions) == 0 and len(player_1) + len(player_2) == 9 and win_var == 0:
            print("You have a DRAW\n Entering Game menu in:")
            time.sleep(1)
            print("3")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("1")
            time.sleep(1)      
      # Player 1 vs stronger bot
      elif game_mode == "3":
         while len(positions) > 0:

         # Player 1 picking
            if len(player_1) <= len(player_2):
               answer_str = input("Human, please choose a box to occupy: ")
               if answer_str not in str_positions:
                  print("Please enter valid numbers only!")
                  time.sleep(1)
                  fresh_grid()
               elif int(answer_str) in positions:
                  answer_int = int(answer_str)
                  positions.remove(answer_int)
                  player_1.append(answer_int)
                  Box(answer_int, "X")
                  fresh_grid()
               else:
                  print("Number has already been taken: ")
                  time.sleep(1)
                  fresh_grid()

            # Score keeper checking X players winning combinations vs score.
               set_x = set(player_1)
               for lists in winners:
                  value = set(lists)
                  if value.issubset(set_x):
                     win_var = 1
                     print("Human, u have won against the machines!\n")
                     positions.clear()
                     print("Entering Game menu in: ")
                     time.sleep(1)
                     print("3")
                     time.sleep(1)
                     print("2")
                     time.sleep(1)
                     print("1")
                     time.sleep(1)  

         # Bot picking
            elif len(player_1) > len(player_2):
            # 8 positions left   
               if len(positions) == 8:
                  if 5 not in positions:
                     hard_answer = rand.choices(hard_positions, [100,  1, 100,  1,  1,  1, 100,  1, 100])
                  else:
                     hard_answer = rand.choices(hard_positions, [20, 1, 20, 1, 100, 1, 20, 1, 20])
            # 6 positions left
               elif len(positions) == 6:
                  # implemented counters: 5-1, 5-3, 5-7, 5-9, 1-3, 1-7, 3-9, 2-8, 4-6, 7-9
                  # available counters: 1-2, 2-3, 4-5, 5-6, 7-8, 8-9, 1-4, 4-7, 2-5, 5-8, 3-6, 6-9, 1-9, 3-7
                  if 5 and 1 in player_1:
                     hard_answer = rand.choices(hard_positions, [1, 1, 1, 1, 1, 1, 1, 1, 100])
                  elif 5 and 3 in player_1:
                     hard_answer = rand.choices(hard_positions, [1, 1, 1, 1, 1, 1, 100, 1, 1])
                  elif 5 and 7 in player_1:
                     hard_answer = rand.choices(hard_positions, [1, 1, 100, 1, 1, 1, 1, 1, 1])
                  elif 5 and 9 in player_1:
                     hard_answer = rand.choices(hard_positions, [100, 1, 1, 1, 1, 1, 1, 1, 1])
                  elif 1 and 3 in player_1:
                     hard_answer = rand.choices(hard_positions, [1, 100, 1, 1, 1, 1, 1, 1, 1])
                  elif 1 and 7 in player_1:
                     hard_answer = rand.choices(hard_positions, [1, 1, 1, 100, 1, 1, 1, 1, 1])
                  elif 3 and 9 in player_1:
                     hard_answer = rand.choices(hard_positions, [1, 1, 1, 1, 1, 100, 1, 1, 1])
                  elif 2 and 8 in player_1:
                     hard_answer = rand.choices(hard_positions, [1, 1, 1, 1, 100, 1, 1, 1, 1])
                  elif 4 and 6 in player_1:
                     hard_answer = rand.choices(hard_positions, [1, 1, 1, 1, 100, 1, 1, 1, 1])
                  elif 7 and 9 in player_1:
                     hard_answer = rand.choices(hard_positions, [1, 1, 1, 1, 1, 1, 1, 100, 1])
            # 4 positions left
               elif len(positions) == 4:
                  hard_answer = rand.choices(hard_positions, [ 5, 10,  5, 10,  0, 10,  5, 10,  5])
            # 2 positions left
               elif len(positions) == 2:
                  hard_answer = rand.choices(hard_positions, [ 5,  5,  5,  5,  5,  5,  5,  5,  5])
            # Bot answer
               answer = hard_answer[0]
               if answer in positions:
                  positions.remove(answer)
                  player_2.append(answer)
                  Box(answer, "O")
                  time.sleep(1)
                  print(f"Bot has picked {answer}.")
                  time.sleep(2)
                  fresh_grid()
                  
            # Score keeper checking Bots winning combinations vs score.
               set_o = set(player_2)
               for lists in winners:
                  value = set(lists)
                  if value.issubset(set_o):
                     print("It's alright to pick flowers instead of playing this hard game!")
                     win_var = 1
                     positions.clear()
                     print("Entering Game menu in: ")
                     time.sleep(1)
                     print("3")
                     time.sleep(1)
                     print("2")
                     time.sleep(1)
                     print("1")
                     time.sleep(1)
         if len(positions) == 0 and len(player_1) + len(player_2) == 9 and win_var == 0:
            print("You have a DRAW\n Entering Game menu in:")
            time.sleep(1)
            print("3")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("1")
            time.sleep(1)  
      # Loop exit code
      elif game_mode == "X":
         os.system("cls")
         print("Thanks for trying out the game!")
         time.sleep(3)
         os.system("cls")
         print("Unloading variables...")
         time.sleep(1)
         os.system("cls")
         print("Unloading variables..")
         time.sleep(1)
         os.system("cls")
         print("Unloading variables.")
         time.sleep(1)
         os.system("cls")
         print("Closing the game...")
         time.sleep(1)
         os.system("cls")
         print("Closing the game..")
         time.sleep(1)
         os.system("cls")
         print("Closing the game.")
         time.sleep(1)
         os.system("cls")
         break
