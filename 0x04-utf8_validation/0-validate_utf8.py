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

            # Check if it's the first byte of a multi-byte sequence
            if expected_bytes > 4:
                return False

        else:
            expected_bytes -= 1
            if (byte >> 6) != 0b10:
                return False
            expected_bytes -= 1

    return True
