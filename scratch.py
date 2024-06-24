def print_sequences(char_list, n, _accum=[]):
    if len(_accum) == n:
        print(_accum)
    else:
        for c in char_list:
            if c in _accum:
                continue
            print_sequences(char_list, n, _accum + [c])


print_sequences([1, 2, 3, 4, 5, 6, 7, 8,9,10], 10)
