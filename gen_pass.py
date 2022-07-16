import random
import sys
import string

chars_to_be_removed = '10IOloqv'
translation_table = str.maketrans('', '', chars_to_be_removed)
charset = string.ascii_letters + string.digits
charset = charset.translate(translation_table)

if __name__ == "__main__":

    try:
        length = int(sys.argv[1])
    except Exception as e:
        print("Please enter the length of password. Error: ", e)

    print("length: " + str(length))
    pass_phrase = ''.join(random.choice(charset) for i in range(length))
    print("password: " + pass_phrase)