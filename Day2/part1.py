RED = 12
GREEN = 13
BLUE = 14


def game_is_possible(string: str) -> [int, bool]:
    r = g = b = 0
    idx, sets = string.split(": ")[0].strip("Game "), string.split(": ")[1].split("; ")

    for s in sets:
        cubes = s.split(", ")
        for cube in cubes:
            c = cube.split(" ")
            if c[1] == 'red':
                if int(c[0]) > r:
                    r = int(c[0])
            elif c[1] == 'green':
                if int(c[0]) > g:
                    g = int(c[0])
            elif c[1] == 'blue':
                if int(c[0]) > b:
                    b = int(c[0])

    if r <= RED and g <= GREEN and b <= BLUE:
        return int(idx)


code = 0
with open("day2_input", 'r') as file:
    for line in file:
        line = line.strip()
        possible = game_is_possible(line)
        if possible:
            code += possible

        print(f"{line} ---> {possible} ---> {code}")

print(code)
