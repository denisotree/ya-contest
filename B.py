current_len = 0
max_len = 0

try:
    f = open("input.txt")
    for i, line in enumerate(f):
        if i == 0:
            try:
                int(line)
                if int(line) > 10000:
                    break
            except ValueError:
                break
        else:
            try:
                int(line)
                if int(line) == 1:
                    current_len += 1
                    if current_len > max_len:
                        max_len = current_len
                elif int(line) == 0:
                    if current_len > max_len:
                        max_len = current_len
                    current_len = 0
            except ValueError:
                break

    print(max_len)

except IOError:
    print(max_len)
