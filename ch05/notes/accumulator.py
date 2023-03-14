## main()
# Programming Pattern 
# for -- programming pattern
# accumulator pattern
# accumulator = start_value
# for i in list:
#   accumulator

def remove_vowels(string):
    vowels = "aeiou"
    vowels += vowels.upper()
    result = ""
    for ch in string: 
        if ch not in vowels:
            result += ch
    return result

def main():
    mystring = "Hello World"
    print(remove_vowels(mystring))
    print(mystring)
main()