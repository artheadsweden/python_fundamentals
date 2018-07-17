
def main():
    values = (1, 2, 3, 4, [99, 98, 97], 3.14, True)
    values[4][1] = 101
    values[4].append(999)
    print(values)


    
if __name__ == '__main__':
    main()