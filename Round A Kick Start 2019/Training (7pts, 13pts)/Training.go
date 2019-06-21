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

func sliceCopy(source, target []int) {
	for index, value := range source {
		target[index] = value
	}
}

func merge(S []int, q int) {
	L := make([]int, q+1)
	R := make([]int, len(S)-q-1)

	sliceCopy(S[:q+1], L)

	sliceCopy(S[q+1:], R)

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

func mergeSort(S []int) {
	if len(S) > 1 {
		q := (len(S) - 1) / 2
		mergeSort(S[:q+1])
		mergeSort(S[q+1:])
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
	time = P*S[0] - sum

	for i := 1; i < len(S)-P+1; i++ {
		sum = sum + S[i+P-1] - S[i-1]
		tmp := P*S[i] - sum
		if tmp < time {
			time = tmp
		}
	}

	return
}

func main() {
	var T int
	_, _ = fmt.Scan(&T)

	for i := 1; i <= T; i++ {
		fmt.Printf("Case #%d: %d\n", i, output())
	}
}
