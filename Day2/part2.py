RED = 12
GREEN = 13
BLUE = 14


def power_of_set_of_cubes(string: str) -> int:
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

    return r * g * b


code = 0
with open("day2_input", 'r') as file:
    for line in file:
        line = line.strip()
        power = power_of_set_of_cubes(line)

        code += power

        print(f"{line} ---> {power}")

print(code)
