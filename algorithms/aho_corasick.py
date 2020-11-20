from collections import deque
from typing import List

class Trie:
    def __init__(self, c: str):
        self.val = c
        self.end = False
        self.children = {}

    """
    Populate the trie with word s
    O(n) runtime, O(1) space
    """
    def add(self, s: str):
        runner = self
        for c in s:
            if c not in runner.children:
                runner.children[c] = Trie(c)
            runner = runner.children[c]
        runner.end = True


class AhoCorasick(Trie):
    def __init__(self):
        super().__init__('')
        self.fail_link = self

    """
    Populate fail links of each trie node using Aho-Corasick algorithm
    O(n) runtime and space assuming unbalanced tree
    """
    def add_fail_links(self):
        q = deque()
        for key in self.children:
            q.append((self, self.children[key]))
        while q:
            parent, node = q.popleft()
            if parent == self:
                node.fail_link = parent
            else:
                runner = parent.fail_link
                while node.val not in runner.children and runner.fail_link is not runner:
                    runner = runner.fail_link
                if node.val in runner.children:
                    node.fail_link = runner.children[node.val]
                else:
                    node.fail_link = runner
            for key in node.children:
                q.append((node, node.children[key]))

    """
    Query string s for the patterns contained in the trie
    O(n) runtime and space assuming unbalanced tree
    """
    def query(self, s: str) -> List[str]:
        visited = set()
        runner = self
        for c in s:
            visited.add(runner)
            while c not in runner.children and runner is not self:
                runner = runner.fail_link
            if c in runner.children:
                runner = runner.children[c]
        sol, cur = [], []
        def dfs(node):
            cur.append(node.val)
            if node in visited and node.end:
                sol.append(''.join(cur))
            for key in node.children:
                dfs(node.children[key])
            cur.pop()
        dfs(self)
        return sol

trie = AhoCorasick()
trie.add("acc")
trie.add("atc")
trie.add("cat")
trie.add("gcg")
trie.add_fail_links()
assert trie.query("gcatcg") == ['atc', 'cat']
