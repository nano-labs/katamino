from datetime import datetime
from itertools import combinations
import json
from tqdm import tqdm
import sys

style = """
<style>
    table {
        # border: 5px solid #000000;
        border: none;
        border-collapse: collapse;
    }
    td {
        width: 40px;
        height: 47px;
        text-align: center;
    }
    .block-1 {
        background-color: #4A7BBA;
    }
    .block-2 {
        background-color: #C174A8;
    }
    .block-3 {
        background-color: #4DAFD0;
    }
    .block-4 {
        background-color: #87BD56;
    }
    .block-5 {
        background-color: #353289;
    }
    .block-6 {
        background-color: #459FD7;
    }
    .block-7 {
        background-color: #FCE84E;
    }
    .block-8 {
        background-color: #4A4A59;
    }
    .block-9 {
        background-color: #D93841;
    }
    .block-10 {
        background-color: #E37C3A;
    }
    .block-11 {
        background-color: #6A3C27;
    }
    .block-12 {
        background-color: #79848B;
    }
    .border-top {
        border-top: 5px solid #000000;
    }
    .border-bottom {
        border-bottom: 5px solid #000000;
    }
    .border-left {
        border-left: 5px solid #000000;
    }
    .border-right {
        border-right: 5px solid #000000;
    }
    .block-y {
        border-bottom: 1px dashed #AAAAAA;
    }
    .block-x {
        border-left: 1px dashed #AAAAAA;
    }
</style>
"""


class Puzzle:

    def __init__(self, bar_at=12, pieces_set=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]):
        self.pieces_set = pieces_set
        self.pieces = (
            [],
            # Blue
            [
                [1, 1, 1, 1, 1],
            ],
            # pink
            [
                [2, 2],
                [2, 2],
                [0, 2],
            ],
            # # turcoise
            [
                [3, 3, 0],
                [0, 3, 0],
                [0, 3, 3],
            ],
            # light green
            [
                [4, 0, 0],
                [4, 4, 0],
                [0, 4, 4],
            ],
            # purple
            [
                [5, 5, 0, 0],
                [0, 5, 5, 5],
            ],
            # light blue
            [
                [6, 0, 0],
                [6, 0, 0],
                [6, 6, 6],
            ],
            # yellow
            [
                [7, 0, 7],
                [7, 7, 7],
            ],
            # green
            [
                [0, 8, 0],
                [0, 8, 0],
                [8, 8, 8],
            ],
            # red
            [
                [0, 9, 0],
                [9, 9, 9],
                [0, 9, 0],
            ],
            # orange
            [
                [10, 10],
                [0, 10],
                [0, 10],
                [0, 10],
            ],
            # Brown
            [
                [0, 11],
                [11, 11],
                [0, 11],
                [0, 11],
            ],
            # light pink
            [
                [0, 12, 12],
                [12, 12, 0],
                [0, 12, 0],
            ],
        )
        self.pieces = [[]] + list([self.pieces[p] for p in self.pieces_set])
        self.bar_at = bar_at
        self.board = [
            [0] * self.bar_at,
            [0] * self.bar_at,
            [0] * self.bar_at,
            [0] * self.bar_at,
            [0] * self.bar_at,
        ]
        self.piece_positions = self.get_all_positions()
        self.iterations = 0
        self.solutions = []
        self.start = datetime.now()
        self.output_file = f"katamino_{self.bar_at}.html"
        self.solutions_file = f"solutions_{self.bar_at}.json"
        self.iterations_file = f"iterations_{self.bar_at}.json"

    def rotate(self, piece):
        return [list(row[::-1]) for row in zip(*piece)]

    def get_rotations(self, piece):
        unique_rotations = [piece]
        for _ in range(3):
            piece = self.rotate(piece)
            if piece not in unique_rotations:
                unique_rotations.append(piece)

        return unique_rotations, len(unique_rotations)

    def mirror_x(self, piece):
        return piece[::-1]

    def mirror_y(self, piece):
        return [row[::-1] for row in piece]

    def get_positions(self, piece):
        positions, _ = self.get_rotations(piece)
        for pos in positions:
            y_reflect = self.mirror_y(pos)
            x_reflect = self.mirror_x(pos)
            if y_reflect not in positions:
                positions.append(y_reflect)
            if x_reflect not in positions:
                positions.append(x_reflect)
        return positions

    def get_all_positions(self):
        piece_positions = []
        for piece in self.pieces[1:]:
            piece_positions.append(self.get_positions(piece))
        return piece_positions

    def islands(self, board):
        board = [[elem for elem in row] for row in board]
        board_height = len(board)
        board_width = len(board[0])
        island_cells = []

        def island(row, col):
            cell_queue = [(row, col)]

            while cell_queue:
                row, col = cell_queue.pop()
                if board[row][col] != 0:
                    continue
                island_cells.append((row, col))
                board[row][col] = "#"
                for row_offset, col_offset in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    temp_row = row + row_offset
                    temp_col = col + col_offset
                    if (
                        0 <= temp_row < board_height
                        and 0 <= temp_col < board_width
                        and board[temp_row][temp_col] == 0
                    ):
                        cell_queue.append((temp_row, temp_col))

        for row in range(board_height):
            for col in range(board_width):
                if board[row][col] == 0:
                    island(row, col)
                    island_size = len(island_cells)

                    if island_size % 5 != 0:
                        return False

                    island_cells = []
        return True

    def add_piece(self, board, piece, start_row, start_col):
        piece_width = len(piece[0])
        piece_height = len(piece)
        legal_move = True
        if (start_row + piece_height > len(board)) or (
            start_col + piece_width > len(board[0])
        ):
            legal_move = False
            return board, legal_move

        changed_squares = []
        for i, row in enumerate(piece):
            for j, val in enumerate(row):
                if val:
                    if board[start_row + i][start_col + j]:
                        legal_move = False
                        return board, legal_move
                    else:
                        changed_squares.append((start_row + i, start_col + j, val))

        new_board = [[val for val in row] for row in board]
        for changed_row, changed_col, val in changed_squares:
            new_board[changed_row][changed_col] = val

        if not self.islands(new_board):
            legal_move = False
            return board, legal_move

        return new_board, legal_move

    def get_legal_squares(self, board, piece):
        legal_moves = []
        for row in range(len(board)):
            for col in range(len(board[0])):
                _, legal_move = self.add_piece(board, piece, row, col)
                if legal_move:
                    legal_moves.append((row, col))
        return legal_moves

    def draw_solution(self, board, solution="", iteration=""):
        with open(self.output_file, "a") as sol:
            sol.write(f"Bar position: {self.bar_at}<br>\n")
            sol.write(f"Pieces: {self.pieces_set}<br>\n")
            sol.write(f"Solution: {solution}<br>\n")
            sol.write(f"Iterations: {iteration}<br>\n")
            sol.write(f"Compute time: {datetime.now() - self.start}")
        self.draw(board)

    def draw(self, board):
        with open(self.output_file, "a") as sol:
            sol.write("<table>\n")
            for y, row in enumerate(board):
                sol.write(f'<tr><td class="block-y">{y+1}</td>')
                for x, col in enumerate(row):
                    border_classes = ""
                    if not board[y][x] == 0:
                        if x > 0 and board[y][x - 1] != col or x == 0:
                            border_classes += " border-left"
                        if (
                            x < len(board[y]) - 1
                            and board[y][x + 1] != col
                            or x == len(board[y]) - 1
                        ):
                            border_classes += " border-right"
                        if y > 0 and board[y - 1][x] != col or y == 0:
                            border_classes += " border-top"
                        if (
                            y < len(board) - 1
                            and board[y + 1][x] != col
                            or y == len(board) - 1
                        ):
                            border_classes += " border-bottom"
                    sol.write(f'<td class="block-{col} {border_classes}"></td>')
                sol.write("</tr>\n")
            sol.write("<tr><td></td>")
            for x in range(len(board[0])):
                sol.write(f'<td class="block-x">{x + 1}</td>')
            sol.write("</td>")
            sol.write("</table>\n<hr>")

    def solve(self, board, pieces):

        self.iterations += 1
        if self.iterations % 10000 == 0:
            print(self.bar_at, self.pieces_set, self.iterations)

        if all([all(row) for row in board]):
            self.solutions.append(board)
            with open(self.solutions_file, "a") as sf:
                sf.write(f"{json.dumps(board)}\n")
            self.draw_solution(board, len(self.solutions), self.iterations)
            return board
        else:
            piece_positions = pieces[0]
            for position in piece_positions:
                legal_squares = self.get_legal_squares(board, position)
                for row, col in legal_squares:
                    self.solve(self.add_piece(board, position, row, col)[0], pieces[1:])

    def run(self):
        # print(f"Starting puzzle with bar at {self.bar_at}")

        # for p in self.pieces[1:]:
        #     self.draw(p)

        # for p in self.piece_positions:
        #     for b in p:
        #         self.draw_solution(b)

        self.solve(self.board, self.piece_positions)
        with open(self.iterations_file, "a") as itf:
            out = {
                "pieces_set": self.pieces_set,
                "iterations": self.iterations,
                "solutions": len(self.solutions),
                "bar_at": self.bar_at,
            }
            itf.write(f"{json.dumps(out, sort_keys=True)}\n")


if __name__ == "__main__":
    all_pieces = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    # for b in tqdm([3, 4, 5, 6, 7, 8, 9, 10, 11, 12]):
    b = int(sys.argv[1])
    print(f"Board: {b}")
    with open(f"katamino_{b}.html", "w") as sol:
        sol.write(style)
    for subset in tqdm(list(combinations(all_pieces, b))):
        Puzzle(bar_at=b, pieces_set=subset).run()
