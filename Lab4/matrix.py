def make_matrix(n_rows=3, n_cols=3):
    mat = []
    for i in range(n_rows):
        row = []
        for j in range(n_cols):
            val = int(input(f"enter {i + 1} row {j + 1} col element : "))
            row.append(val)
        mat.append(row)
    return mat


def display_matrix(mat, n_rows=3, n_cols=3, transpose=False):
    if transpose:
        for i in range(n_rows):
            for j in range(n_cols):
                print(mat[j][i], end=" ")
            print()
    else:
        for i in range(n_rows):
            for j in range(n_cols):
                print(mat[i][j], end=" ")
            print()


def add_all_elements(mat, n_rows=3, n_cols=3):
    total_sum = 0
    for i in range(n_rows):
        for j in range(n_cols):
            total_sum += mat[i][j]
    return total_sum


def add_diag_elements(mat, n_rows=3, n_cols=3):
    diag_sum = 0
    for i in range(n_rows):
        for j in range(n_cols):
            if i == j:
                diag_sum += mat[i][j]
    return diag_sum


def find_largest_and_smallest_element(mat, n_rows=3, n_cols=3):
    largest_el = mat[0][0]
    smallest_el = largest_el
    for i in range(n_rows):
        for j in range(n_cols):
            val = mat[i][j]
            if val > largest_el:
                largest_el = val
            if val < smallest_el:
                smallest_el = val
    return largest_el, smallest_el


if __name__ == "__main__":
    print("creating matrix...")
    mat = make_matrix()

    display_matrix(mat)

    print("total sum of all elements: ", add_all_elements(mat))

    print("total sum of diagonal elements: ", add_diag_elements(mat))

    largest, smallest = find_largest_and_smallest_element(mat)
    print(f"largest element: {largest}, and smallest element: {smallest}")

    print("transpose of matrix: ")
    display_matrix(mat, transpose=True)
