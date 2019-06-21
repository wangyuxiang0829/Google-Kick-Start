# Wiggle Walk (6pts, 12pts)

### Problem

Banny has just bought a new programmable robot. Eager to test his coding skills, he has placed the robot in a grid of squares with **R** rows (numbered 1 to **R** from north to south) and **C** columns (numbered 1 to **C** from west to east). The square in row r and column c is denoted (r, c).

Initially the robot starts in the square (**SR**, **SC**). Banny will give the robot **N** instructions. Each instruction is one of `N`, `S`, `E` or `W`, instructing the robot to move one square north, south, east or west respectively.

If the robot moves into a square that it has been in before, the robot will continue moving in the same direction until it reaches a square that it *has not* been in before. Banny will never give the robot an instruction that will cause it to move out of the grid.

Can you help Banny determine which square the robot will finish in, after following the **N** instructions?

### Input

The first line of the input gives the number of test cases, **T**. **T** test cases follow. Each test case starts with a line containing the five integers **N**, **R**, **C**, **SR** and **SC**, the number of instructions, the number of rows, the number of columns, the robot's starting row and starting column, respectively.

Then, another line follows containing a single string of **N** characters; the i-th of these characters is the i-th instruction Banny gives the robot (one of `N`, `S`, `E` or `W`, as described above).

### Output

For each test case, output one line containing `Case #x: r c`, where `x` is the test case number (starting from 1), `r` is the row the robot finishes in and `c` is the column the robot finishes in.

### Limits

Memory limit: 1GB.

$1 \leq \mathrm { T } \leq 100$
$1 \leq \mathrm { R } \leq 5 \times 10 ^ { 4 }$
$1 \leq \mathrm { C } \leq 5 \times 10 ^ { 4 }$
$1 \leq \mathrm { S } _ { \mathrm { R } } \leq \mathrm { R }$
$1 \leq \mathrm { S } _ { \mathrm { C } } \leq \mathrm { C }$

The instructions will not cause the robot to move out of the grid.

#### Test set 1 (Visible)

Time limit: 20 seconds.

$1 \leq \mathrm { N } \leq 100$

#### Test set 2 (Hidden)

Time limit: 60 seconds.

$1 \leq \mathrm { N } \leq 5 \times 10 ^ { 4 }$

### Sample

| Input         | Output         |
| ------------- | -------------- |
| `3`           |                |
| `5 3 6 2 3`   |                |
| `EEWNS`       | `Case #1: 3 2` |
| `4 3 3 1 1`   |                |
| `SESE`        | `Case #2: 3 3` |
| `11 5 8 3 4`  |                |
| `NEESSWWNESE` | `Case #3: 3 7` |

Sample Case #1:

![](D:\10673\Documents\Go-Work-Space\src\github.com\wangyuxiang0829\Google-Kick-Start\Round C 2019 - Kick Start 2019\Wiggle Walk (6pts, 12pts)\Sample Case #1.png)

 Sample Case #2:

![](D:\10673\Documents\Go-Work-Space\src\github.com\wangyuxiang0829\Google-Kick-Start\Round C 2019 - Kick Start 2019\Wiggle Walk (6pts, 12pts)\Sample Case #2.png)

Sample Case #3:

![](D:\10673\Documents\Go-Work-Space\src\github.com\wangyuxiang0829\Google-Kick-Start\Round C 2019 - Kick Start 2019\Wiggle Walk (6pts, 12pts)\Sample Case #3.png)

In each diagram, the yellow square is the square the robot starts in, while the green square is the square the robot finishes in.

### Analysis

#### Test set 1 (Visible)

Approaching the problem naively, one might try to simply simulate what has been mentioned in the problem statement i.e. keep on moving the robot in the specified direction till it reaches an un-visited square. The running time of this approach is going be $T ( n ) = \theta \left( n ^ { 2 } \right)$ in the worst case, which although good enough for test set 1.

#### Test set 2 (Hidden)

The problem with the above approach is that it visits a lot of already visited squares which in worst case will be all the previously visited squares (Consider the input where you are given alternating `E` and `W` throughout). If we somehow get to the destination square for each instruction faster, we might be able to reduce the running time.

Let's say the robot is in some row r and received an instruction `W`. Now, all the already visited squares (if any) it will pass before reaching an unvisited square have to form a contiguous interval in row r. This suggests that we may use intervals to represent all the visited squares in the same row.

With that in mind, consider we have a [set](https://en.wikipedia.org/wiki/Set_(abstract_data_type)) of intervals for each row and each column of the grid to represent which cells have been visited in that particular row or column, let's call them interval-sets. Initially, all these sets are empty except for the set corresponding to row **SR**, which has a single interval (**SC**, **SC**), and the set corresponding to the column **SC**, which has a single interval (**SR**, **SR**).

Now, using this data-structure, let's try to find the destination square for the robot. Let's say it's in square (r, c) and got an instruction `W`. For this, first we search in the interval-set corresponding to row r. We will try to find which interval in this set contains c (there must definitely be one!). Once we find it, we immediately know what's going to be the new position for the robot! It's apparent that the same method works for all other directions as well.

All that remains now is to find a way to update our data-structure suitably to also include the newly visited square. This can be done in a very standard manner by simply finding the adjacent intervals for that square in both, the corresponding column interval-set and the corresponding row interval-set and then updating them either by extending one of the intervals or merging them or adding a new 1 length interval.

Since we add at most one interval in each case, the number of intervals is $O ( n )$. Since all operations are about finding/inserting/removing a single interval, all of those can be handled easily in $O ( \lg n )$ time. So the over all run time of this approach is $O ( n \lg n )$ . There is also a  $O ( n )$ solution to this problem using hash tables. It is left as an exercise to the reader.