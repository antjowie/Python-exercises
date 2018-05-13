def main():
    cap = int(input("Make a list only consisting of numbers lower than: "))
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [int(i) for i in a if i < cap]
    print(b)



if __name__ == '__main__':
    main()
