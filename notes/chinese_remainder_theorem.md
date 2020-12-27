# Chinese Remainder Theorem
- Source: https://www.youtube.com/watch?v=ru7mWZJlRQg
- Used to compute x, which is a variable in a system of equations
- Eg:
    - x%3=2
    - x%7=1
    - x%8=6
- Modulo number must all have a GCD of 1 for there to be a solution to x
- If there are n equations in the system, x can be composed as a summation of n numbers
    - in the example above, x would be a summation of 3 terms, as there are three equations to be satisfied
- each term contains the product of all modulos in the system of equations, asides from a different one every time
    - in the example above, `x = 7*2*c1 + 3*8*c2 + 3*7*c3`, where the values of `cn` are to be explained later on
    - notice that the first term corresponds to the product of all modulo asides from the first, second term applies to second modulo, etc
- for each term the current distribution of x, take the corresponding mod, and multiply the number such that is satisfies the corresponding equation
    - considering the first segment of `x`, being `7*2`, we mod it by `3`, extracted from the first equation in the system (`x%3=2`)
    - `7*2=14`, `14%3=2`, this term already satisfies the first condition by coincidence, so `c1=1`, we can move on to the next term
    - `3*8=24`, `24%7=3`, we must find a constant `c2` to multiply `3` by such that it satisfies the respective equation `x%7=1` from our system
    - through trial and error we see that `c2=5`, `3*5=15`, `15%7=1`
    - we substitute the value for `c2` into the equation for `x`
    - repeating the above steps, we solve for `c3`, which happens to be `6`
- in conclusion, we have `x = 7*8*1 + 3*8*5 + 3*7*6`, which is equal to `302`
- every multiple of the product of modulos satisfies the system of equations, so if we want the smallest number, we can perform `302%(3*7*8)=134`, or `x%prod`
    - for the example above, we conclude that the smallest value of x to satisfy the system of equations is `134`