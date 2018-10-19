__author__ = 'Reijer'

def cutstring(s, a, b, c, d):
    """s:string max 200; a,b,c,d: integers"""
    return s[a:b+1] + " " + s[c:d+1]

def test():
    s = "jyel8a4D5HDSKq3C42RWhucfqHWDSZY7ITrionyxCQaz4bvgL3S9SQzyWLwTaEuBlhH94u7t3hUv60Jk99SJSxTeLdlBIOxHViMVHuxN0qcTzV8ddFm7onFykoTWDQm9zDZHq8WCS6bx9wX8XGQ6h2NaKBaQGC7kcUNv1Wqcaninust0F1ReIV1qLF2."
    a = 33
    b = 39
    c = 167
    d = 173
    ans = cutstring(s, a, b, c, d)
    print ans


if __name__ == '__main__':
    test()