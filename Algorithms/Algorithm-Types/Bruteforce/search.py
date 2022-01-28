def search(haystack, needle):
    for position, item in enumerate(haystack):
        if item == needle:
            return position
    return -1