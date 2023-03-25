"""Module illustrates and computes two's complement for a variety length of bits."""

import struct

# ---------------------------------------------------------------------------

def check_bin_string(bin_string, num_bits) -> bool:
    """
    Check whether the given binary string `bin_string` is a valid two's complement representation 
    of a signed integer with the specified number of bits `num_bits`. Returns True if the binary 
    string is valid, and False otherwise.

    Args:
    - bin_string (str): A binary string that represents a signed integer in two's complement form.
    - num_bits (int): The number of bits in the binary string.

    Returns:
    - bool: True if the binary string is a valid two's complement representation of a signed 
            integer with the specified number of bits, False otherwise.
    """

    # Check to ensure type is correct
    if not isinstance(bin_string, str):
        return False

    # Check for the obvious binary values
    for digit in bin_string:
        if digit == '0' or digit == '1':
            continue
        else:
            return False

    # If fewer than "num_bits" was provided, fill them up with 0s
    # If more digits are entered than num_bits, zfill() does nothing
    bin_string = bin_string.zfill(num_bits)

    # Check to ensure number of bis entered is correct
    if len(bin_string) != num_bits:
        return False
    
    return True

# ---------------------------------------------------------------------------

def get_negative_num(num_bits, bin_string) -> int:
    """
    Return the negative integer represented by the given binary string `bin_string` in two's complement 
    notation with the specified number of bits `num_bits`.

    Args:
    - num_bits (int): The number of bits in the binary string.
    - bin_string (str): A binary string that represents a signed integer in two's complement form.

    Returns:
    - int: The negative integer represented by the given binary string in two's complement notation.

    Raises:
    - ValueError: If the binary string does not represent a valid two's complement number with the 
                  specified number of bits.

    Notes:
    - This function assumes that the binary string represents a negative number (i.e., has a leading 
      1 bit). If the binary string represents a positive number, the result will be incorrect.
    """

    # The lowest number based on the number of bits provided
    min_num = -1*2**(num_bits-1)

    # Go through each bit and add:
    # - 2^0 adds 1 if the MSB is 1
    # - 2^1 adds 2 if the next bit is 1
    # - 2^2 adds 4 if the next bit is 1
    # ...
    # Goes up to 2^(num_bits-1)
    # Does not compute the MSB because that is the indicator of the signed bit
    for i in range(num_bits-1):
        min_num += int(bin_string[num_bits-i-1]) * 2**i

    return min_num

# ---------------------------------------------------------------------------

def check_num_bits(num_bits, allowed_num_bits) -> bool:
    """
    TBD
    """

    # Must be a digit
    if not num_bits.isdigit():
        return False

    # Must be a number in the allowable set
    if int(num_bits) not in allowed_num_bits:
        return False
    
    return True

# ---------------------------------------------------------------------------

def print_results(bin_string, bin_inv_string, x, y) -> None:
    """
    Check whether the given string `num_bits` represents a valid number of bits for two's complement 
    representation, based on the set of allowed numbers `allowed_num_bits`. Returns True if the 
    `num_bits` is valid, and False otherwise.

    Args:
    - num_bits (str): A string representing the number of bits to use for two's complement representation.
    - allowed_num_bits (set): A set of integers representing the allowed numbers of bits for two's complement 
                              representation.

    Returns:
    - bool: True if the `num_bits` is a valid number of bits for two's complement representation, False 
            otherwise.
    
    Notes:
    - This function assumes that the `num_bits` parameter is a string representation of a positive integer.
    - The `allowed_num_bits` parameter should be a set containing only positive integers.
    """

    print(f'You entered 0b{bin_string}, which is represented as a signed value of: {x}')
    print(f'The two\'s complement is 0b{bin_inv_string}, which is represented as a signed value of: {y}')

# ---------------------------------------------------------------------------

def get_bytes(x) -> tuple:
    """
    Return a tuple of two bytes that represent the given integer `x`.

    Args:
    - x (int): An integer to convert to a tuple of two bytes.

    Returns:
    - tuple: A tuple containing two bytes that represent the given integer.

    Notes:
    - This function assumes that the integer `x` can be represented in two bytes.
    """

    # Grab the 2 bytes representing a SHORT
    first_byte = (x & 0xFF00) >> 8
    second_byte = x & 0x00FF

    return first_byte, second_byte

# ---------------------------------------------------------------------------

if __name__ == '__main__':

    # Allowed number of bits
    allowed_num_bits = {2, 4, 8, 16}

    # The bit masks for each number of bits:
    # - The bit mask for capturing if the MSB is 1 or 0
    # - The bit mask for capturing all bits
    MASKS = {2:  {'MSB_MASK': 0x2, 'ALL_MASK': 0x3},
             4:  {'MSB_MASK': 0x8, 'ALL_MASK': 0xF},
             8:  {'MSB_MASK': 0x80, 'ALL_MASK': 0xFF},
             16: {'MSB_MASK': 0x8000, 'ALL_MASK': 0xFFFF}}

    # Grab # bits to use for processing
    print("Two's complement")
    num_bits = input(f'How many bits will you be providing? Choose a number from this set: {allowed_num_bits}')

    # Check bits were entered correctly
    if not check_num_bits(num_bits, allowed_num_bits):
        print(f'ERROR: {num_bits} is not in {allowed_num_bits}\n\n')
        raise ValueError
    
    # Convert to int
    num_bits = int(num_bits)

    # Grab string representation of bits
    bin_string = input(f'Enter no more than {num_bits} 1s and 0s :')

    # Check binary string
    if not check_bin_string(bin_string, num_bits):
        print(f'ERROR: Non binary characters detected, or input is greater than {num_bits} digits.\n\n')
        raise ValueError
    
    # Convert binary string to integer
    num = int(bin_string, 2)

    # Compute two's complement
    inv_num = MASKS[num_bits]['ALL_MASK'] ^ (num - 1)

    # Convert two's complement to binary string
    bin_inv_string = "{0:b}".format(inv_num).zfill(num_bits)

    # For 2, 4 and 8 bits, do the math myself.  For 16, use struct package like below.
    if num_bits == 16:

        # Grab the 2 bytes for the signed short
        first_byte, second_byte = get_bytes(num)
        first_byte_inv, second_byte_inv = get_bytes(inv_num)

        # Little Endian byte order by default
        # See https://en.wikipedia.org/wiki/Endianness
        # See https://docs.python.org/3/library/struct.html#format-characters
        signed_num = struct.unpack('h', bytes([second_byte, first_byte]))  
        inv_signed_num = struct.unpack('h', bytes([second_byte_inv, first_byte_inv]))
        
    # If the MSB is 1, it is a negative number according to two's complement
    if num & MASKS[num_bits]['MSB_MASK'] == MASKS[num_bits]['MSB_MASK']:

        # Struct did the work of computing the signed value for the 16-bit case
        # For all other number of bits, do the work manually
        if num_bits != 16:
            signed_num = get_negative_num(num_bits, bin_string)
        print_results(bin_string, bin_inv_string, signed_num, inv_num)

    else:
        if num_bits != 16:
            inv_signed_num = get_negative_num(num_bits, bin_inv_string)
        print_results(bin_string, bin_inv_string, inv_signed_num, num)
