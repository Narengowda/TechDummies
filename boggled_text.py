"""
Find all possible words in a board of characters or Boggle
Author: Narendra L
Date: 20-7-2018
"""

from collections import defaultdict
from nltk.corpus import words
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#english_words = words.words()

# If you wan to remove stop words
# stop_words = set(stopwords.words('english'))
# english_words = [w for w in english_words if w not in stop_words]

english_words = ['apple', 'pickle', 'side', 'kick', 'sick', 'mood', 'cat',
                 'cats', 'man', 'super', 'antman', 'godzilla', 'dog', 'dot',
                 'sine', 'cos', 'signal', 'bitcoin', 'cool', 'zapper']

boggle = [
    ['c', 'n', 't', 's', 's'],
    ['d', 'a', 't', 'i', 'n'],
    ['o', 'o', 'm', 'e', 'l'],
    ['s', 'i', 'k', 'n', 'd'],
    ['p', 'i', 'c', 'l', 'e']
]

# Instead of X and Y co-ordinates
# better to use Row and column
lenc = len(boggle[0])
lenr = len(boggle)

# Initialize trie datastructure
trie_node = {'valid': False, 'next': {}}

# lets get the delta to find all the nighbors
neighbors_delta = [
    (-1,-1, "↖"),
    (-1, 0, "↑"),
    (-1, 1, "↗"),
    (0, -1, "←"),
    (0,  1, "→"),
    (1, -1, "↙"),
    (1,  0, "↓"),
    (1,  1, "↘"),
]


def gen_trie(word, node):
    """udpates the trie datastructure using the given word"""
    if not word:
        return

    if word[0] not in node:
        node[word[0]] = {'valid': len(word) == 1, 'next': {}}

    # recursively build trie
    gen_trie(word[1:], node[word[0]])


def build_trie(words, trie):
    """Builds trie data structure from the list of words given"""
    for word in words:
        gen_trie(word, trie)
    return trie


def get_neighbors(r, c):
    """Returns the neighbors for a given co-ordinates"""
    n = []
    for neigh in neighbors_delta:
        new_r = r + neigh[0]
        new_c = c + neigh[1]

        if (new_r >= lenr) or (new_c >= lenc) or (new_r < 0) or (new_c < 0):
            continue
        n.append((new_r, new_c, neigh[2]))
    return n


def dfs(r, c, visited, trie, now_word, direction):
    """Scan the graph using DFS"""
    if (r, c) in visited:
        return

    letter = boggle[r][c]
    visited.append((r, c))

    if letter in trie:
        now_word += letter

        if trie[letter]['valid']:
            print('Found "{}" {}'.format(now_word, direction))

        neighbors = get_neighbors(r, c)
        for n in neighbors:
            dfs(n[0], n[1], visited[::], trie[letter], now_word, direction + " " + n[2])


def main(trie_node):
    """Initiate the search for words in boggle"""
    trie_node = build_trie(english_words, trie_node)

    # print the board
    print("Given board")
    for i in range(lenr):print (boggle[i])
    print ('\n')

    for r in range(lenr):
        for c in range(lenc):
            letter = boggle[r][c]
            dfs(r, c, [], trie_node, '', 'directions from ({},{})({}) go '.format(r, c, letter))


if __name__ == '__main__':
    main(trie_node)

