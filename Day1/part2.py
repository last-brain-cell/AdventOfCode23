import re

digits = {
    "oneight": "18",
    "twone": "21",
    "threeight": "38",
    "fiveight": "58",
    "sevenine": "79",
    "eightwo": "82",
    "eighthree": "83",
    "nineight": "98",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

nums = list()
with open("day1_input", "r") as file:
    for line in file:
        for digit in digits:
            line = line.replace(digit, digits.get(digit))

        matches = re.findall(pattern=r'\d', string=line)
        output = matches[0] + matches[-1]
        nums.append(int(output))

code = sum(nums)
print(f"\nFinal Answer: {code}")
