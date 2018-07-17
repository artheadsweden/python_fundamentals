
def main():
    person = {"name" : "John Smith", "age" : 37, "city" : "London"}
    print(person)
    person["country"] = "UK"
    print(person)
    person["name"] = "Anne Jones"
    print(person)
    print(type(person))
    person[1] = 99
    print(person)
    
if __name__ == '__main__':
    main()