# Problem Set 4C
# Name: Saeed Entezari

import string
from ps4a import get_permutations
from ps4b import load_words, is_word

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
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
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        assert len(vowels_permutation) == len(VOWELS_LOWER)
        # create substitution dictionary for vowells
        vowel_sub_dict = {VOWELS_LOWER[i]: vowels_permutation[i] for i in range(len(VOWELS_LOWER))}
        vowel_sub_dict.update(
            {VOWELS_UPPER[i]: vowels_permutation[i].upper() for i in range(len(VOWELS_UPPER))}
            )
        # map all letters to their substitute
        letters = list(string.ascii_letters)
        transpose_dict = {}
        for let in letters:
            if let in vowel_sub_dict:
                transpose_dict[let] = vowel_sub_dict[let]
            else:
                transpose_dict[let] = let
        # return transpose dictionary
        return transpose_dict
    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        message_shifted = ''
        for char in self.get_message_text():
            if char in transpose_dict:
                message_shifted += transpose_dict[char]
            else:
                message_shifted += char

        return message_shifted
        
class EncryptedSubMessage(SubMessage):

    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        SubMessage.__init__(self, text)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message.
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        best_nvalids, best_transdict = 0, {}
        # iterate over all possible transpose dictionaries
        for permut in get_permutations('aeiou'):
            transdict = self.build_transpose_dict(permut)
            # decrypt message with this transdict
            decrypted_message = self.apply_transpose(transdict)
            # count the number of valid words regard to this transdict
            nvalids = 0
            for word in decrypted_message.split():
                nvalids += is_word(self.get_valid_words(), word)
            # is this transdict the best so far?
            if nvalids > best_nvalids:
                best_transdict = transdict
                best_nvalids = nvalids

        return self.apply_transpose(best_transdict)



if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())