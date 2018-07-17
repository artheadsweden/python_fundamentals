
def my_gen():
    for i in range(10):
        yield i**2

def main():
    text = "HI THERE"
    numbers = [3,6,4,6,8,9,10]
    text_gen = (c.lower() for c in text)
    comp_gen = (i**2 for i in numbers)

    for c in text_gen:
        print(c)

    for x in comp_gen:
        print(x)
    
if __name__ == '__main__':
    main()