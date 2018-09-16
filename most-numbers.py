def checkio(*arg):
    try:
        return max(arg) - min(arg)
    except:
        return 0