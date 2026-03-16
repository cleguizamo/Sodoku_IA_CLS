import time
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from boards.board_Easy import board_easy
from boards.board_Hard import board_hard
from boards.board_Medium import board_medium
from boards.board_NoSolution import board_no_solution
from boards.board import print_board, find_empty, is_valid
from src.forward_checking import forward_checking


print("PRUEBAS DE FORWARD CHECKING:")

print ("Tablero Fácil:")
print_board(board_easy)
start_time = time.time()
if forward_checking(board_easy):
    print("Solución encontrada con Forward Checking:")
    print_board(board_easy)
else:
    print("No se encontró solución con Forward Checking.")
print(f"Tiempo de ejecución: {time.time() - start_time:.4f} segundos\n")


print ("Tablero Medio:")
print_board(board_medium)
start_time = time.time()
if forward_checking(board_medium):
    print("Solución encontrada con Forward Checking:")
    print_board(board_medium)
else:
    print("No se encontró solución con Forward Checking.")
print(f"Tiempo de ejecución: {time.time() - start_time:.4f} segundos\n")


print ("Tablero Difícil:")
print_board(board_hard)
start_time = time.time()
if forward_checking(board_hard):
    print("Solución encontrada con Forward Checking:")
    print_board(board_hard)
else:
    print("No se encontró solución con Forward Checking.")
print(f"Tiempo de ejecución: {time.time() - start_time:.4f} segundos\n")

print ("Tablero Sin Solución:")
print_board(board_no_solution)
start_time = time.time()
if forward_checking(board_no_solution):
    print("Solución encontrada con Forward Checking:")
    print_board(board_no_solution)
else:
    print("No se encontró solución con Forward Checking.")
print(f"Tiempo de ejecución: {time.time() - start_time:.4f} segundos\n") 