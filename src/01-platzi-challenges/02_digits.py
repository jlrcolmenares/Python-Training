# Print the numbers of digits of a given number

def digits(number):
    count = 0 #
    while number > 0:
        number = number//10 # 9//10 = 0
        count += 1
    return count

print('1:',digits(1))
print('25:', digits(25))
print('144:',digits(144))
print('1001:',digits(1001))
print('1000:',digits(1000))
print('100:',digits(100))
print('10:',digits(10))
print('0:',digits(0))
print('32000:',digits(32000)) 