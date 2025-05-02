import copy

def is_valid(board, row, col, num):
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

# Khởi tạo domain cho toàn bộ board
def init_domains(board):
    domains = [[set() for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                domains[i][j] = set(n for n in range(1, 10) if is_valid(board, i, j, n))
    return domains

# Cập nhật domain sau khi gán giá trị
def forward_check(board, domains, row, col, num):
    updated = []  # Lưu các domain đã bị thay đổi để có thể phục hồi khi backtrack

    for k in range(9):
        # Cột
        if board[k][col] == 0 and num in domains[k][col]:
            domains[k][col].remove(num)
            updated.append((k, col, num))
            if len(domains[k][col]) == 0:
                return False, updated

        # Hàng
        if board[row][k] == 0 and num in domains[row][k]:
            domains[row][k].remove(num)
            updated.append((row, k, num))
            if len(domains[row][k]) == 0:
                return False, updated

    # Khối 3x3
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            r, c = start_row + i, start_col + j
            if board[r][c] == 0 and num in domains[r][c]:
                domains[r][c].remove(num)
                updated.append((r, c, num))
                if len(domains[r][c]) == 0:
                    return False, updated

    return True, updated

# Backtrack solver với Forward Checking
def solve_forward_checking(board, domains):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in domains[i][j].copy():
                    if is_valid(board, i, j, num):
                        board[i][j] = num
                        backup_domains = copy.deepcopy(domains)  # Lưu lại domains trước khi cập nhật
                        success, updated = forward_check(board, domains, i, j, num)

                        if success and solve_forward_checking(board, domains):
                            return True

                        # Backtrack
                        board[i][j] = 0
                        domains = backup_domains

                return False  # Không có số nào phù hợp
    return True  # Đã điền hết ô

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

domains = init_domains(sudoku_board)
if solve_forward_checking(sudoku_board, domains):
    for row in sudoku_board:
        print(row)
else:
    print("Không tìm thấy lời giải cho Sudoku này.")
