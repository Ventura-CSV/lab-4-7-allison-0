def main():
    numbers = []
    while True:
        N = int(input("Enter a value"))
        numbers.append(N)
        N = int(input("Enter a value"))
        if N <= numbers[-1]:
            numbers.append(N)
        else:
            break

    ########################################
    # Do not delete the return statement
    ########################################
    print(*numbers)
    return numbers


if __name__ == '__main__':
    main()
