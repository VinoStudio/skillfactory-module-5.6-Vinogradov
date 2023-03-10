import random
from random import *
print('*' * 15, 'Добро пожаловать в игру "Крестики-нолики!', '*' * 15, sep='')
print()
print('-' * 15, 'Вашим оппонентом выступит компьютер. Приготовьтесь!', '-' * 15, '\n', sep='')
board = list(i for i in range(1,10))
player1 = None
player2 = None
ii = None
while True:
   player1 = input('Выберете за какую сторону вы хотите играть: X или O? \n')
   if any([player1 == 'X', player1 == 'x', player1 == 'х', player1 == 'O', player1 == 'o', player1 == 'о']):
      player1 = player1.upper()
      player1 = player1.replace(' ', '')
      player1 = player1.replace('\n', '')
      if player1 == 'X' or player1 == 'Х':
         player2 = 'O'
         break
      elif player1 == 'O' or player1 == 'О':
         player2 = 'X'
         break
   else:
      print('Пожалуйста, введите соответствующий символ игрока')
      continue



def game_board(board):
   print("-" * 13)
   for i in range(3):
      print("|-", board[0+i*3], "-|-", board[1+i*3], "-|-", board[2+i*3], "-|", sep='')
      print("-" * 13)



def game_input():
   while True:
      player_input = input(f'Первый игрок, выберете число куда желаете поставить ваш символ: {player1}?\n')
      try:
         player_input = int(player_input)
      except ValueError:
         print('Ошибка. Убедитесь, что вы ввели число')
         continue
      if 1 <= player_input <= 9 and type(board[player_input-1]) != str:
         board[player_input-1] = player1
         break
      elif player_input > 9 or player_input < 1:
         print('Вы вышли за рамки :)')
      else:
         print('Клетка уже занята!')
   while True:
      ii = choice(board)
      if type(ii) == str and any(isinstance(x, int) for x in board):
         continue
      if type(ii) == int and 1 <= ii <= 9:
         board[ii-1] = player2
         print('Компьютер сделал свой ход!')
         break
      else:
         break

def check_win(board):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for i in win_coord:
       if board[i[0]] == board[i[1]] == board[i[2]]:
          return board[i[0]]
   return False


def game(board):
   counter = 0
   win = False
   print('Ваше поле для сражений: ')
   while not win:
      game_board(board)
      if counter % 2 == 0:
         game_input()
         counter += 2
      if counter > 4:
         victory = check_win(board)
         if victory:
            if victory == player1:
               print('*' * 25)
               print('Поздравляю! Вы победили!')
               win = True
               break
            elif victory == player2:
               print('*' * 25)
               print('Компьютер победил!')
               win = True
               break
      if counter >= 9:
         print("Ничья!")
         break
   game_board(board)


game(board)
