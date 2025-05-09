
import tkinter as tk
from tkinter import messagebox
import time
import os
import psutil
import copy

# ------------------ TẢI MA TRẬN ------------------ #
def load_board(filepath):
    with open(filepath, "r") as f:
        return [[int(ch) for ch in line.strip()] for line in f.readlines()]

puzzle_levels = {
    "easy.txt": load_board("easy.txt"),
    "medium.txt": load_board("medium.txt"),
    "hard.txt": load_board("hard.txt"),
    "expert.txt": load_board("expert.txt")
}

# ------------------ BACKTRACKING CƠ BẢN ------------------ #
def is_valid_basic(board, row, col, num):
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False
    sr, sc = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[sr + i][sc + j] == num:
                return False
    return True

def solve_basic(board, counter):
    def find_empty():
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return i, j
        return None

    def backtrack():
        empty = find_empty()
        if not empty:
            return True
        row, col = empty
        for num in range(1, 10):
            if is_valid_basic(board, row, col, num):
                board[row][col] = num
                if backtrack():
                    return True
                board[row][col] = 0
                counter[0] += 1
        return False

    return backtrack()

# ------------------ BITMASKING ------------------ #
def get_box_index(row, col):
    return (row // 3) * 3 + (col // 3)

def is_available(mask, num):
    return not (mask >> (num - 1)) & 1

def set_bit(mask, num):
    return mask | (1 << (num - 1))

def clear_bit(mask, num):
    return mask ^ (1 << (num - 1))

def solve_bitmasking(board, counter):
    row_mask = [0] * 9
    col_mask = [0] * 9
    box_mask = [0] * 9
    empty_cells = []

    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num != 0:
                bit = 1 << (num - 1)
                row_mask[i] |= bit
                col_mask[j] |= bit
                box_mask[get_box_index(i, j)] |= bit
            else:
                empty_cells.append((i, j))

    def backtrack(index):
        if index == len(empty_cells):
            return True
        i, j = empty_cells[index]
        box = get_box_index(i, j)
        for num in range(1, 10):
            if is_available(row_mask[i], num) and is_available(col_mask[j], num) and is_available(box_mask[box], num):
                board[i][j] = num
                row_mask[i] = set_bit(row_mask[i], num)
                col_mask[j] = set_bit(col_mask[j], num)
                box_mask[box] = set_bit(box_mask[box], num)
                if backtrack(index + 1):
                    return True
                board[i][j] = 0
                row_mask[i] = clear_bit(row_mask[i], num)
                col_mask[j] = clear_bit(col_mask[j], num)
                box_mask[box] = clear_bit(box_mask[box], num)
                counter[0] += 1
        return False

    return backtrack(0)

# ------------------ FORWARD CHECKING ------------------ #
def is_valid_fc(board, row, col, num):
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False
    sr, sc = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[sr + i][sc + j] == num:
                return False
    return True

def init_domains(board):
    domains = [[set() for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                domains[i][j] = set(n for n in range(1, 10) if is_valid_fc(board, i, j, n))
    return domains

def forward_check(board, domains, row, col, num):
    updated = []
    for k in range(9):
        if board[k][col] == 0 and num in domains[k][col]:
            domains[k][col].remove(num)
            updated.append((k, col, num))
            if not domains[k][col]:
                return False, updated
        if board[row][k] == 0 and num in domains[row][k]:
            domains[row][k].remove(num)
            updated.append((row, k, num))
            if not domains[row][k]:
                return False, updated
    sr, sc = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            r, c = sr + i, sc + j
            if board[r][c] == 0 and num in domains[r][c]:
                domains[r][c].remove(num)
                updated.append((r, c, num))
                if not domains[r][c]:
                    return False, updated
    return True, updated

def solve_forward_checking(board, counter):
    domains = init_domains(board)
    def backtrack():
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    for num in domains[i][j].copy():
                        if is_valid_fc(board, i, j, num):
                            board[i][j] = num
                            success, updated = forward_check(board, domains, i, j, num)
                            if success and backtrack():
                                return True
                            board[i][j] = 0
                            for r, c, val in updated:
                                domains[r][c].add(val)
                            counter[0] += 1
                    return False
        return True
    return backtrack()

# ------------------ MRV ------------------ #
def is_valid_mrv(board, row, col, num):
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False
    sr, sc = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[sr + i][sc + j] == num:
                return False
    return True

def find_MRV(board):
    best_cell = None
    min_options = 10
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                count = sum(1 for n in range(1, 10) if is_valid_mrv(board, i, j, n))
                if count < min_options:
                    min_options = count
                    best_cell = (i, j)
    return best_cell

def solve_mrv(board, counter):
    empty = find_MRV(board)
    if not empty:
        return True
    row, col = empty
    for num in range(1, 10):
        if is_valid_mrv(board, row, col, num):
            board[row][col] = num
            if solve_mrv(board, counter):
                return True
            board[row][col] = 0
            counter[0] += 1
    return False

# ------------------ GIAO DIỆN ------------------ #
def show_solution_gui(solutions, algo_name):
    gui = tk.Toplevel()
    gui.title(f"Kết quả - {algo_name}")
    left = tk.Frame(gui)
    left.pack(side=tk.LEFT, padx=10, pady=10)
    right = tk.Frame(gui)
    right.pack(side=tk.RIGHT, padx=10)

    tk.Label(left, text=f"Kết quả giải bằng {algo_name}", font=("Arial", 14, "bold")).pack()

    for name, _, _, time_used, mem_used, bt_count in solutions:
        tk.Label(left, text=f"Mức độ: {name}\nThời gian: {time_used:.4f}s\nBộ nhớ: {mem_used:.6f}MB\nBacktrack: {bt_count}\n", justify='left', anchor="w").pack(anchor='w')

    for idx, (level, original, solved, *_ ) in enumerate(solutions):
        frame = tk.LabelFrame(right, text=level, padx=2, pady=2)
        frame.grid(row=idx//2, column=idx%2, padx=5, pady=5)
        for i in range(9):
            for j in range(9):
                val = solved[i][j]
                bg = "#b6fcb6" if original[i][j] == 0 else "#ffffff"
                e = tk.Label(frame, text=str(val), width=2, height=1, font=("Consolas", 10), relief="solid", bg=bg)
                e.grid(row=i, column=j)

def run_and_display(solver_func, algo_name):
    solutions = []
    for name, puzzle in puzzle_levels.items():
        original = copy.deepcopy(puzzle)
        board = copy.deepcopy(puzzle)
        counter = [0]
        start_mem = psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024
        start_time = time.perf_counter()
        solver_func(board, counter)
        end_time = time.perf_counter()
        end_mem = psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024
        solutions.append((name, original, board, end_time - start_time, end_mem - start_mem, counter[0]))
    show_solution_gui(solutions, algo_name)

root = tk.Tk()
root.title("Sudoku - Trình giải đa thuật toán")

frame = tk.Frame(root)
frame.pack(pady=20)

tk.Label(frame, text="Chọn thuật toán để giải toàn bộ mức độ Sudoku", font=("Arial", 14)).pack(pady=10)

tk.Button(frame, text="Thuật toán Backtrack cơ bản", width=50, height=2,
          command=lambda: run_and_display(solve_basic, "Backtracking cơ bản")).pack(pady=5)

tk.Button(frame, text="Thuật toán Bitmasking", width=50, height=2,
          command=lambda: run_and_display(solve_bitmasking, "Bitmasking")).pack(pady=5)

tk.Button(frame, text="Thuật toán ForwardChecking", width=50, height=2,
          command=lambda: run_and_display(solve_forward_checking, "Forward Checking")).pack(pady=5)

tk.Button(frame, text="Thuật toán Minimum Remaining Values - Heuristic", width=50, height=2,
          command=lambda: run_and_display(solve_mrv, "MRV")).pack(pady=5)

root.mainloop()