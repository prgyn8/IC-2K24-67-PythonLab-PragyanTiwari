# Lab 7 — Time and space complexity

For each snippet, find **time** and **space** complexity in Big-O notation and justify in one line.

Full answers are in `time complexity assignment.docx`.

---

## Snippet 1 — `find_max`

**Question:** Find the maximum value in an array.

**Approach:** One loop over all elements → **O(n)** time. Only `max_val` and `i` → **O(1)** space.

## Snippet 2 — `has_duplicate`

**Question:** Check if the array has any duplicate pair.

**Approach:** Nested loops compare every pair → **O(n²)** time. Fixed loop variables → **O(1)** space.

## Snippet 3 — `sum_digits`

**Question:** Sum digits of `n` using recursion.

**Approach:** `n` is divided by 10 each call → **O(log₁₀ n)** time and call-stack space.

## Snippet 4 — `print_pairs`

**Question:** Build every ordered pair from the array.

**Approach:** Double loop over `n` → **O(n²)** time. `result` holds `n²` pairs → **O(n²)** space.

## Snippet 5 — `binary_search`

**Question:** Search a sorted array for `target`.

**Approach:** Range halves each step → **O(log₂ n)** time. Only `low`, `high`, `mid` → **O(1)** space.

## Snippet 6 — `matrix_multiply`

**Question:** Multiply two `n × n` matrices.

**Approach:** Three nested loops → **O(n³)** time. Output matrix has **n²** cells → **O(n²)** space.

## Snippet 7 — `to_sparse`

**Question:** Store non-zero cells of a matrix as `(row, col, value)` triples.

**Approach:** Visit every cell → **O(m × n)** time. Store **k** non-zeros → **O(k)** space.

## Snippet 8 — `process`

**Question:** Print each element, then print all pairs.

**Approach:** One loop over `n`, then a double loop that prints **n²** pairs → **O(n³)** time (as in my assignment write-up).

## Snippet 9 — `check_first_ten`

**Question:** See if any array value equals an integer from 0 to 9.

**Approach:** Outer loop **n**, inner loop fixed at 10 → **O(n)** time.

## Snippet 10 — `reverse_new`

**Question:** Return a new reversed list.

**Approach:** Loop **n** times and build a list of size **n** → **O(n)** time and **O(n)** space.

## Snippet 11 — `reverse_in_place`

**Question:** Reverse the list by swapping from both ends.

**Approach:** About **n/2** swaps → **O(n)** time. Two pointers only → **O(1)** extra space.

## Snippet 12 — `factorial`

**Question:** Compute `n!` recursively.

**Approach:** **n** recursive calls → **O(n)** time and **O(n)** stack space.

## Snippet 13 — `fibonacci`

**Question:** Naive recursive Fibonacci.

**Approach:** Each call branches twice → **O(2ⁿ)** time. Depth **n** → **O(n)** stack space.

## Snippet 14 — `count_pairs_with_sum`

**Question:** Count pairs that sum to `target` using a set.

**Approach:** One pass; set lookup/add average **O(1)** → **O(n)** time and **O(n)** space.

## Snippet 15 — `print_all_subsets`

**Question:** Print every subset using bit masks.

**Approach:** **2ⁿ** subsets, **n** bits checked each → **O(n × 2ⁿ)** time.

## Snippet 16 — `merge_sorted`

**Question:** Merge two sorted lists.

**Approach:** Each of **n + m** elements moved once → **O(n + m)** time and space for `result`.

## Snippet 17 — `is_palindrome`

**Question:** Check if a string is a palindrome.

**Approach:** Reversed copy and compare length **n** → **O(n)** time and **O(n)** space.

## Snippet 18 — `flatten`

**Question:** Flatten a 2D matrix to a 1D list.

**Approach:** Visit every cell once → **O(m × n)** time and space.

## Snippet 19 — `power`

**Question:** `base^exp` by repeated multiplication in recursion.

**Approach:** **exp** calls → **O(exp)** time and stack space.

## Snippet 20 — `fast_power`

**Question:** `base^exp` with divide-and-conquer.

**Approach:** `exp` halved each call → **O(log exp)** time and stack space.

## Snippet 21 — `has_common_element`

**Question:** Check if two lists share any value.

**Approach:** Nested loops over sizes **n** and **m** → **O(n × m)** time, **O(1)** extra space.

## Snippet 22 — `build_frequency_map`

**Question:** Count how many times each value appears.

**Approach:** One loop over **n** items → **O(n)** time; dict holds up to **n** keys → **O(n)** space.
