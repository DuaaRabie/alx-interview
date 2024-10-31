#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """ checks utf-8 validation """
    byte_count = 0
    for byte in data:
        # Check if it's a continuation byte
        if byte >= 128:
            # Count leading zeros
            leading_zeros = 0
            while (byte & (1 << (7 - leading_zeros))) == 0:
                leading_zeros += 1

            # Check if it's the first byte of a multi-byte sequence
            if leading_zeros == 0:
                return False

            # Check if it's the second or third byte
            if leading_zeros > 1:
                return False

            # Update byte count
            byte_count += 1 + leading_zeros

    # Check if the total byte count matches the expected count
    if byte_count % 4 != 0:
        return False

    return True
