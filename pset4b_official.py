import string


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
    # True
    # >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'


class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object

        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        # try/except statement in case text passed in is not a string
        try:
            self.message_text = text
        except TypeError:
            print("Must enter valid message")

        # self.valid_words attribute is NOT passed in as a parameter when initializing instance
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


    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.

        shift (integer): the amount by which to shift every letter of the
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to
                 another letter (string).
        '''
        dict = {}
        list_upper = []
        list_lower = []
        # stop the program from running if shift input outside range
        assert 0 <= shift < 27, shift
        # creating a list containing all uppercase letters of the alphabet
        for l in string.ascii_uppercase:
            list_upper.append(l)
        # for each letter, add the shift to its current index num.
        for i, char in enumerate(list_upper):
            index_total = i + shift
            # if the new letter following the shift comes before the end of the alphabet,
            # simply access the new letter via the new index (previous index + shift)
            if index_total <= 25:
                new_upper = list_upper[index_total]
                # add new letter to dictionary as the value associated with the original letter key
                dict[char] = new_upper
            # if the shift change extends beyond the end of the alphabet,
            # must go back to the beginning
            else:
                new_upper = list_upper[index_total - 26]
                dict[char] = new_upper

        # now we repeat the process with lowercase letters
        for n in string.ascii_lowercase:
            list_lower.append(n)
        for i, char in enumerate(list_lower):
            index_total = i + shift
            if index_total <= 25:
                new_lower = list_lower[index_total]
                dict[char] = new_lower
            else:
                new_lower = list_lower[index_total - 26]
                dict[char] = new_lower

        return dict

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift

        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        # initializing cipher message
        cipher = ""
        # calling function that creates dictionary based on input shift
        dict = self.build_shift_dict(shift)
        # iterating through each character of message to be encrypted
        for char in self.message_text:
            # if letter, change to new code letter by accessing dictionary
            if char in dict:
                new_char = dict[char]
                cipher += new_char
            else:
                # if non-letter symbol, leave as is in new cipher message
                cipher += char
        return cipher


class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object

        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''

        # since PlaintextMessage is a subclass of the Message class, I can simply call the 'init'
        # function of the parent class to inherit the following attributes: valid_words & message_text
        Message.__init__(self, text)
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(self.shift)
        self.message_text_encrypted = self.apply_shift(self.shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class

        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class

        Returns: a COPY of self.encryption_dict
        '''
        return self.encryption_dict[:]

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class

        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, newshift):
        '''
        Changes self.shift of the PlaintextMessage and updates other
        attributes determined by shift.

        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        # program stops running if new shift is out of range
        assert 0 <= newshift < 26
        self.shift = newshift
        self.encryption_dict = self.build_shift_dict(newshift)
        self.message_text_encrypted = self.apply_shift(newshift)


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object

        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        # calling 'init' function of Message class to inherit its data attributes
        Message.__init__(self, text)

    def decrypt_message(self):
        '''
        Decrypts self.message_text by trying every possible shift value
        and finding the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create
        the maximum number of valid words, function will return any of those shifts
        (and their corresponding decrypted messages)

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        word_count_dict = {}
        # checking through all shift possibilities to count num valid words each possibility yields
        for s in range(26):
            valid_word_count = 0
            decrypt_attempt = self.apply_shift(26 - s)
            split_message = decrypt_attempt.split()
            for w in split_message:
                if is_word(self.valid_words, w):
                    valid_word_count += 1

            # creating a dictionary to map each shift to valid word count
            word_count_dict[s] = valid_word_count

        # finding max word count from dict
        values = word_count_dict.values()
        best = max(values)

        # using dict to get best shift value & final message reveal
        for shift in word_count_dict:
            if word_count_dict[shift] == best:
                best_shift_value = 26 - shift
                revealed_message = self.apply_shift(best_shift_value)
                break

        return (best_shift_value, revealed_message)


if __name__ == '__main__':
#Below are cases to test if I can properly encrypt and decrypt messages using my program
#Test it out! you will see that the 'Expected Output' matches the 'Actual Output' in each case
# ********************************************************************************************

    # Test case 1 (PlaintextMessage)
    # plaintext = PlaintextMessage('ask', 3)
    # print('Expected Output: dvn')
    # print('Actual Output:', plaintext.get_message_text_encrypted())

    # # Test case 2 (PlaintextMessage)
    # plaintext = PlaintextMessage('I don\'t', 2)
    # print("Expected Output: K fqp\'v")
    # print('Actual Output:', plaintext.get_message_text_encrypted())
    #
    # #Test case 1 (CiphertextMessage)
    # ciphertext = CiphertextMessage('dvn')
    # print('Expected Output:', (23, 'ask'))
    # print('Actual Output:', ciphertext.decrypt_message())
    #
    # # Test case 2 (CiphertextMessage)
    # ciphertext = CiphertextMessage('K gcv ucnv')
    # print('Expected Output:', (24, 'I eat salt'))
    # print('Actual Output:', ciphertext.decrypt_message())

    # (12, 'Jack Florey is a mythical character created on the spur of a moment to help cover an insufficiently planned hack. He has been registered for classes at MIT twice before, but has reportedly never passed aclass. It has been the tradition of the residents of East Campus to become Jack Florey for a few nights each year to educate incoming students in the ways, means, and ethics of hacking.')

# Uncomment the lines below. Output should match text above!
    # story = CiphertextMessage(get_story_string())
    # print(story.decrypt_message())

