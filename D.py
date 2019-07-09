def brackets(pairs, s='', l=0, r=0):
    if l == pairs and r == pairs:
        print(s)
    else:
        if l < pairs:
            brackets(pairs, s + '(', l + 1, r)
        if r < l:
            brackets(pairs, s + ')', l, r + 1)


if __name__ == "__main__":

    n = int(input())

    brackets(n)
