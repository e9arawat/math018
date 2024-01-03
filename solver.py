def solver(input_string):
    i = 1
    index, i = 0, 1
    input_list = []
    while index < len(input_string):
        temp_list = []
        for j in range(i):
            temp_list.append(int(input_string[index]))
            index += 1
        input_list.append(temp_list)
        i+=1

    for i in input_list:
        print(i)

if __name__ == "__main__":
    print(solver('1234567898'))
