def code(val):
    """
    float to binary code
    required float val
    integer part must be -127 < integer_part < 127
    real part may be any
    """
    try:
        val_split = str(val).split(".")
        integer_part = val_split[0]
        real_part = val_split[1]
        integer_part_in_bin = bin(int(integer_part)).split("b")[1]
    except Exception as e:
        print e


def real_part_to_bin(val):
    try:
        val = "0." + val
        val = float(val)
        count = 27
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
