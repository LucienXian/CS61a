def multiple(a, b):
    """Return the smallest number n that is a multiple of both a and b.

    >>> multiple(3, 4)
    12
    >>> multiple(14, 21)
    42
    """
    return a * b // gcm(a, b)

def gcm(a, b):
    if a>=b:
        if a%b == 0:
            return b
        else:
            return gcm(b, a-b)
    else:
        return gcm(b, a)

def has_digit(n, k):
    while n!=0:
        temp = n % 10
        if temp == k:
            return True
        n = n//10
    return False

def unique_digits(n):
    """Return the number of unique digits in positive integer n

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(1313131) # 1 and 3
    2
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(10000) # 0 and 1
    2
    >>> unique_digits(101) # 0 and 1
    2
    >>> unique_digits(10) # 0 and 1
    2
    """
    count = 0
    for i in range(0, 10):
        if has_digit(n, i):
            count += 1
    return count
