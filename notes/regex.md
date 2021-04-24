# Regex

## Source
https://www.youtube.com/watch?v=sa-TUpSx1JA

- there are metacharacters that need to be escaped, such as `.[{()\^$|?*+`
  - escape characters with `\`

## Literals
- `.` matches any character that is not a new line
- `\d` matches any digit in the range of 0-9
  - `\D` matches anything that is not a digit from 0-9
- generally, upper case negate searches
- `\w` matches a word character, which is a-z, A-Z, 0-9, or _
  - `\W` matches anything that isn't a word character as defined above
- `\s` matches any whitespaces, such as spaces, tabs, newlines
  - `\S` matches anything that isn't a whitespace

## Anchors
- Anchors match positions before and after a character, but dont match a literal character
- `\b` is an anchor to match a word boundary
  - `\B` is an anchor to match not a word boundary
  - `\bHello\b` matches `Hello` in `A Hello A`
- `^` matches to the start of a line, `$` matches to the end of a line

## Character Sets, []
- `[]` is a character set, put in characters that you want to match
- `[-.c]` matches one of either `-`, `.`, or `c`
- no need to escape anything inside character sets
- `-` specifies a range of values, numbers of characters, `[1-7]`, `[a-z]`, `[A-Z]`
  - can be used in combination `[0-9a-zA-Z]`
- `^` negates inside a character set
  - `[^a-z]` matches anything that's not `a-z`

## Quantifiers
- `P{n}` matches for `n` of the pattern `P`
- `P{a, b}` matches for a to b number of occurences of the pattern `P`
- `P?` is an optional match for pattern `P`; it can be there or not
  - "0 or one"
- `P*` matches 0 or more of the pattern `P`
- `P+` matches 1 or more of the pattern `P`

## Groups
- `()` is a group, it allow us to match many different patterns
- group can specify different matches
- groups require special characters to be escaped
- `(abc|def|ghi)` matches one of either `abc`, `def`, or `ghi`
- similar to character sets but matches groups of regex expressions instead of just one matcher
### Returning Groups
- groups are id'ed by the order that they appear in
  - the 0-th group is the entire match, the first group is the first occuring group in the pattern, etc
  - these group numbers can be passed into the application calling the regex
