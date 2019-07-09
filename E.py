def anagram_first(s1, s2):
    l1 = list(s1)
    l1.sort()
    l2 = list(s2)
    l2.sort()

    print(1 if l1 == l2 else 0)


if __name__ == "__main__":
    s1 = input()
    s2 = input()

    anagram_first(s1, s2)
