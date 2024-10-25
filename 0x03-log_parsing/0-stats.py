#!/usr/bin/python3
""" log parsing """


import re
import sys


def parse_line(line):
    """ parse func """
    pattern = (
        r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] '
        r'"GET /projects/260 HTTP/1.1" (\d+) (\d+)$')
    match = re.match(pattern, line.strip())
    if match:
        ip, date, status_code, file_size = match.groups()
        return int(status_code), int(file_size)
    return None


def main():
    """ main func"""
    total_file_size = 0
    status_counts =\
        {str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}

    try:
        for line_num, line in enumerate(sys.stdin, start=1):
            parsed = parse_line(line)
            if parsed:
                status_code, file_size = parsed
                total_file_size += file_size
                status_counts[str(status_code)] += 1

                if line_num % 10 == 0 or line_num == 1:
                    print(f"File size: {total_file_size}", end="\n")
                    sorted_status_codes = \
                        sorted(status_counts.keys(), key=lambda x: int(x))
                    for code in sorted_status_codes:
                        if status_counts[code] > 0:
                            print(f"{code}: {status_counts[code]}")

    except BrokenPipeError:
        print("Connection closed.")
    finally:
        print(f"File size: {total_file_size}")
        sorted_status_codes = \
            sorted(status_counts.keys(), key=lambda x: int(x))
        for code in sorted_status_codes:
            if status_counts[code] > 0:
                print(f"{code}: {status_counts[code]}")
        except KeyboardInterrupt:
            print("")

if __name__ == "__main__":
    main()
