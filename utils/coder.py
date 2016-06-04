def code(val):
    """
    float to binary code
    required float val
    integer part must be -127 < integer_part < 127
    real part may be any
    :returns str
    :example ""10000001.000111001000111010001010"
    """
    try:
        val_split = str(val).split(".")
        integer_part = val_split[0]
        real_part = val_split[1]
        val_in_bin = ""
        if val < 0:
            val_in_bin += "1"
        else:
            val_in_bin += "0"
        if integer_part[0] == "-":
            integer_part = integer_part.split("-")[1]
        integer_part_in_bin = integer_part_to_bin(integer_part)
        real_part_in_bin = real_part_to_bin(real_part)
        val_in_bin += integer_part_in_bin + "." + real_part_in_bin
        return val_in_bin
    except Exception as e:
        print e


def left_part_bin_to_integer(integer_part_in_bin):
    pass


def right_part_bin_to_integer(real_part_in_bin):
    pass


def decode(val_in_bin):
    """
    val_in_bin example "10000001.000111001000111010001010"
    :param val_in_bin:
    :returns float number
    """
    try:
        is_positive = False
        if val_in_bin[0] == "0":
            is_positive = True
        val_split = val_in_bin.split(".")
        integer_part_in_bin = val_split[0][1:]
        real_part_in_bin = val_split[1]
        integer_part = left_part_bin_to_integer(integer_part_in_bin)
        real_part = right_part_bin_to_integer(real_part_in_bin)
    except Exception as e:
        print e


def integer_part_to_bin(val):
    try:
        integer_part_in_bin = bin(int(val)).split("b")[1]
        while len(integer_part_in_bin) != 7:
            integer_part_in_bin = "0" + integer_part_in_bin
        return integer_part_in_bin
    except Exception as e:
        print e


def real_part_to_bin(val):
    """
    val must be str
    """
    try:
        val = "0." + val
        val = float(val)
        count = 24
        val_bin = ""
        while count:
            val *= 2
            if val >= 1:
                val_bin += "1"
            else:
                val_bin += "0"
            val %= 1
            count -= 1
        return val_bin
    except Exception as e:
        print e
