schematic = list()

with open("sample", 'r') as file:
    for line in file:
        line = line.strip()
        scheme = list()
        for char in line:
            scheme.append(char)
        schematic.append(scheme)

SCHEMATIC_LENGTH = len(schematic)
SCHEME_LENGTH = len(scheme)

for s in schematic:
    print("  ".join(s))

