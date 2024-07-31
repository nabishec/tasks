//Реализовать fibonacci функцию, которая возвращает функцию (замыкание), 
//которая возвращает последовательные числа Фибоначчи (0, 1, 1, 2, 3, 5, ...).

package main

import "fmt"

func fibonacci() func() float64 {
	var now float64 = -1
	var was float64 = 0
	return func() float64 {
		if now < 1 {
			now += 1
			return now
		}
		now, was = (now + was), now
		return now
	}
}

func Fibonacci() {
	f := fibonacci()
	for i := 0; i < 1000; i++ {
		fmt.Println(f())
	}
}