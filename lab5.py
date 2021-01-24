import re

def naive_search(string:str, substring:str):
    result = []
    for index in range(len(string)-len(substring)+1):
        for substr_index in range(len(substring)):
            if not string[index+substr_index]==substring[substr_index]:
                break
        else:
            result.append((index, index+len(substring)))
    return result


print(naive_search("AC2AC2FA", "АС2"))

print(re.search(re.escape("A+"),"A+C2AC2FA"))

