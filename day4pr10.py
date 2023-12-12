def isScramble(s1, s2):
    if len(s1) != len(s2) or sorted(s1) != sorted(s2):
        return False
    if s1 == s2:
        return True
    n = len(s1)
    for i in range(1, n):
        if (isScramble(s1[:i], s2[:i]) and isScramble(s1[i:], s2[i:])) or \
           (isScramble(s1[:i], s2[-i:]) and isScramble(s1[i:], s2[:-i])):
            return True
    return False
s1 = "great"
s2 = "rgeat"
result = isScramble(s1, s2)
print(result)
