
def main():
    my_list = [1, 2, 3, 4, 5]

    result_list = []
    for value in my_list:
        if value != 3:
            result_list.append(value**2)


    print(result_list)

    result_list2 = [value**2 for value in my_list if value != 3]
    print(result_list2)

    result_list3 = [i*j for i in range(4) for j in range(3)]
    print(result_list3)

    result_list4 = []
    for i in range(4):
        for j in range(3):
            result_list4.append(i*j)

    print(result_list4)

    
if __name__ == '__main__':
    main()