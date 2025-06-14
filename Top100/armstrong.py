num = int(input())
numlen = len(str(num))

result = 0

for digit in (str(num)):
    result += int(digit) ** numlen

if result == num:
    print("Armstrng")
else:
    print("Not")
