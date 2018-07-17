
def main():
    # Write to a text file version 1
    f = open("data.txt", "w")
    try:
        f.write("This is the first line\n")
        f.write("This is the second line\n")
    finally:
        f.close()

    # Write to a text file version 2
    with open("data.txt", "w") as f:
        f.write("This is the first line\n")
        f.write("This is the second line\n")

    # Appending to a text file
    with open("data.txt", "a") as f:
        f.write("This line was added to the file\n")

    # Reading from text files

    # Read all lines into a list
    f = open("data.txt", "r")
    lines = f.readlines()
    print(lines)
    f.close()

    #Read all lines into a string
    f = open("data.txt", "r")
    textfile = f.read()
    print(textfile)
    f.close()

    #Read a line at a time
    f = open("data.txt", "r")
    line = f.readline()
    print(line, end="")
    line = f.readline()
    print(line, end="")
    line = f.readline()
    print(line, end="")
    f.close()

    #Read a file using read(N)
    f = open("data.txt", "r")
    a = f.read(2)
    b = f.read(5)
    print(a)
    print(b)
    f.close()

    #Read using an iterator
    #Don't use this method
    f = open("data.txt", "r")
    for line in f.readlines():
        print(line, end="")
    f.close()

    #Read using an itertor
    f = open("data.txt", "r")
    for line in f:
        print(line, end="")
    f.close()

    #Read using iterator compact version
    for line in open("data.txt", "r"):
        print(line, end="")

    #Read a file using the list constructor
    lines = list(open("data.txt", "r"))
    print(lines)

    #Read a file using list comprehension
    lines = [line.rstrip()  for line in open("data.txt", "r")]
    print(lines)

    #Check if a line is in a text file
    line = "This is the second line\n"
    if line in open("data.txt", "r"):
        print("Line found")
    else:
        print("Line not found")

if __name__ == '__main__':
    main()