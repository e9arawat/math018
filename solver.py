"""python program to find maximum sum"""


def find_length(input_list, ans, max_sum, i, j):
    """recursive function to find maximum sum"""
    if i >= len(input_list):
        return max_sum
    ans += input_list[i][j]
    max_sum = find_length(input_list, ans, max_sum, i + 1, j)
    max_sum = find_length(input_list, ans, max_sum, i + 1, j + 1)
    if ans > max_sum:
        max_sum = ans
    return max_sum


def solver(input_list):
    """main function"""
    ans, max_sum = 0, 0
    max_sum = find_length(input_list, ans, max_sum, 0, 0)
    return max_sum


if __name__ == "__main__":
    print(solver([[1], [2, 3], [4, 5, 6], [7, 8, 9, 8]]))
