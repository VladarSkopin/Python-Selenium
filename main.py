# This is a sample Python script.

def string_splosion(str):
    result = ''
    count = 0
    while count < len(str):
        buffer_word = str[0:count + 1]
        result += buffer_word
        count += 1
    return result


if __name__ == '__main__':
    print(string_splosion('Code'))
    print(string_splosion('abc'))
    print(string_splosion('ab'))
