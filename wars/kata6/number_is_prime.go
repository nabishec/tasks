package main

import (
	"fmt"
	"log"
	"math"
	"math/big"
)

func NumberIsPrime() {
	var number int
	_, err := fmt.Scan(&number)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(isPrime(number))
	fmt.Println(isPrimme(number))
}

// good solution
func isPrime(n int) bool {
	return big.NewInt(int64(n)).ProbablyPrime(0)
}

// my solution
func isPrimme(n int) bool {
	if n < 0 {
		return false
	}

	if n == 0 || n == 1 {
		return false
	}

	for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}
