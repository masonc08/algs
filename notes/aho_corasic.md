# Aho-Corasick
- Regular trie with failure links by suffix-prefix relationships, similar to KMP dictionaries
- Used for matching a set of patterns against a string
- Trie holds a set of patterns, as expected
- Failure links link a node's longest suffix to somewhere else in the trie where that same suffix exists as a prefix
  - suffixes can be the 1 less than the length of the pattern, up to an empty string
  - In the worst case, there will be at least one failure link, being an empty string if nothing else was matched
- can identify all matching patterns by traversing master string while following trie, resorting to failure links where required
  - mark down when traversed to end of trie, as that is where a pattern is matched
