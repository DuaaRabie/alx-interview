#!/usr/bin/python3
""" UTF-8 Validation """
""" check Commit df6c627 is another way to solve it """


def validUTF8(data):
    """ checks utf-8 validation """
    expected_bytes = 0

    for byte in data:
        # Get the 8 least significant bits of the byte
        byte = byte & 0xFF

        # expected bytes
        if expected_bytes == 0:
            if (byte >> 7) == 0b0:
                expected_bytes = 0
            elif (byte >> 5) == 0b110:
                expected_bytes = 1
            elif (byte >> 4) == 0b1110:
                expected_bytes = 2
            elif (byte >> 3) == 0b11110:
                expected_bytes = 3
            else:
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            expected_bytes -= 1

    return expected_bytes == 0
