package main

/*
Описание:
Давным-давно, на пути через старый дикий гористый запад,…

... человеку были даны указания, как пройти из одной точки в другую. Указаниями были "СЕВЕР", "ЮГ", "ЗАПАД", "ВОСТОК". Очевидно, что "СЕВЕР" и "ЮГ" противоположны, "ЗАПАД" и "ВОСТОК" тоже.

Идти в одном направлении и сразу же возвращаться в противоположном - бесполезное усилие. Поскольку это дикий запад, с ужасной погодой и небольшим количеством воды, важно экономить немного энергии, иначе вы можете умереть от жажды!
Как я с умом пересек гористую пустыню.

Указания, данные мужчине, следующие (в зависимости от языка)::

["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"].
or
{ "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST" };
or
[North, South, South, East, West, North, West]

Вы сразу видите, что ехать "НА СЕВЕР" и сразу "на ЮГ" неразумно, лучше оставаться на том же месте! Итак, задача состоит в том, чтобы дать мужчине упрощенную версию плана. Лучший план в этом случае - просто:

["WEST"]
or
{ "WEST" }
or
[West]

*/
import (
	"fmt"
)

func DirectionsReductions() {
	a := []string{"NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "NORTH"}
	doTest(a, []string{"NORTH"})
}
func doTest(arr []string, answer []string) {
	ans := dirReduc(arr)
	my_ans := dirReducc(arr)
	fmt.Println(answer, ans, my_ans)
}

// best solution
func dirReduc(arr []string) []string {
	zeroMap := map[string]string{
		"NORTH": "SOUTH",
		"SOUTH": "NORTH",
		"WEST":  "EAST",
		"EAST":  "WEST",
	}
	res := make([]string, 0)
	for _, r := range arr {
		l := len(res)
		if l > 0 && res[l-1] == zeroMap[r] {
			res = res[:l-1]
		} else {
			res = append(res, r)
		}
	}
	return res
}

func dirReducc(arr []string) []string {
	for i := len(arr) - 1; i > 0; i-- {
		if len(arr) == 1 {
			return arr
		}
		if i >= len(arr) && len(arr) != 0 {
			i = len(arr) - 1
		}
		if arr[i] == "WEST" && arr[i-1] == "EAST" {
			arr = append(arr[:i-1], arr[i+1:]...)
		} else if arr[i] == "EAST" && arr[i-1] == "WEST" {
			arr = append(arr[:i-1], arr[i+1:]...)
		} else if arr[i] == "NORTH" && arr[i-1] == "SOUTH" {
			arr = append(arr[:i-1], arr[i+1:]...)
		} else if arr[i] == "SOUTH" && arr[i-1] == "NORTH" {
			arr = append(arr[:i-1], arr[i+1:]...)
		}
	}
	return arr
}
