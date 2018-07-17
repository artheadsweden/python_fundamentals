
def main():
    my_list = [1, 2, 3, 4, 5]

    #List Comprehension
    result_list = [value**2 for value in my_list if value != 3]
    print(result_list)

    #Set comprehension
    result_set = {value**2 for value in my_list if value != 3}
    print(result_set)

    #Dict comprehension
    result_dict = {value: value**2 for value in my_list if value != 3}
    print(result_dict)

    #Tuple comprehension
    result_tuple = tuple([value**2 for value in my_list if value != 3])
    print(result_tuple)
    
if __name__ == '__main__':
    main()