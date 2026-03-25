# The line below will only work if you have cloned the ox repository as described above,
# and the ox folder is a subfolder of the folder containing this notebook.
# You should not attempt to install ox using pip.  That will get you a completely 
# unrelated package that happens to have the same name.
import ox

pq, winner, moves = ox.play_game(ox.random_move, ox.random_move, return_moves=True)
print('Draw' if winner is None else 'Player ' + ['O', 'X'][winner] + ' wins')
print(moves)
ox.show_board_ascii(pq, winner)
ox.show_board(pq, winner)

pq, winner = ox.play_game(ox.random_move, ox.suggest_move)
print('Draw' if winner is None else 'Player ' + ['O', 'X'][winner] + ' wins')
ox.show_board(pq, winner)

pq, winner = ox.play_game(ox.input_move, ox.random_move)
print('Draw' if winner is None else 'Player ' + ['O', 'X'][winner] + ' wins')
ox.show_board(pq, winner)
