import re

nums = list()
with open("day1_input", "r") as file:
    for line in file:
        matches = re.findall(pattern=r'\d', string=line)
        output = matches[0] + matches[-1]
        nums.append(int(output))

code = sum(i for i in nums)
print(code)
