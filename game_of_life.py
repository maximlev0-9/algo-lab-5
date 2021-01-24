def get_generation(cells, generations):
    result = [[0 for i in range(len(cells[0]))] for i in range(len(cells))]
    rows = len(cells)
    cols = len(cells[0])
    for iteration in range(generations):
        for row in range(rows):
            for col in range(cols):
                neighbour_cells = get_neighbour_cells(row, col, rows, cols)
                # print("generation:", iteration)
                print(row, col)
                print(neighbour_cells)
                count = 0
                for i, j in neighbour_cells:
                    if cells[i][j]:
                        count += 1
                if count == 3 or (count == 2 and cells[row][col]):
                    result[row][col] = 1
                else:
                    result[row][col] = 0
        cells = result
        result = [[0 for i in range(len(cells[0]))] for i in range(len(cells))]

    return result


def get_neighbour_cells(i, j, rows, cols):
    neighbour_cells = []

    possible_neighbour_cells = [(i-1, j-1),
                                (i, j-1),
                                (i+1, j-1),
                                (i+1, j),
                                (i+1, j+1),
                                (i, j+1),
                                (i-1, j+1),
                                (i-1, j)]

    not_left = not j == 0
    not_top = not i == 0
    not_right = not j == cols-1
    not_bottom = not i == rows-1

    conditions = [not_left and not_top, not_left, not_left and not_bottom,
                  not_bottom, not_bottom and not_right, not_right, not_right and not_top, not_top]

    for i in range(8):
        if conditions[i]:
            neighbour_cells.append(possible_neighbour_cells[i])

    return neighbour_cells


def main():
    start = [[1, 0, 0],
             [0, 1, 1],
             [1, 1, 0]]
    end = [[0, 1, 0],
           [0, 0, 1],
           [1, 1, 1]]

    result = get_generation(start, 1)
    print('my_result:')
    print(result)
    print('correct:')
    print(end)


if __name__ == '__main__':
    main()
    # TODO: make input from console and any number of iterations
