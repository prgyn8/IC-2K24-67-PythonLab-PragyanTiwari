# Lab 3 — Star patterns

## 1. Hollow diamond

**Question:** Print a hollow diamond pattern for an odd positive value of `n`.

**Approach:** I built a list of row widths (increase then decrease), found the middle row, and printed stars only at the left and right edges with spaces in between. Leading spaces center each row.

File: `hollow_diamond.py`

## 2. Butterfly pattern

**Question:** Print a butterfly pattern using stars and spaces.

**Approach:** I used two lists for the top and bottom halves of row sizes, then for each row calculated how many stars go on the left and right and how much space sits in the middle.

File: `butterfly.py`
