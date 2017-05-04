import whois
import re


# str(w)

# result = re.findall(r'@\w+.\w+', str(w))
# print(result)


# from datetime import datetime
# print(datetime.now())


def domenTell():
    w = whois.whois('таймвеб.рф')
    return str(w)

