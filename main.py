def create_fib(items):
    fib = [0, 1]
    for current in range(2, items):
        fib.append(fib[current-1] + fib[current-2])
    return fib


def enter_num():
    num = int(input("Enter num: "))
    return num


def find_num(fib, num):
    for i in range(0, len(fib)-1):
        if fib[i] == num:
            print(f"Representation is {fib[i]}")
            break
        elif fib[i] > num:
            new_fib = fib[:i]
            new_fib.reverse()
            print(new_fib)
            for j in range(0, len(new_fib)-1):
                value1 = num - fib[j]
                j += 1

            print(f"Closest is {fib[i-1]}")
            break






if __name__ == "__main__":
    fib = create_fib(31)
    num = enter_num()
    find_num(fib, num)
