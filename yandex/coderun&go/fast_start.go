//Здесь будут закомменчены все задачи подряд, так как они простые и так удобнее

//FIRST
/*
Даны три натуральных числа. Возможно ли построить треугольник с такими сторонами? Если это возможно, выведите строку YES, иначе выведите строку NO.

Треугольник — это три точки, не лежащие на одной прямой.
Формат ввода

Вводятся три натуральных числа.
Формат вывода

Выведите ответ на задачу.
*/

// decision
/*
package main

import (
    "fmt"
    "log"
)

func main() {
    var number [3]int64
    for i := 0; i < 3; i++ {
        _, err := fmt.Scan(&number[i])
        if err != nil {
            log.Fatal(err)
        }
    }
    if number[2]/(number[0]+number[1])+number[1]/(number[0]+number[2])+number[0]/(number[2]+number[1]) == 0 {
        fmt.Println("Yes")
    } else {
        fmt.Println("No")
    }
}

*/

//SECOND
/*

 */
package main

import (
	"fmt"
)

func main() {
	var input int
	for {
		n, err := fmt.Scan(&input)
		fmt.Println("Вы ввели:", input, n, err)
		if err != nil {
			fmt.Println("Ошибка при считывании ввода:", err)
			return
		}

		fmt.Println("Вы ввели:", input, n, err)
	}
}
