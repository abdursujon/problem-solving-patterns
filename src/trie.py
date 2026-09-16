'''
A Trie, also known as a prefix tree, is a tree-like data structure used to store a dynamic set of strings, where the keys are usually strings. It is particularly useful for retrieval of a key in a dataset of strings, which makes it highly efficient for solving word-based problems.
Usage
    • Autocomplete: Ideal for implementing autocomplete functionality in search engines or text editors.
    • Spell Checker: Useful for building spell checkers in word processors.
    • IP Routing: Used in IP routing to store and search routes.
Pros and Cons
    • Pros:
        ◦ Efficiency: Provides fast retrieval of strings and is more efficient than hash tables or sets when it comes to string keys.
        ◦ Prefix Searching: Excellent for problems that require prefix searching or matching.
    • Cons:
        ◦ Space Overhead: Can use more space compared to other data structures when the dataset is sparse.
        ◦ Complexity: Implementation can be complex, especially when handling deletion of words from the Trie.
Example Problems from Grokking the Coding Interview
    1. Insert into and Search in a Trie: Implement insertion and search in a Trie.
    2. Longest Common Prefix: Find the longest common prefix of a set of strings.
    3. Word Search: Given a 2D board and a word, find if the word exists in the grid.
'''    