import sys


def main():
    if len(sys.argv) < 3:
        print("Input and Output files required")
        return

    source = sys.argv[1]
    dest = sys.argv[2]

    print("Parsing data")
    data = []
    with open(source) as src:
        for line in src:
            convertedLine = map(lambda _hex: int(_hex, 16), line.split(" "))
            data += convertedLine
            # for _hex in line.split(" "):
            #     data.append(int(_hex, 16))
    print("Done parsing")
    with open(dest, "wb") as dst:
        dst.write(bytearray(data))

    print("Complete")


if __name__ == "__main__":
    main()
