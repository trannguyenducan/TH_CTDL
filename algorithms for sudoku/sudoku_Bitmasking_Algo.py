def get_box_index(row, col):
    # Tính chỉ số khối 3x3 dựa vào hàng và cột
    return (row // 3) * 3 + (col // 3)

def is_available(mask, num):
    # Kiểm tra bit thứ (num - 1) có bật không (số num đã dùng chưa?)
    return not (mask >> (num - 1)) & 1

def set_bit(mask, num):
    # Bật bit tương ứng với số num (đánh dấu là đã dùng)
    return mask | (1 << (num - 1))

def clear_bit(mask, num):
    # Tắt bit tương ứng với số num (khi backtrack)
    return mask ^ (1 << (num - 1))

def solve_sudoku_bitmask(board):
    # Tạo 3 danh sách để lưu trạng thái bitmask cho từng hàng, cột, khối
    row_mask = [0] * 9
    col_mask = [0] * 9
    box_mask = [0] * 9
    empty_cells = []

    # Bước 1: Duyệt qua toàn bộ bảng và đánh dấu các số đã có bằng bitmask
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num != 0:
                bit = 1 << (num - 1)
                row_mask[i] |= bit         # Đánh dấu số đã có trong hàng
                col_mask[j] |= bit         # Đánh dấu số đã có trong cột
                box_mask[get_box_index(i, j)] |= bit  # Đánh dấu số đã có trong khối 3x3
            else:
                empty_cells.append((i, j))  # Lưu lại vị trí ô trống

    # Bước 2: Hàm backtracking giải Sudoku
    def backtrack(index):
        if index == len(empty_cells):
            return True  # Đã điền hết tất cả ô trống

        i, j = empty_cells[index]
        box = get_box_index(i, j)

        # Thử điền các số từ 1 đến 9 vào ô trống
        for num in range(1, 10):
            if is_available(row_mask[i], num) and is_available(col_mask[j], num) and is_available(box_mask[box], num):
                # Đánh dấu số num vào bảng và cập nhật bitmask
                board[i][j] = num
                row_mask[i] = set_bit(row_mask[i], num)
                col_mask[j] = set_bit(col_mask[j], num)
                box_mask[box] = set_bit(box_mask[box], num)

                # Đệ quy tiếp tục giải ô tiếp theo
                if backtrack(index + 1):
                    return True

                # Nếu không thành công → backtrack: gỡ đánh dấu và xóa số
                board[i][j] = 0
                row_mask[i] = clear_bit(row_mask[i], num)
                col_mask[j] = clear_bit(col_mask[j], num)
                box_mask[box] = clear_bit(box_mask[box], num)

        return False  # Không tìm được số nào phù hợp

    # Gọi hàm backtracking từ ô trống đầu tiên
    return backtrack(0)

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

if solve_sudoku_bitmask(sudoku_board):
    for row in sudoku_board:
        print(row)
else:
    print("Không tìm thấy lời giải cho Sudoku này.")
