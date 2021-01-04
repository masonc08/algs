# Dynamic Programming

- source: https://www.youtube.com/watch?v=OQ5jsbhAv_M
- https://www.youtube.com/watch?v=ENyox7kNKeY

- dp can be considered as careful brute force, guessing + recursion + memoization + shortest path in some DAG
- subproblem dependencies must be acylic to apply DP or memoization
- bottom up DP algorithms require a topological sort of subproblem dependency dag, and it processes them in this order, as each subproblem can be processed free of missing dependencies
- running time of DP is always `# of subproblems * time per subproblem`
### so how do we convert a cyclic graph to an acyclic graph so we can use dp?
- convert graphs to k duplicate layers, one layer for each node in the graph
- each node's edge goes into the respective vertice in the layer below
![example](https://i.imgur.com/6wso6ft.png)
- this automatically makes any graph acyclic
- define a new shortest path from s to v using at most k edges as `delta_k(s, v)`
- by this definition, the shortest path from u to v using k edges becomes `shortest path from s to u using k-1 edges + weight from u to v`
- this makes subproblems acyclic, but increases the number of subproblems to v^2 as there is now a 2D grid of subproblems

## 5 steps to dp
- not dependent and sequential steps
1. define subproblems
2. guess (part of solution)
3. relate subproblem solutions using recurrence
4. recurse and memoize, or build DP table bottom-up. generally tables are more practical and faster, but usually will have same running time
5. solve the original problem

- typically the number of guesses and the time to combine subproblems will be the same, but there are exceptions
- ensure subproblems can be topologically sorted, if they are not, introduce a new dimension into the dp problem to break up cycles
- sometimes, combining solutions to get final answer may not take constant time

## text justification
- split text into "good" lines
- given text as a list of words, and a function badness(i, j)
- badness function returns how bad it is to use words [i:j) as one line
- if badness = inf, the words dont fit in a line
- otherwise, badness = (page width - total width)^3
- highly discourage big gaps
- in a greedy approach, you make every line as good as they can be with given words, but with DP you consider if it's better to leave some space on lines so the later lines are better
1. define subproblems!
- could be the hard part, as it's not always obvious what the subproblems is
- think about the brute force strategies first: which is to try to split on every word, with 2^n possibilities, of whether you should split at a word or not
- We would like to know where the lines begin, or where to split words
- subproblems are suffixes of the original list of words, so on the first level there's n subproblems
2. guess
- guess how long the first line is, guess where the second line begins
- try all possible words after the first word, until you can't pack any more words into the first line
- set up subproblems so that after you create guesses, there is a subproblem that is similar to the original type
- guess where to break and start the second line
- number of choices for the guess is at most n choices
3. recurrence
- for subproblem starting at word i and trying to pack up to all n words...
- call a recursion, and take min of all guesses, with added on badness of current selection of words packed
- base case: DP(n) = 0, where there is no cost for a line with no words
```python
for j in range(i+1, n+1):
    min(f(j)+badness(i, j), prev)
```
- O(n) operation, as we assume recursive call is free
4. check for a topological oder for this subproblem
- i = n, n-1, ..., 0: this is a linear order, obviously there are no loops
- total time is O(n^2) as each recursive call makes up to n guesses
5. original problem to be solved is DP(0)
