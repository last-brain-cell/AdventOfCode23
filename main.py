import re

line = 'one'

matches = re.findall(pattern=r'\d|one|two|three|four|five|six|seven|eight|nine', string=line)

print(matches)
