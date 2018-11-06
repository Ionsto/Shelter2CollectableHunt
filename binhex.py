filename = input()
with open(filename, "rb") as level:
    byte = level.read(1)
    while byte != "":
        # Do stuff with byte.
        byte = level.read(1)
        