
def main():
    name = ""
    name_list = []
    while name.lower() != "exit":
        name = input("Enter a name. End with exit: ")
        if name.lower() != "exit":
            name_list.append(name)

    print(name_list)
    
if __name__ == '__main__':
    main()