# coding=utf-8

# input: array with multiple strings
# expected output: rank of the 3 most often repeated words in given set of strings and number of times they occured, case insensitive

sentences = [
    'Taki mamy klimat',
    'Wszędzie dobrze ale w domu najlepiej',
    'Wyskoczył jak Filip z konopii',
    'Gdzie kucharek sześć tam nie ma co jeść',
    'Nie ma to jak w domu',
    'Konduktorze łaskawy zabierz nas do Warszawy',
    'Jeżeli nie zjesz obiadu to nie dostaniesz deseru',
    'Bez pracy nie ma kołaczy',
    'Kto sieje wiatr ten zbiera burzę',
    'Być szybkim jak wiatr',
    'Kopać pod kimś dołki',
    'Gdzie raki zimują',
    'Gdzie pieprz rośnie',
    'Swoją drogą to gdzie rośnie pieprz?',
    'Mam nadzieję, że poradzisz sobie z tym zadaniem bez problemu',
    'Nie powinno sprawić żadnego problemu, bo Google jest dozwolony',
]

# Example result:
# 1. "mam" - 12
# 2. "tak" - 5
# 3. "z" - 2


# Good luck! You can write all the code in this file.

def occurrences(str_arr):
    arr = ' '.join(str_arr).lower().split()
    arr_alnum = []
    for w in arr:
        arr_alnum.append(''.join(filter(str.isalnum, w)))

    dic = (dict((w, arr_alnum.count(w)) for w in arr_alnum))
    dic_sorted = sorted(dic.items(), key=lambda x: (-x[1], x[0]))

    result = ""
    for i in range(3):
        result += f"{i+1}. \"{dic_sorted[i][0]}\" - {dic_sorted[i][1]}\n"
    return result.rstrip()

def main():
    print(occurrences(sentences))


if __name__ == "__main__":
    main()