def convert_str_to_float(s):
    """

    :param s:
    :return:
    """
    try:
        return float(s)
    except (ValueError):
        print("Input error!")
        return ""

print(convert_str_to_float("1"))
print(type(convert_str_to_float("1")))

result = convert_str_to_float("fgfg")
print(result)
print(type(result))

