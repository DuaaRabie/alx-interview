#!/usr/bin/python3
""" Log parsing """


import sys


def main():
    """ main function """
    total_file_size = 0
    status_codes_count = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            if len(parts) < 7 or parts[1] != '-' or parts[2] != '[' or parts[4] != '"GET' or parts[6] != 'HTTP/1.1"':
                continue

            try:
                status_code = int(parts[5])
                file_size = int(parts[6])
            except (ValueError, IndexError):
                continue

            total_file_size += file_size

            if status_code in status_codes_count:
                status_codes_count[status_code] += 1

            if line_count % 10 == 0:
                print_metrics(total_file_size, status_codes_count)

    except KeyboardInterrupt:
        print_metrics(total_file_size, status_codes_count)

def print_metrics(total_file_size, status_codes_count):
    """ print function """
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes_count):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")

if __name__ == "__main__":
    main()
