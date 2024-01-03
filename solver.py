"""python program to find maximum sum"""
def find_length(input_list, ans, max_sum, i, j):
    """recursive function to find maximum sum"""
    if i>=len(input_list):
        return max_sum
    ans += input_list[i][j]
    max_sum = find_length(input_list, ans, max_sum, i+1, j)
    max_sum = find_length(input_list, ans, max_sum, i+1, j+1)
    if ans > max_sum:
        max_sum = ans
    return max_sum

    
def solver(input_string: str = None):
    """main function"""
    if input_string: # if the input is given in form of a string then this if block will convert it into a 2D grid
        temp = input_string.split("\n")
        temp_list = [i.split() for i in temp]
        input_list = [[int(i) for i in j] for j in temp_list]
    ans, max_sum = 0, 0
    max_sum = find_length(input_list, ans, max_sum, 0, 0)
    return max_sum

if __name__ == "__main__":
    input_string = """3
7 4
2 4 6
8 5 9 3"""
    print(solver(input_string))
