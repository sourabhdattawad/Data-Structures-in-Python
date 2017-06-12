from collections import defaultdict

class Trie:
    """
    Implement a trie with insert, search, and startsWith methods.
    """
    def __init__(self):
        self.root = defaultdict()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        print self.root
        
        current = self.root
        for letter in word:
            #{'a':{'b':{}}}
            current = current.setdefault(letter, {})
            print self.root
        
        current.setdefault("_end")
        print self.root

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                return False
            current = current[letter]
        if "_end" in current:
            return True
        return False

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        current = self.root
        for letter in prefix:
            if letter not in current:
                return False
            current = current[letter]
        return True

# Now test the class

test = Trie()
test.insert('helloworld')
# test.insert('ilikeapple')
test.insert('helloz')

# print test.search('hello')
# print test.startsWith('hello')
# print test.search('ilikeapple')
