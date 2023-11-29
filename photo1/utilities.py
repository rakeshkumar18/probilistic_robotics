def sum_nested_list(nested_list):
    sum = 0
    for i in range(len(nested_list)):
        for j in range(len(nested_list[i])):
            sum += nested_list[i][j]
    return sum