package main

import (
	"fmt"
	"sort"
)

func RemoveDuplicates() {
	fmt.Println(removeDuplicates([]int{1, 2, 3, 4, 5, 6, 4, 3, 2, 4}))
}
func removeDuplicates(nums []int) []int {
	index := 1
	sort.Ints(nums)
	if len(nums) == 1 {
		return nums[:index]
	}

	for i := 1; i < len(nums); i++ {
		if nums[index-1] != nums[i] {
			nums[index] = nums[i]
			index++
		}
	}
	return nums[:index]
}
