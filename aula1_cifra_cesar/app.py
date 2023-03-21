

alphabet = 'abcdefghijklmnopqrstuvwyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWYZÀÁÃÂÉÊÓÕÍÚÇ'
non_alphabet = ["."," ",","]

def ceasar(message, key=1, mode='e'):

    string_validate(message)

    def __index_rotation(position):
        alphabet_positions = len(alphabet)

        if position >= alphabet_positions:
            return position - alphabet_positions
        elif position < 0:
            return position + alphabet_positions
        else:
            return position
        
    def __index_generate():
        converted_msg = ''
        for c in message:

            if c in non_alphabet:
                converted_msg = converted_msg + c
            else:
                pass
                c_index = alphabet.find(c)

                if mode == 'e':
                    new_index = c_index + key
                elif mode == 'd':
                    new_index = c_index - key

                new_position = __index_rotation(new_index)
                converted_msg = converted_msg + alphabet[new_position] 
# uftuf eb uftub
        return converted_msg

    def __encrypt():
        return __index_generate()
    def __decrypt():
        return __index_generate()

    if mode == 'e':
        return __encrypt()
    elif mode == 'd':
        return __decrypt()


def string_validate(message):
    for c in message:
        c_index = alphabet.find(c)
        if c_index == -1 and c not in non_alphabet:
            print(f"Character: {alphabet[c_index]} invalid!")
            # return 1
            raise("Invalid character!")
    return message

mode = input("[e] To encrypt and [d] To decrypt:\n")
phrase = input("Text to be converted:")

print(ceasar(phrase, mode=mode))