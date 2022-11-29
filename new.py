def number_mult(num):
    if num == 0 or num == 1:
        return 1
    else:
        return number_mult(num) * number_mult(num - 1)
