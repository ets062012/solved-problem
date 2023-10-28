def swap_case(s):
    stri=""
    for i in s:
        if i.isupper():
            i=i.lower()
        else:
            i=i.upper()
        stri+=i
    return stri

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)