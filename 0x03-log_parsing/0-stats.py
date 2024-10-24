#!/usr/bin/python3
""" log parsing """


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

            if len(parts) < 7:
                continue

            # Extract components
            ip = parts[0]
            date = parts[2].strip('[]')
            request = parts[3] + " " + parts[4] + " " + parts[5]  # "GET /projects/260 HTTP/1.1"
            status_code = parts[6]
            try:
                file_size = int(parts[7])
            except (ValueError, IndexError):
                continue

            # Update total file size
            total_file_size += file_size

            # Update status code counts
            if status_code in status_codes_count:
                status_codes_count[int(status_code)] += 1

            # Print metrics every 10 lines
            if line_count % 10 == 0:
                print_metrics(total_file_size, status_codes_count)

    except KeyboardInterrupt:
        print_metrics(total_file_size, status_codes_count)

def print_metrics(total_file_size, status_codes_count):
    """ print function """
    print(f"File size: {total_file_size}")
    
    # Sort status codes
    sorted_status_codes = sorted(status_codes_count.keys(), key=lambda x: int(x))
    
    # Print each status code and count
    for code in sorted_status_codes:
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")

if __name__ == "__main__":
    main()
