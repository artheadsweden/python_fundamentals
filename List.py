
def main():
    pals = ['Peter', 'Anna', 'Sue', 'John', 'Anna']
    pals.append('Lisa')
    print(pals)
    pals.remove('Anna')
    pals.remove('Anna')
    print(pals)
    pals.pop()
    print(pals)
    pals[0] = "Anna"
    print(pals)

if __name__ == '__main__':
    main()