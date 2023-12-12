#!/usr/bin/python3
'''log parsing script'''


def print_metrics(file_size, codes):
    """prints metrics"""
    print(f"File size: {file_size}")
    for element in sorted(codes):
        print(f"{element}: {codes[element]}")


if __name__ == "__main__":
    import sys

    count = 0
    file_size = 0
    codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']

    try:
        for line in sys.stdin:
            if count == 10:
                print_metrics(file_size, codes)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                file_size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    codes[line[-2]] = codes.get(line[-2], 0) + 1
            except IndexError:
                pass

        print_metrics(file_size, codes)

    except KeyboardInterrupt:
        print_metrics(file_size, codes)
        raise
