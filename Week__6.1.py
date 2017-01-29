import sys

print("Please enter an ipAddress in the format xxx.yyyy.zzzz.nnnn: ")

ipAddress = sys.stdin.readline()

print(ipAddress.count("."))