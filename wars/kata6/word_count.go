// посчитать сколько раз встречается каждое слово в строке считает через пробелы

package main

import (
	"fmt"
	"strings"
)


func WordCount() {
	fmt.Println(wordCount("Hello, world"))
}
func wordCount(s string) map[string]int {
	array := strings.Fields(s)
	m := make(map[string]int)
	for i := range array {
		_, ok := m[array[i]]
		if !ok {
			m[array[i]] = 0
		}
		m[array[i]] += 1
	}
	return m
}
