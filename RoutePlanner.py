def route_exists(from_row, from_column, to_row, to_column, map_matrix):
    visited = [[False] * len(map_matrix[0]) for _ in range(len(map_matrix))]
    return dfs(from_row, from_column, to_row, to_column, map_matrix, visited)

def dfs(row, column, to_row, to_column, map_matrix, visited):
    # Check if the current position is out of bounds or already visited
    if row < 0 or row >= len(map_matrix) or column < 0 or column >= len(map_matrix[0]) or visited[row][column]:
        return False

    # Check if the current position is the destination
    if row == to_row and column == to_column:
        return True

    visited[row][column] = True

    # Check the neighboring positions (up, down, left, right)
    if (row > 0 and map_matrix[row - 1][column] and dfs(row - 1, column, to_row, to_column, map_matrix, visited)) or \
            (row < len(map_matrix) - 1 and map_matrix[row + 1][column] and dfs(row + 1, column, to_row, to_column, map_matrix, visited)) or \
            (column > 0 and map_matrix[row][column - 1] and dfs(row, column - 1, to_row, to_column, map_matrix, visited)) or \
            (column < len(map_matrix[0]) - 1 and map_matrix[row][column + 1] and dfs(row, column + 1, to_row, to_column, map_matrix, visited)):
        return True

    return False


if __name__ == '__main__':
    map_matrix = [
        [True, False, False],
        [True, True, False],
        [False, True, True]
    ]

    print(route_exists(0, 0, 2, 2, map_matrix))
