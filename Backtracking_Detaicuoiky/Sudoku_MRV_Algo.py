def is_valid(board, row, col, num):
    # Kiểm tra hàng
    for x in range(9):
        if board[row][x] == num:
            return False
    # Kiểm tra cột
    for x in range(9):
        if board[x][col] == num:
            return False
    # Kiểm tra ô 3x3
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def find_MRV(board):
    min_possibilities = 10  # Số lượng khả năng nhỏ nhất (tối đa là 9)
    best_cell = None

    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:  # Nếu ô trống
                possibilities = 0
                for num in range(1, 10):  # Đếm số lượng số hợp lệ có thể điền
                    if is_valid(board, i, j, num):
                        possibilities += 1
                if possibilities < min_possibilities:
                    min_possibilities = possibilities
                    best_cell = (i, j)

    return best_cell  # Trả về ô có ít khả năng nhất hoặc None nếu không còn ô trống

def solve_sudoku(board):
    empty = find_MRV(board)
    if not empty:
        return True  # Không còn ô trống, đã giải xong

    row, col = empty

    for num in range(1, 10):  # Thử từ 1 đến 9
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0  # Backtrack

    return False  # Không có số nào hợp lệ

# ví dụ về bảng sudoku
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(sudoku_board):
    for row in sudoku_board:
        print(row)
else:
    print("Không tìm thấy lời giải cho Sudoku này.")
