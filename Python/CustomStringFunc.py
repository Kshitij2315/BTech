# Custom String Functions

def cust_len(s):
    count = 0
    for ch in s:
        count += 1
    return count


def cust_min(s):
    min_char = s[0]
    for ch in s:
        if ch < min_char:
            min_char = ch
    return min_char


def cust_max(s):
    max_char = s[0]
    for ch in s:
        if ch > max_char:
            max_char = ch
    return max_char


def cust_find(s, search):
    n = len(s)
    m = len(search)

    for i in range(n - m + 1):
        if s[i:i + m] == search:
            return i
    return -1


def cust_upper(s):
    result = ""
    for ch in s:
        if 'a' <= ch <= 'z':
            result += chr(ord(ch) - 32)
        else:
            result += ch
    return result


def cust_lower(s):
    result = ""
    for ch in s:
        if 'A' <= ch <= 'Z':
            result += chr(ord(ch) + 32)
        else:
            result += ch
    return result


def cust_join(sep, lst):
    result = ""
    for i in range(len(lst)):
        result += lst[i]
        if i != len(lst) - 1:
            result += sep
    return result


def cust_replace(s, old, new):
    result = ""

    for ch in s:
        if ch == old:
            result += new
        else:
            result += ch

    return result

def cust_swapcase(s):
    result = ""

    for ch in s:
        if 'a' <= ch <= 'z':
            result += chr(ord(ch) - 32)
        elif 'A' <= ch <= 'Z':
            result += chr(ord(ch) + 32)
        else:
            result += ch

    return result


def cust_capitalize(s):
    result = ""

    for i in range(len(s)):
        if i == 0 and 'a' <= s[i] <= 'z':
            result += chr(ord(s[i]) - 32)
        elif i != 0 and 'A' <= s[i] <= 'Z':
            result += chr(ord(s[i]) + 32)
        else:
            result += s[i]

    return result

def cust_partition(s, sep):
    pos = cust_find(s, sep)

    if pos == -1:
        return (s, "", "")

    return (s[:pos], sep, s[pos + len(sep):])

def cust_rpartition(s, sep):
    pos = cust_find(s, sep)

    if pos == -1:
        return ("", "", s)

    return (s[:pos], sep, s[pos + len(sep):])

def cust_split(s, sep):
    result = []
    word = ""

    for ch in s:
        if ch == sep:
            result.append(word)
            word = ""
        else:
            word += ch

    result.append(word)
    return result

def cust_rsplit(s, sep):
    result = []
    word = ""

    i = len(s) - 1

    while i >= 0:
        if s[i] == sep:
            result.insert(0, word)
            word = ""
        else:
            word = s[i] + word
        i -= 1

    result.insert(0, word)
    return result

def cust_lstrip(s):
    i = 0

    while i < len(s) and s[i] == ' ':
        i += 1

    return s[i:]

def cust_rstrip(s):
    i = len(s) - 1

    while i >= 0 and s[i] == ' ':
        i -= 1

    return s[:i+1]

def cust_strip(s):
    return cust_rstrip(cust_lstrip(s))

s = "        KshItiJ        "
search = "ti"

print("Length :", cust_len(s), len(s))
print("Min    :", cust_min(s), min(s))
print("Max    :", cust_max(s), max(s))
print("Find   :", cust_find(s, search), s.find(search))
print("Upper  :", cust_upper(s), s.upper())
print("Lower  :", cust_lower(s), s.lower())

s1 = "Python-is-easy"
sep = "-"

print("Join       :", cust_join(sep, s), sep.join(s))
print("Replace    :", cust_replace(s, "ti", "XX"), s.replace("ti", "XX"))
print("Swapcase   :", cust_swapcase(s), s.swapcase())
print("Capitalize :", cust_capitalize(s), s.capitalize())
print("Partition  :", cust_partition(s1, sep), s1.partition(sep))
print("RPartition :", cust_rpartition(s1, sep),s1.rpartition(sep))
print("Split: ", cust_split(s1, sep),s1.split(sep))
print("RSplit: ", cust_rsplit(s1, sep),s1.rsplit(sep))
print("LStrip: ",cust_lstrip(s), s.lstrip())
print("RStrip: ",cust_rstrip(s), s.rstrip())
print("Strip: ", cust_strip(s), s.strip())
