import sys


def merge_lists():
    res = [0] * 101
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        arr = sys.stdin.readline().strip()
        for j, c in enumerate(arr.split(' ')):
            if j == 0:
                continue
            res[int(c)] += 1

    output = [(str(k) + ' ') * val for k, val in enumerate(res) if val > 0]
    output = ''.join(output)

    print(output)


if __name__ == "__main__":
    merge_lists()
