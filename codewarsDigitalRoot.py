<<<<<<< HEAD
def digital_root(n):
    while n>=10:
        n = sum(int(x) for x in str(n))
    return n

=======
def digital_root(n):
    while n>=10:
        n = sum(int(x) for x in str(n))
    return n

>>>>>>> 5163535b87aef3f153fee9a8c1cb75fa7110cd77
print(digital_root(942))