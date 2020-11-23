# Complexity: P, NP, NP-completeness, Reductions
- source: MIT 6.046J Design and Analysis of Algorithms, Spring 2015
  - https://www.youtube.com/watch?v=mr1FMrwi6Ew

### Theory
- P is problems solvable in polynomial time
- NP is decision problems solvable in non deterministic polynomial time
- in nondeterministic models, you can make a guess out of polynomially many options
  - guess should lead to a YES answer for the problem if possible, if not possible, then the guess will still lead to a NO
  - "if a guess would result in a YES answer, then we get this guess"
  - answer is biased towards YES, biasing towards NO is called co-np
  - "I would really like a result that gives me a YES answer, but if still ends in NO, then there is no possible result that can give you YES
  - you get a lot more information from a NO than a YES
- 3SAT is the most important NP-complete problem
  - given a boolean formula `(not x1 or x3 or not x6) and (not x2 or x3 or not x7)`
  - decision question: can you set the variables such that the formula is `true`?
  - at least one of the left needs to be `true`, and at least one of the right needs to be `true`
  - the problem is hard, there is no polynomial time algorithm to solve it
- there is a polynomial nondeterministic algorithm to solve 3SAT
  - you can guess if x1 is true or false, then same for x2, etc ...
  - we assume each guess operation is O(1)
  - after all variables are guesed, check if forumla is satisfied
  - return the formula satisfiability
  - nondeterministic algorithm is biased towards YES, so it will try to return answers to give you YES
- generally, you do nondeterministic guessing first, then do polynomial time (deterministic) checking to verify the answer and return it
- this essentially makes problems like 3SAT a verification algorithm
  - first given a "solution", check the solution for validity in polynomial time and return yes or no
- using this method, there's only a way to proove YES, but never NO
  - given a solution set, you can only proove there is a solution to 3SAT, but not there ISNT a solution to 3SAT
- this states that while the problem can't be solved in polynomial time, you can still verify it in polynomial time
- NP problems are decision problems with polynomial size certificates and polynomial time verifiers
  - certificates being the solution set to give a YES answer to the problem after polynomial time checking
- problem x is NP-complete if x is in NP, and x is NP hard
- problem x is NP-hard if every problem y in NP reduces to problem x
  - if x is NP-hard, it's at least as hard as every problem in NP
  - if x in NP-hard, it is also not in P, unless P=NP
- NP algorithms have a polynomial time verification algorithm, but NP-hard algorithms dont
- NP-complete sits at the intersection of NP and NP-hard
  - ```
    |--------------NP------------------|------NP-hard----------|
    |------P---------|                 ^ NP-complete
    ```
  - notice that this also shows P is a subset of NP
- P=NP hypothesis implies that computers can engineer luck to compute certificates in polynomial time
  - implies that all non-deterministic algorithms are actually deterministic
- under normal assumptions that P != NP, we know that any NP-hard or NP-complete problem cannot be in P
- reduction from problem A to problem B is a polynomial time algorithm which converts A inputs to equivalent B inputs, where the final answer of both problem A and B remains the same
  - implies that if B has a polynomial time algorithm, A will also have a polynomial time algorithm through reduction to B
  - if B is in P, then A is also in P
  - if B is in NP, then A is also in NP
  - also implies that B is at least as hard as A
- How can we prove that a problem x is NP-complete?
  - used to prove a lower bound on the algorithm, states that the problem is too hard and there's no point in looking for a faster solution than exponential
1. prove that x is in NP
  - give a non-deterministic algorithm for certificates, and run a polynomial time algorithm for verification
2. prove that x in NP-hard, so reduce from some known NP-complete problem to problem x
  - every problem in NP reduces to NP-complete, so if we reduce NP-complete to problem x, we successfully show that all problems in NP also reduce to problem x
- first NP-complete proof was done in 1971, where 3SAT was proved to be NP-complete, through reduction from every NP problem to NP-complete
- every problem can reduce to 3SAT as hardware can implement any software program through boolean equations, boolean equations can all be written in the form of ANDs of series of 3 ORs, which is 3SAT

### Reduce 3SAT to super mario brothers, proving super mario brothers is NP-hard
- given a level, can you prove that the level is completable?
- given 3SAT formula, build super mario level that implements the formula
- mario enters a variable like x1, x2, x3 from 3SAT, and has to fall either to the left(TRUE) or right(FALSE)
- gadgets are features of input algorithm that are converted to inputs of the algorithm being reduced to
- clause gadgets are the clauses in 3SAT
- mario dips all clause gadgets that have the decision variable just made, this satisfies those clauses, he then goes to the next decision variable
- once all decision variables have been visited, he traverses all clause gadgets
  - this is the verification algorithm

### 3-Dimensional Matching
- graph theory problem
- looking for pairs of three
- given disjoint sets X, Y, Z each size n
- given triples T where T is a subset of the cross product of X, Y, Z
  - not all triples are allowed, instead only a subset of them, which is T
- choose amongst a subset S of T where every element (either X or Y or Z) is in exactly one triple
- we know this problem is in NP as we can guess which elements of T are in S, then check if all elements are covered
- we must now prove that the problem is NP-hard through a reduction from 3SAT
- convert variable `xi` to a wheel of points
  - ![wheel](https://i.imgur.com/9YMQM8p.png)
  - you can pick only the red or the blue set, if you mix and match, some points will not be covered
  - this is the variable gadget
- clause gadgets are formed by `xi OR not xj OR xk`
  - ![clause gadget](https://i.imgur.com/vquukkD.png)
  - this can be represented by another set of 3 points, where at least one point needs to be unoccupied
- additional points in the clause gadget that are not used are sent to garbage collection

### Subset Sum
- reduce from 3D matching
- given n integers, `A={a1, a2, a3, .., an}`
- given target sum `t`, is there a subset of the numbers that add up to the target?
- NP problem as you can just guess which numbers would add up to the sum
- also considered weakly NP-hard
- view numbers in base b = 1+max(nxi)
  - this ensures there will never be a carry in the addition
- given triple `(xi, xj, xk)`, convert to `0000100001001000`, where each `1` represents one of `i`, `j`, and `k`
  - this is equivalent to `b^i+b^j+b^k`, where b represents the base of the number
- target sum then becomes `1111111111`
- triplets add together to become the target sum, if there are remaining 0s in the sum, those are matched in clause gadets and/or sent to garbage collection
- however, base-b representation of numbers grow exponentially as more numbers are added
  - strong NP-hardness does not allow for exponential growth of this number, so this problem is actually weakly NP-hard

### Partition
- given n integers, `A={a1, a2, a3, .., an}`, positive
- is there a subset of these integers s such that the sum of s is equal to the subset of integers not in s
  - effectively also means that sum of s is half of the sum of A
- also weakly NP-hard
- to reduce from subset sum, notice that this problem is actually a special case of subset sum, because t=sum(A)/2
- let sigma=sum(A)
- suppose we add together `xn+1=sigma+t` and `xn+2=2sigma-t`

### Rectangle Packing
- given rectangles ri of variant sizes and a target rectangle t, put the rectangles in the big rectangle without any overlap
- weakly NP-complete
- reduction from partition
- from integers in partition, convert them to 1x3ai rectangles
- target rectangle is 2x3t, where t is the sum of the array from partitioning problem
- essentially if we make the big rectangle into two rows that fits smaller rectangles, it becomes a partitioning problem

### Jigsaw Puzzles
- each side of the puzzle can be a tab, a pocket, or a flat
- NP-complete problem
- simulate a rectangle with a set of puzzle pieces
- needs to be reduced by a strong NP-hard problem as jigsaw puzzles aren't represented by numbers
- Reduce from 4-partition problem instead, which is strongly NP-hard

### Strongly NP-hard
#### 4-Partition
- Given integers A, split A into n/4 quadruples of same sum
- Jigsaw puzzle is a strongly NP-hard problem