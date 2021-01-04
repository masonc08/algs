# Dynamic Programming

- source: MIT 6.006 Introduction to Algorithms, Fall 2011
- I: https://www.youtube.com/watch?v=OQ5jsbhAv_M
- II: https://www.youtube.com/watch?v=ENyox7kNKeY
- III: https://www.youtube.com/watch?v=ocZMDMZwhCY
- IV: https://www.youtube.com/watch?v=tp4_UXaVyx8

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

- note that this does not tell you which words to pack on which line
- to get this information, we need to use parent pointers, which is a concept that applies to all DP problems
- parent pointers tell you which choice was the best one
- when computing guesses, the j that came out to be the smallest badness factor is called the argmin
- store `parent[i] = argmin(...) = best j value for i` inside of DP memo/table
- trace back on this table to see what the best decision was
- `0 -> parent[0] -> parent[parent[0]]...`

## Blackjack
- there is a dealer and a player, the dealer's strategy is completely deterministic, but the player must optimize
- A is either 1 or 11, so A+7 is either 8 or 18
- player can either pick another card or not
- player wants to beat dealer's card values

### Perfect information blackjack
- with perfect information, suppose you know the entire deck
- on each case, do you hit or do you stand?
- deck is n cards, `c0, c1, ..., cn-1`
- you are 1 player vs dealer
- $1 bet per hand
1. subproblems:
- where do you start the new hand? (card suffixes)
- n subproblems, as there's n different suffixes
2. guess:
- do you want to hit or stand, given a card
- In the first hand, how many times should I hit?
- number of choices is at most n
3. recurrence:
outcome of a play is either -1, 0, 1
`BJ(i) = max(outcome(i) + BJ(j) for j in range(i+4, n) if it's a valid play)`
![example](https://i.imgur.com/7N7nyfM.png)
- O(n^2) runtime as there are n subproblems, and making n guesses on each subproblem

## How do we pick a good subrpoblem for strings and sequences?
- previously used suffixes, x[i:] for all i
  - good if you're plucking off the beginning of a sequence or string
- however, sometimes prefixes can also be more convenient, which is similar to suffixes
- we can also pick substrings x[i:j] for all i <= j
  - nC2, n^2 substrings

## parenthesization:
- given associative expression, and want to evaluate it in some order which is optimal
- `A0*A1*A2*...*An-1`, want to compute product of these matrices
- you can pick where the parenthesis are to multiply two matrices
- some parenthesis setups are actually cheaper to compute than others 
- find out which is best
- consider a `column vct * row vct * col vct`, you can do `(column vct * row vct) * col vct` or `column vct * (row vct * col vct)`
- the second setup is cheaper as don't have to create a maxtrix in the middle
![example](https://i.imgur.com/mOpixMX.png)
1. subproblem: optimal evaluation of Ai...Aj-1
- O(n^2) subproblems
2. guess:
- guess the outermost operation
- (A0...Ak-1)*(Ak...Aj-1), guess where this split is
- this gives us O(j-i+1) = O(n) choices
3. recurrence
- `DP(i, j) = min(DP(i, k)+DP(k+j)+cost(Ai:k, Ak:j) for k in range(i+1, j))`
- time per subproblem is O(n)
4. time = O(n^3)
- topological order:
  - for suffixes, topological orders are right to left, other way around for prefixes
  - but what about in this case for substrings?
  - work in increasing substring size, notice that this also applies for suffixes and prefixes
  - longest substring sits at the top, largest number of substrings sits in the middle, smallest substrings sit at the bottom
  - much more difficult to model as each node depends on two other subproblems
  ![example](https://i.imgur.com/EAuoyCH.png)
  - note that DP is not the shortest path in the DAG
5. solve DP(0, n)

## Edit distance:
- given two strings x and y, what is the cheapest possible sequence of character edits to turn x to y?
  - allowed insert a character, delete a character, replace a character
- consider associating costs with replacing character to create an algorithm used for typo correction
- longest common subsequence problem also falls into this category, where cost of insert/delete is 1, and cost of replacing is 0 if c=c', infinite otherwise 
- HIEROGLYPHOLOGY vs. MICHAELANGELO
- what is the longest common subsequence between these two strings?
  - HELLO is the common subsequence
- look at suffixes of x and y
1. subproblem: edit distance on x[i:] and y[j:]
- number of subproblems is n^2, which we need to consider every combination of every suffix size of strings x and y
2. guess:
- given x[i:] and y[j:], convert x to y
- look at very first character, you can either replace, add, or remove it
- specifically:
  - replace x[i] -> y[j], insert y[j], delete x[i]
3. recurrence, which is a max of the three options
```
DP(i, j) = min(
    cost(x[i] -> y[j]) + DP(i+1, j+1),
    cost(add y[j]) + DP(i, j+1),
    cost(del x[i], DP(i+1, j))
)
```
4. topological order, since this is two suffixes, we are going from x to 0, y to 0 (right to left)
```
for i = len(x), ... , 0:
  for j = len(y), ..., 0:
    pass
```
- think of this as a matrix of m=x, n=y, where each cell in the matrix is a subproblem
- each subproblem depends on 3 adjacent cells
![example](https://i.imgur.com/rBY2W5n.png)
5. we want to solve DP(0, 0)

- overall, running time per subproblem is O(1) since there's only 3 choices, making overall running time O(x*y)
- you can improve to linear space by using a DP table, but can't control this with recursion

## Knapsack problem
- given list of items, int size `s_i`, value `v_i`
- knapsack of size `S`
- choose a subset of the items with total size less than `S` that maximizes sum of values
1. subproblem:
- use suffixes i: of items
2. guessing:
- decide on whether you want to take the `i`th item or not
3. recurrence:
- incorrectly, you can try `DP(i) = max(DP(i+1), DP(i+1)+vi)`, but this is wrong as you can't keep track of capacity currently in the bag (there's no S in this formula)
- to fix this problem, give the subproblem more information
  - add the remaining capacity to each subproblem
  - this gives us O(n*S) subproblems
- so instead, use `DP(i, s) = max(DP(i+1, s), DP(i+1, s-si)+vi)`
- total running time: O(n*S), this is NOT polynomial time!
  - by definition, polynomial time is with respect to n, which n is size of the input
  - this algorithm is instead pseudopolynomial time, as it is exponential with respect to O(nlgS), where S is the bit representation of each weight number
  - pseudopolynomial time means that the solution is polynomial in n and the numbers within the input
  - inbetween polynomial and exponential time

## 2 kind of guesing
- there's a different way to guess than the classical approach done so far
- done in step 2 and 3 of the DP process
- in step 2 and step 3, you guess which subproblem to use to solve the bigger subproblem at hand
- in step 1, when you define the subproblems, you can add more subproblems to guess or remember more features of the solution
- did this in knapsacking problem by adding a parameter to the DP, which was the current carried weight, this multiplied each previum subproblem to S more versions of itself, giving a total of n*S subproblems
  - in this approach, we "remember" more about the past

## Piano/Guitar fingering
- given a music piece, which finger should be used to play which note, to give the eaiest transition?
- find fingering for each note
- fingers are 1, ... F, one to five
- difficulty measure d(note p, on finger f, transition to note q, using finger g)
1. subproblems = suffixes, how to play notes[i:] with finger f
2. guess which finger to use for note i from finger f
3. write a recurrence
```
DP(i,f)=min(DP(i+1)+d(i, f, i+1, g) for g in 1, ..., f)
```
4. topological order:
- move from right to left in notes, then from 1 to F for all fingers:
```python
for i in reversed(range(n)):
    for f in 1, ..., F:
        pass
```
5. original problem:
- notice that we dont know what finger to give to the original problem, we we must try all choices
- `min(DP(0, f) for f in 1, ..., F)`

- consider a DAG for this problem:
- it is a complete bipart ite graph, where each subproblem chooses all 5 next finger transitons
![example](https://i.imgur.com/gO7zFcG.png)

- O(n*F^2) overall runtime
- if we wanted to generalize finger to fingers F and strings S, we can adjust the algorithm to give final runtime of O(nF^2S^2)

## Tetris training:
- given sequence of n pieces, must drop from top, only rotating before dropping
- full rows dont clear
- width of board w is small
- board is initially empty
- can you survive?
1. subproblems
- suffix pieces of [i:]
- we also need to know what the skyline of the problem is
- (h+1)^w possible different skylines, making n(h^1)^w total subproblemms
2. guess how to play each pieces, making 4*w choices, 4 rotations and w location to place each pieces
- gives a total runtime of `O(n*w*(h+1)^w)`

## Super Mario Brothers
- given a level with small w*h screen
### configurations
- think about all the configurations, which is everything on the screen, which is c^(w*h)
- theres a constant c nmber of choices for every pixel on the screen
- mario's velocity
- time, with max time T
- score, with max score S
- where the screen is relative to the level, max width of W
- this makes the maximum confirmations a producct of all configurations
