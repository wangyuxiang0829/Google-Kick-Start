package main

import "fmt"

func input(N, R, C, Sr, Sc *int) []byte {
	_, _ = fmt.Scan(N, R, C, Sr, Sc)

	inst := make([]byte, *N)

	for i:= 0; i < len(inst); i++ {
		_, _ = fmt.Scanf("%c", &inst[i])
	}

	return inst
}

func output() (r, c int) {
	var N, R, C, Sr, Sc int

	inst := input(&N, &R, &C, &Sr, &Sc)

	grid := make([][]bool, R)
	for j := 0; j < R; j++ {
		grid[j] = make([]bool, C)
	}

	r, c = Sr, Sc
	grid[r - 1][c - 1] = true

	for _, direction := range inst {
		switch direction {
		case 'E': {
			for c++; grid[r - 1][c - 1] == true; {
				c++
			}
			grid[r - 1][c - 1] = true
		}
		case 'W': {
			for c--; grid[r - 1][c - 1] == true; {
				c--
			}
			grid[r - 1][c - 1] = true
		}
		case 'N': {
			for r--; grid[r - 1][c - 1] == true; {
				r--
			}
			grid[r - 1][c - 1] = true
		}
		case 'S': {
			for r++; grid[r - 1][c - 1] == true; {
				r++;
			}
			grid[r - 1][c - 1] = true
		}
		}
	}

	return
}

func main()  {
	var T int
	_, _ = fmt.Scan(&T)

	for x := 1; x <= T; x++ {
		r, c := output()

		fmt.Printf("Case #%d: %d %d\n", x, r, c)
	}
}
