def checkio(str_number: str, radix: int) -> int:
    try:
        return int(str_number,radix)
    except:
        return -1
