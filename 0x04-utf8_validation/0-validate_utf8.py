#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """ checks utf-8 validation """
    # Initialize variables
    i = 0
    n_bytes = 0
    max_bytes = 0

    # Iterate through the data
    while i < len(data):
        # Get the current byte
        byte = data[i]

        # Check if it's a start of sequence
        if (byte & 0x80) == 0:
            # 1-byte sequence
            max_bytes = 1
        elif (byte & 0xE0) == 0xC0:
            # 2-byte sequence
            max_bytes = 2
        elif (byte & 0xF0) == 0xE0:
            # 3-byte sequence
            max_bytes = 3
        elif (byte & 0xF8) == 0xF0:
            # 4-byte sequence
            max_bytes = 4
        else:
            # Invalid byte
            return False

        # Check if we've exceeded the maximum allowed bytes
        if n_bytes + max_bytes > 4:
            return False

        # Increment n_bytes counter
        n_bytes += 1

        # Move to the next byte
        i += 1

    # Check if we've processed all bytes
    if n_bytes != max_bytes:
        return False

    # If we reach here, the data is valid UTF-8
    return True
