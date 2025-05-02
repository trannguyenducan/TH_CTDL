
"""
SudokuApp_with_backtrack.py

Ứng dụng Sudoku sử dụng thuật toán backtracking.
Tính năng:
- Giao diện nhập Sudoku với Tkinter
- Giải Sudoku bằng đệ quy + đếm số lần backtrack
- Hiển thị thời gian thực thi và bộ nhớ sử dụng
- Tô màu ô được giải
- Nút xóa bảng để làm mới
"""
import tkinter as tk
from tkinter import messagebox
from copy import deepcopy
import time
from memory_profiler import memory_usage

# ------------------ GIẢI THUẬT SUDOKU ------------------

def is_valid(board, row, col, num):
    """Kiểm tra số 'num' có thể đặt vào ô (row, col) không"""
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False
    sr, sc = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[sr + i][sc + j] == num:
                return False
    return True

def find_empty(board):
    """Tìm ô trống đầu tiên trên bảng, trả về (row, col) hoặc None nếu đầy"""
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def solve_sudoku_with_count(board, gui):
    """Giải Sudoku bằng backtracking, đồng thời đếm số lần backtrack"""
    def backtrack():
        empty = find_empty(board)
        if not empty:
            return True
        row, col = empty
        for num in range(1, 10):
            if is_valid(board, row, col, num):
                board[row][col] = num
                if backtrack():
                    return True
                board[row][col] = 0
                gui.backtrack_count += 1  # Tăng khi quay lui
        return False
    return backtrack()

def measure_runtime_and_memory(solve_func, board):
    """Đo thời gian và bộ nhớ sử dụng để chạy hàm giải Sudoku"""
    def target():
        return solve_func()
    start = time.time()
    mem_usage = memory_usage(target, interval=0.01, timeout=None)
    end = time.time()
    duration = end - start
    peak_memory = max(mem_usage) - min(mem_usage)
    return duration, peak_memory

# ------------------ GIAO DIỆN NGƯỜI DÙNG ------------------

class SudokuGUI:
    def __init__(self, root):
        """Khởi tạo giao diện và trạng thái ban đầu"""
        self.root = root
        self.root.title("Sudoku")
        self.selected_cell = None
        self.cells = [[None for _ in range(9)] for _ in range(9)]
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.backtrack_count = 0

        self.create_grid()
        self.create_buttons()
        self.root.bind("<Key>", self.key_input)

    def create_grid(self):
        """Tạo lưới 9x9 ô Sudoku với màu xen kẽ khối 3x3"""
        frame = tk.Frame(self.root)
        frame.pack(pady=10)
        for i in range(9):
            for j in range(9):
                bg_color = "#f0f0f0" if (i // 3 + j // 3) % 2 == 0 else "#d0e0ff"
                cell = tk.Label(frame, text="", width=4, height=2, font=("Arial", 16),
                                borderwidth=1, relief="solid", bg=bg_color)
                cell.grid(row=i, column=j, padx=(2 if j % 3 == 0 else 1), pady=(2 if i % 3 == 0 else 1))
                cell.bind("<Button-1>", lambda e, row=i, col=j: self.select_cell(row, col))
                self.cells[i][j] = cell

    def select_cell(self, row, col):
        """Chọn một ô để nhập số"""
        if self.selected_cell:
            r, c = self.selected_cell
            self.cells[r][c].config(highlightthickness=0)
        self.selected_cell = (row, col)
        self.cells[row][col].config(highlightbackground="red", highlightthickness=2)

    def key_input(self, event):
        """Nhập hoặc xóa số bằng bàn phím"""
        if self.selected_cell and event.char in '123456789':
            row, col = self.selected_cell
            num = int(event.char)
            self.cells[row][col]['text'] = str(num)
            self.board[row][col] = num
        elif self.selected_cell and event.keysym in ('BackSpace', 'Delete'):
            row, col = self.selected_cell
            self.cells[row][col]['text'] = ""
            self.board[row][col] = 0

    def create_buttons(self):
        """Tạo các nút chức năng: Giải và Xóa bảng"""
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        solve_btn = tk.Button(btn_frame, text="Giải", width=12, height=2, bg="lightgreen",
                              font=("Arial", 14), command=self.solve_sudoku)
        solve_btn.grid(row=0, column=0, padx=10)

        clear_btn = tk.Button(btn_frame, text="Xóa bảng", width=12, height=2, bg="lightcoral",
                              font=("Arial", 14), command=self.clear_board)
        clear_btn.grid(row=0, column=1, padx=10)

    def solve_sudoku(self):
        """Gọi giải Sudoku, đo hiệu suất, tô màu và hiển thị kết quả"""
        board_copy = deepcopy(self.board)
        original_board = deepcopy(self.board)
        self.backtrack_count = 0

        def run_solver():
            return solve_sudoku_with_count(board_copy, self)

        duration, peak_memory = measure_runtime_and_memory(run_solver, board_copy)

        if solve_sudoku_with_count(board_copy, self):
            self.update_board_with_highlight(board_copy, original_board)
            messagebox.showinfo("Thành công",
                f"✅ Đã giải xong Sudoku!"
                f"\nThời gian thực thi: {duration:.4f} giây"
                f"\nBộ nhớ sử dụng: {peak_memory:.4f} MB"
                f"\n🔁 Số lần backtrack: {self.backtrack_count}"
            )
        else:
            messagebox.showerror("Thất bại", "❌ Lỗi! Không thể giải Sudoku.")

    def update_board_with_highlight(self, solved_board, original_board):
        """Cập nhật ô đã giải và tô xanh lá cây các ô mới được điền"""
        for i in range(9):
            for j in range(9):
                self.board[i][j] = solved_board[i][j]
                self.cells[i][j]['text'] = str(solved_board[i][j])
                if original_board[i][j] == 0:
                    self.cells[i][j]['bg'] = "#b6fcb6"
                else:
                    self.cells[i][j]['bg'] = "#f0f0f0" if (i // 3 + j // 3) % 2 == 0 else "#d0e0ff"

    def clear_board(self):
        """Xóa bảng hiện tại để nhập mới"""
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                self.cells[i][j]['text'] = ""
                self.cells[i][j]['highlightthickness'] = 0
                self.cells[i][j]['bg'] = "#f0f0f0" if (i // 3 + j // 3) % 2 == 0 else "#d0e0ff"

# ------------------ CHẠY ỨNG DỤNG ------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuGUI(root)
    root.mainloop()