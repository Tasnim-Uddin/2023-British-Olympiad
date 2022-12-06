def create_fib(items):
    fib = [0, 1]
    for current in range(2, items):
        fib.append(fib[current-1] + fib[current-2])
    return fib


def enter_num():
    num = int(input("Enter num: "))
    return num


def new_fib(fib, num):
    for i in range(0, len(fib)-1):
        if fib[i] > num:
            new_fib = fib[:i]
            new_fib.reverse()
            skip = 2
            del new_fib[skip - 1::skip]
            greatest = new_fib[0]
            return greatest
            break


def find_representations(new_fib, num):
    while num > 0:
        values = new_fib(fib, num)
        print(values, end=" ")
        num -= values



if __name__ == "__main__":
    fib = create_fib(1000)
    print(fib)
    num = enter_num()
    greatest = new_fib(fib, num)
    find_representations(new_fib, num)

