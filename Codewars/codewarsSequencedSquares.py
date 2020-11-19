# import math

# def squared_digits_series(n):
#     nearest_power_of_2 = int(math.log2(n))
#     result = 0
#     count = n - 2 ** nearest_power_of_2 + 1
#     result += ((2 ** nearest_power_of_2) * 10 + 1) * count
#     for i in reversed(range(0,nearest_power_of_2)):
#         count = 2 ** i
#         result += ((2 ** i) * 10 + 1) * count
#     return result

# print(squared_digits_series(100000000))

# import ipaddress as ip

# def int_to_ipv4(int_ip):
#    return str(ip.IPv4Address(int_ip))

# print(int_to_ipv4(2149583361))