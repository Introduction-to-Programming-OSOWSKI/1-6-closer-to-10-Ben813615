def close10(a, b):
    if abs(a-10) < abs(b-10):
        return a
    elif abs(a-10) > abs(b-10):
        return b
    else:
        return 0

print (close10(8,8))


