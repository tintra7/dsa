class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.wordEnd = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            index = ord(c) - ord('a')
            if curr.child[index] is None:
                new_node = TrieNode()
                curr.child[index] = new_node
            curr = curr.child[index]
        curr.wordEnd = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            index = ord(c) - ord('a')
            if curr.child[index] is None:
                return False
            curr = curr.child[index]
        return curr.wordEnd

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            index = ord(c) - ord('a')
            if curr.child[index] is None:
                return False
            curr = curr.child[index]
        return True

    def delete(self, word: str) -> bool:
        # Helper function for recursion
        def _delete(node, word, depth):
            if not node:
                return False

            # If end of word is reached
            if depth == len(word):
                # Check if the word exists in the Trie
                if not node.wordEnd:
                    return False

                # Unmark the wordEnd and check if the node can be deleted
                node.wordEnd = False
                return not any(node.child)  # Safe to delete if no children exist

            # Recur for the child corresponding to the next character
            index = ord(word[depth]) - ord('a')
            if _delete(node.child[index], word, depth + 1):
                # If child can be deleted, remove the reference
                node.child[index] = None
                # Return true if the current node is not an end of another word
                # and has no other children
                return not node.wordEnd and not any(node.child)

            return False

        # Start the recursive deletion
        return _delete(self.root, word, 0)

trie = Trie()
print(trie.insert("apple"))
print(trie.search("apple"))
print(trie.delete("apple"))
print(trie.startsWith("app"))