# Binary Search
- multiple decisions can change behavior of code such as
  - do I use left or right or mid?
  - do I use `<` or `<=` or `>` or `>=`?
  - do I shrink boundary to `mid`, `mid-1`, or `mid+1`?
- the boundary is the range of elements inclusive to be searching from
  - if question asks you to search for index to insert a value in an array, then bounds 
    should be [0, arr.length] because you can insert after the last element
- calculating mids can overflow when numbers are big
  - `(lo+hi)//2` easy to overflow
  - `lo+(hi-lo)//2` is better but can still overflow
  - `(lo+hi)>>1` is best
- can pick if you want left-leaning or right-leaning mid of a subarray by calculating 
  mid differently
  - `lo+(hi-lo)//2` gives left-leaning
  - `lo+(hi-lo+1)//2` gives right-leaning
- when shrinking boundary, try to always use logic that you can exclude mid
  - eg:
    ```
    if (target < nums[mid]) {
      hi = mid - 1; // mid is excluded since we know its not our answer
    } else {
      lo = mid; // mid is still possible to be our answer
    }
    ```
  - on the contrary, this means that we can also write the logic as
    ```
    if (target > nums[mid]) {
      lo = mid + 1; // mid is excluded
    } else {
      hi = mid; // mid is included
    }
    ```
- it is best to always set the loop condition to `while(lo < hi)` since there is only 
  one possible exitting condition where `lo == hi`
- a bad choice of left-leaning or right-leaning `mid` can lead to an infinite loop
  - generally, shrinking logic and the direction that `mid` leans has to work together
  - eg. if `mid` leans left, and you are doing `lo = mid`, then this will give you an 
    infinite loop
- if there is an infinite loop in the binary search, consider event with two elements 
  remaining in the subarray
