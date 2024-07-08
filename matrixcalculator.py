# Name: Nguyễn Phúc Nguyên
# Student ID: 20227138
# Class:  150328
# Project: 01 - Thư viện/Tiện ích ma trận
# Date: 10 - 06 - 2024

def add_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2):
        raise ValueError("Hai ma trận phải có cùng số lượng hàng")
    
    num_columns1 = len(matrix1[0])
    num_columns2 = len(matrix2[0])
    for row in matrix1:
        if len(row) != num_columns1:
            raise ValueError("Ma trận thứ nhất có hàng không đồng nhất về số lượng cột")
    for row in matrix2:
        if len(row) != num_columns2:
            raise ValueError("Ma trận thứ hai có hàng không đồng nhất về số lượng cột")
    if num_columns1 != num_columns2:
        raise ValueError("Hai ma trận phải có cùng số lượng cột")
    
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[i])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

def subtract_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2):
        raise ValueError("Hai ma trận phải có cùng số lượng hàng")
    
    num_columns1 = len(matrix1[0])
    num_columns2 = len(matrix2[0])
    for row in matrix1:
        if len(row) != num_columns1:
            raise ValueError("Ma trận thứ nhất có hàng không đồng nhất về số lượng cột")
    for row in matrix2:
        if len(row) != num_columns2:
            raise ValueError("Ma trận thứ hai có hàng không đồng nhất về số lượng cột")
    if num_columns1 != num_columns2:
        raise ValueError("Hai ma trận phải có cùng số lượng cột")
    
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[i])):
            row.append(matrix1[i][j] - matrix2[i][j])
        result.append(row)
    return result

def multiply_matrices(matrix1, matrix2):
    num_columns1 = len(matrix1[0])
    for row in matrix1:
        if len(row) != num_columns1:
            raise ValueError("Ma trận thứ nhất có hàng không đồng nhất về số lượng cột")
        
    num_columns2 = len(matrix2[0])
    for row in matrix2:
        if len(row) != num_columns2:
            raise ValueError("Ma trận thứ hai có hàng không đồng nhất về số lượng cột")

    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Số cột của ma trận thứ nhất phải bằng số hàng của ma trận thứ hai")

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            sum = 0
            for k in range(len(matrix1[0])):
                sum += matrix1[i][k] * matrix2[k][j]
            row.append(sum)
        result.append(row)
    return result


def transpose_matrix(matrix):
    num_columns1 = len(matrix[0])
    for row in matrix:
        if len(row) != num_columns1:
            raise ValueError("Ma trận có hàng không đồng nhất về số lượng cột")
        
    result = []
    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        result.append(row)
    return result
def inverse_matrix(matrix): 
    n = len(matrix)
    # Kiểm tra xem ma trận có phải là ma trận vuông không
    if any(len(row) != n for row in matrix):
        raise ValueError("Ma trận phải là ma trận vuông(Ví dụ 3x3)")
    # Tạo ma trận đơn vị cùng kích thước với ma trận đầu vào
    identity_matrix = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    # Ghép ma trận đầu vào với ma trận đơn vị (augmentation)
    aug_matrix = [matrix[i] + identity_matrix[i] for i in range(n)]
    # Áp dụng phương pháp Gauss-Jordan
    for i in range(n):
        # Tìm phần tử chính và đổi dòng nếu cần
        if aug_matrix[i][i] == 0:
            for j in range(i + 1, n):
                if aug_matrix[j][i] != 0:
                    aug_matrix[i], aug_matrix[j] = aug_matrix[j], aug_matrix[i]
                    break
            else:
                raise ValueError("Ma trận không có ma trận nghịch đảo")
        # Chia cả dòng cho phần tử chính
        pivot = aug_matrix[i][i]
        aug_matrix[i] = [element / pivot for element in aug_matrix[i]]
        # Khử các phần tử khác trong cột
        for j in range(n):
            if i != j:
                row_factor = aug_matrix[j][i]
                aug_matrix[j] = [aug_matrix[j][k] - row_factor * aug_matrix[i][k] for k in range(2 * n)]

    # Tách ma trận đơn vị ra khỏi ma trận đã được ghép
    inverse = [row[n:] for row in aug_matrix]
    return inverse
