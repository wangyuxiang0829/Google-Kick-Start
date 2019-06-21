## Training (7pts, 13pts)

### Problem

As the football coach at your local school, you have been tasked with picking a team of exactly **P** students to represent your school. There are **N** students for you to pick from. The i-th student has a *skill rating* **Si**, which is a positive integer indicating how skilled they are.

You have decided that a team is *fair* if it has exactly **P** students on it and they all have the same skill rating. That way, everyone plays as a team. Initially, it might not be possible to pick a fair team, so you will give some of the students one-on-one coaching. It takes one hour of coaching to increase the skill rating of any student by 1.

The competition season is starting very soon (in fact, the first match has already started!), so you'd like to find the minimum number of hours of coaching you need to give before you are able to pick a fair team.

### Input

The first line of the input gives the number of test cases, **T**. **T** test cases follow. Each test case starts with a line containing the two integers **N** and **P**, the number of students and the number of students you need to pick, respectively. Then, another line follows containing **N** integers **Si**; the i-th of these is the skill of the i-th student.

### Output

For each test case, output one line containing `Case #x: y`, where `x` is the test case number (starting from 1) and `y` is the minimum number of hours of coaching needed, before you can pick a fair team of **P** students.

### Limits

Time limit: 15 seconds per test set.
Memory limit: 1 GB.
1 ≤ **T** ≤ 100.
1 ≤ **Si** ≤ 10000, for all $i$.
2 ≤ **P** ≤ **N**.

#### Test set 1 (Visible)

2 ≤ **N** ≤ 1000.

#### Test set 2 (Hidden)

2 ≤ **N** ≤ 105.

### Sample

| Input         | Output        |
| ------------- | ------------- |
| `3`           |               |
| `4 3`         |               |
| `3 1 9 100`   | `Case #1: 14` |
| `6 2`         | `Case #2: 0`  |
| `5 5 1 2 3 4` | `Case #3: 6`  |
| `5 5`         |               |
| `7 7 1 7 7`   |               |

In Sample Case #1, you can spend a total of 6 hours training the first student and 8 hours training the second one. This gives the first, second and third students a skill level of 9. This is the minimum time you can spend, so the answer is 14.

In Sample Case #2, you can already pick a fair team (the first and second student) without having to do any coaching, so the answer is 0.

In Sample Case #3, **P** = **N**, so every student will be on your team. You have to spend 6 hours training the third student, so that they have a skill of 7, like everyone else. This is the minimum time you can spend, so the answer is 6.



### Analysis

To make a fair team, we have to train the members of the team to the same skill level as the most skillful member of the team. 
For any **P** students we pick, the time required to make a fair team is $= \Sigma \left( \max \left( \mathbf { S } _ { \mathbf { i } } , \mathbf { S } _ { \mathbf { i } + 1 } \ldots \mathbf { S } _ { \mathbf { P } } \right) - \mathbf { S } _ { \mathbf { i } } \right)$, for all students i = 1 to **P** in the team. Our goal is to minimize this value.
One possible approach could be to go through all possible subsets of **P** students, from the given **N** students. But there exists $\left( \begin{array} { l } { N } \\ { P } \end{array} \right)$ such subsets(here symbol () denotes [Combination](https://en.wikipedia.org/wiki/Combination/)). Number of such subsets will be in the order of [Factorial(**N**)](https://en.wikipedia.org/wiki/Factorial) and so enumerating through all of them will not fit within the time limit.

#### Test set 1 (Visible)

We can start with the observation that once we fix the student with highest skill level x, to minimize our goal we should always choose students with skills as high as possible, but less than or equal to x. Hence we can sort students on the basis of skill level in decreasing order, and iterate over each student assuming they would have the highest skill level in the team. Say, this student is at position $i$ in the sorted sequence; the team would be formed of students on positions $i , i + 1 , \ldots , i + P - 1$ (i.e. a contiguous subarray of size **P**).
For each subarray of size **P** in the sorted array, we can calculate the training time required to make a fair team using the aforementioned formula. There are $N - P + 1$ subarrays of size **P**, and the complexity of calculating training time of subarray size **P** is $O ( \mathbf { P } )$. So the overall complexity of this approach is $O ( \mathbf { N } \times \mathbf { P } )$, which will be sufficient for test set 1.

#### Test set 2 (Hidden)

We need to go through all of the subarrays once, but can we calculate the training time of a subarray faster? 
Let us assume the array is sorted in decreasing order. The training time formula for a subarray starting at position $i$ is 
$= \Sigma ( \mathrm { S } [ i ] - \mathrm { S } [ j ] )$ where $j = i$ to $i + P - 1$
$= \mathbf { P } \times \mathbf { S } [ i ] - \Sigma ( \mathbf { S } [ j ] )$ where $j = i \operatorname { to } i + p - 1$
As we always need the sum of a contiguous subarray, we can pre compute the prefix sum of the whole array in advance, and get the sum of any subarray in $O ( 1 )$ time, which makes the calculation of training time $O ( 1 )$.
So, the overall complexity of this approach is $\mathrm { O } ( \mathbf { N } )$.



### Code

```go
package main

import "fmt"

func input(N *int, P *int) []int {
	_, _ = fmt.Scanf("%d %d", N, P)

	S := make([]int, *N)

	for i := 0; i < len(S); i++ {
		_, _ = fmt.Scan(&S[i])
	}

	return S
}

func sliceCopy(source, target []int)  {
	for index, value := range source {
		target[index] = value
	}
}

func merge(S []int, q int)  {
	L := make([]int, q + 1)
	R := make([]int, len(S) - q - 1)

	sliceCopy(S[:q + 1], L)

	sliceCopy(S[q + 1:], R)

	i, j, k := 0, 0, 0

	for k < len(S) {
		if L[i] < R[j] {
			S[k] = R[j]
			j++
			k++
			if j == len(R) {
				break
			}
		} else {
			S[k] = L[i]
			i++
			k++
			if i == len(L) {
				break
			}
		}
	}

	if i == len(L) {
		sliceCopy(R[j:], S[k:])
	} else {
		sliceCopy(L[i:], S[k:])
	}
}

func mergeSort(S []int)  {
	if len(S) > 1 {
		q := (len(S) - 1) / 2
		mergeSort(S[:q + 1])
		mergeSort(S[q + 1:])
		merge(S, q)
	}
}

func output() (time int) {
	var N, P int
	S := input(&N, &P)

	mergeSort(S)

	sum := 0
	for i := 0; i < P; i++ {
		sum += S[i]
	}
	time = P * S[0] - sum

	for i := 1; i < len(S) - P + 1; i++ {
		sum = sum + S[i + P - 1] - S[i - 1]
		tmp := P * S[i] - sum
		if tmp < time {
			time = tmp
		}
	}

	return
}

func main()  {
	var T int
	_, _ = fmt.Scan(&T)

	for i := 1; i <= T; i++ {
		fmt.Printf("Case #%d: %d\n", i, output())
	}
}

```

