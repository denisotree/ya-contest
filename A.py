def find_jewelry(jewelry, stones):
    count = 0
    for stone in stones:
        if stone in jewelry:
            count += 1
    return count


if __name__ == '__main__':

    j = input()
    s = input()

    if len(j) <= 100 and len(s) <= 100:
        print(find_jewelry(j, s))
