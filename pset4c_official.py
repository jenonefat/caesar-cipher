import string
from permutations import get_permutations


### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''

    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    # >>> is_word(word_list, 'bat') returns
    True
    # >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### END HELPER CODE ###


WORDLIST_FILENAME = 'words.txt'


VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'


class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object

        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class

        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.

        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]

    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)

        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled
        according to vowels_permutation. The first letter in vowels_permutation
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary has 52
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to
                 another letter (string).
        '''
        # interrupts program if incorrect number of letters passed in
        assert len(vowels_permutation) == 5, 'wrong input length, must be 5 vowels'

        # creating dictionary and adding consonants
        transpose_dict = {}
        for l in CONSONANTS_UPPER:
            transpose_dict[l] = l
        for c in CONSONANTS_LOWER:
            transpose_dict[c] = c

        # simultaneously iterate through 'aeiou' & lowercase permutation of vowels passed in
        # map as key-value pairs in dictionary
        for (char1, char2) in zip(VOWELS_LOWER, vowels_permutation):
            transpose_dict[char1] = char2.lower()
        # repeat process for uppercase vowels
        for (char1, char2) in zip(VOWELS_UPPER, vowels_permutation):
            transpose_dict[char1] = char2.upper()

        return transpose_dict

    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary

        Returns: an encrypted version of the message text, based
        on the dictionary
        '''
        # initializing cipher message
        cipher = ''
        # iterating through each character in message text
        for char in self.message_text:
            # if char is a letter, access corresponding value in dict
            if char in transpose_dict:
                new_char = transpose_dict[char]
                # add value to cipher message
                cipher += new_char
            # if char is not a letter, add the same char to cipher message
            else:
                cipher += char
        return cipher


class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        # EncryptedSubMessage is a child class of SubMessage
        # call SubMessage 'init' function to inherit message_text & valid_words attributes
        SubMessage.__init__(self, text)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message

        Goes through each permutation of the vowels and tests it
        on the encrypted message. For each permutation, checks how many
        words in the decrypted text are valid English words, and returns
        the decrypted message with the most English words.

        If no good permutations are found (i.e. no permutations result in
        at least 1 valid word), returns the original string. If there are
        multiple permutations that yield the maximum number of words, returns any
        one of them.

        Returns: the best decrypted message

        '''
        word_count_dict = {}
        # function is imported from 'permutations.py' file
        permutations = get_permutations(VOWELS_LOWER)
        # for each possible vowel permutation....
        for perm in permutations:
            word_count = 0
            # create dictionary & use it on encryption to make a decryption attempt
            trans_dict = self.build_transpose_dict(perm)
            decrypt_attempt = self.apply_transpose(trans_dict)
            # convert decryption attempt message into a list
            split_message = decrypt_attempt.split()

            # counting number of valid words in decryption attempt
            for w in split_message:
                if is_word(self.valid_words, w):
                    word_count += 1

            # adding permutation and its corresponding valid word count to new dict
            word_count_dict[perm] = word_count

        # after iterating through all possible permutations,
        # search for highest valid word count
        values = word_count_dict.values()
        best = max(values)

        # return original message if none of the decryption attempts yielded a single valid word
        if best == 0:
            message_reveal = self.get_message_text()
        else:
            # finding the permutation associated with the highest valid word count,
            # applying this permutation to reveal the decrypted message
            for perm in word_count_dict:
                if word_count_dict[perm] == best:
                    message_reveal = self.apply_transpose(self.build_transpose_dict(perm))
                    break

        return message_reveal




if __name__ == '__main__':
# Uncomment the appropriate lines below to test out the SubMessage and EncryptedSubMessage functions

    #SubMessage test case 1
    # message_1 = SubMessage("Eat More Vegetables!!")
    # permutation = "iueoa"
    # enc_dict_1 = message_1.build_transpose_dict(permutation)
    # print(f"Original message:{message_1.get_message_text()}, Permutation: {permutation}")
    # print("Expected encryption: Uit Moru Vugutiblus!!")
    # print(f"Actual encryption: {message_1.apply_transpose(enc_dict_1)}")

    #SubMessage test case 2
    # message_2 = SubMessage("About ME.....")
    # permutation = "OUIAE"
    # enc_dict_2 = message_2.build_transpose_dict(permutation)
    # print(f"Original Message: {message_2.get_message_text()}, Permutation: {permutation}")
    # print("Expected Encryption: Obaet MU....")
    # print(f"Actual Encryption: {message_2.apply_transpose(enc_dict_2)}")

    #EncryptedSubMessage test case 1
    # encrypted_message = EncryptedSubMessage(message_1.apply_transpose(enc_dict_1))
    # decrypted_message = encrypted_message.decrypt_message()
    # print(f"Decrypted Message: {decrypted_message}")

    #EncryptedSubMessage test case 2
    # coded_message = EncryptedSubMessage(message_2.apply_transpose(enc_dict_2))
    # print(f"Decrypted Message: {coded_message.decrypt_message()}")