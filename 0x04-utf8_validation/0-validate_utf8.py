#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """ checks utf-8 validation """
    expected_bytes = 0

    for byte in data:
        # Get the 8 least significant bits of the byte
        byte = byte & 0xFF

        # expected bytes
        if expected_bytes == 0:
            while (byte & (1 << (7 - expected_bytes))) != 0:
                expected_bytes += 1
            if expected_bytes in [0, 2, 3, 4]:
                if expected_bytes != 0:
                    expected_bytes -= 1
            else:
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            expected_bytes -= 1

    return expected_bytes == 0
