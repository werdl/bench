package main

import (
	"fmt"
	"sort"
)

func main() {
	ints := []int{9,8,7,6,5,4,3,2,1}
    sort.Ints(ints)
    fmt.Println(ints)
}