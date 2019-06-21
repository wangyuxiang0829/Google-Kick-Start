package main

import (
	"fmt"
	"math"
)

func even(n int) bool {
	if n < 10 {
		return n%2 == 0
	}
	return even(n/10) && (n%10)%2 == 0
}

func in() (i int) {
	fmt.Scan(&i)
	return
}

func find(N int) int {
	c := make(chan int, 2)
	go func(n int, c chan int) {
		for ; !even(n); n++ {

		}
		c <- n
	}(N, c)

	go func(n int, c chan int) {
		for ; !even(n); n-- {

		}
		c <- n
	}(N-1, c)

	x, y := <-c, <-c

	return int(math.Min(math.Abs(float64(x-N)), math.Abs(float64(y-N))))
}

func main() {
	T := in()
	for i := 1; i <= T; i++ {
		N := in()
		fmt.Printf("Case #%d: %d\n", i, find(N))
	}
}
