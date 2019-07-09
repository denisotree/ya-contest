def del_duplicates():
    a = []
    try:
        with open('input.txt') as f:
            first_line = f.readline()
            try:
                if int(first_line) > 1000000:
                    return False
            except ValueError:
                return False
            for line in f:
                try:
                    if len(a):
                        if int(line) != a[-1]:
                            a.append(int(line))
                            print(int(line))
                    else:
                        a.append(int(line))
                        print(int(line))
                except ValueError:
                    continue

    except IOError:
        return False


if __name__ == "__main__":
    del_duplicates()
