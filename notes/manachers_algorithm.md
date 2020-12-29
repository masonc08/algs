# Manacher's Algorithm

- source: https://cp-algorithms.com/string/manacher.html

- used to compute number of palindromic substrings within a string S in linear time
- uses trivial algorithm to compute base palindromes, but uses cached data in the future for other palindromic substrings
- keep indexes [i, j] to identify a range where there has been a palindrome
- first run the trivial palindromic substring algorithm to detect a palindromic substring range of [i, j]
- when we try to detect any palindromes centered around an index in the interval [i, j], say around index k, we can reuse the data from the mirror of index k in the palindrome
- if index `i+j-k` (mirror of index k in the palindrome) has 3 palindromic substrings centered around it, index k also has AT LEAST 3 palindromic substrings centered around it
- However, if k has a palindrome that can expand outside of the outer palindrome borders, in which case we must continue to run our trivial algorithm
- update the [i, j] range after every iteration
- compute odd and even palindromes separately in two passes

```cpp
vector<int> d1(n);
for (int i = 0, l = 0, r = -1; i < n; i++) {
    int k = (i > r) ? 1 : min(d1[l + r - i], r - i + 1);
    while (0 <= i - k && i + k < n && s[i - k] == s[i + k]) {
        k++;
    }
    d1[i] = k--;
    if (i + k > r) {
        l = i - k;
        r = i + k;
    }
}

vector<int> d2(n);
for (int i = 0, l = 0, r = -1; i < n; i++) {
    int k = (i > r) ? 0 : min(d2[l + r - i + 1], r - i + 1);
    while (0 <= i - k - 1 && i + k < n && s[i - k - 1] == s[i + k]) {
        k++;
    }
    d2[i] = k--;
    if (i + k > r) {
        l = i - k - 1;
        r = i + k ;
    }
}
```