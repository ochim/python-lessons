# filter(function, iterator)

def is_even(n):
    return n % 2 == 0

#print(list(filter(is_even,range(11))))

print(list(filter(lambda n: n%2 == 0,range(11))))
