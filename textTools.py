

def is_int(num) -> bool:
    try:
        int(num)
        return True
    except:
        return False


def count_words(string: str) -> int:
    """
    count words in string
    """
    sparte_betwwn_words = {" ": True, ",": True, ".": True}
    num = 0
    i = 0
    if string[i] not in sparte_betwwn_words and not is_int(string[i]):
        num += 1
    while i < len(string) - 1:
        i += 1
        if string[i] not in sparte_betwwn_words and not is_int(string[i]):
            if string[i - 1] in sparte_betwwn_words:
                num += 1

    return num





