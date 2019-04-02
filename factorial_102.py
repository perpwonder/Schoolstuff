def factorial(f):
    if f <= 1:
        return 1
    else:
        return f * factorial(f - 1)
