package main

import "fmt"

func main() {
	var results = []int{90, 70, 50, 80, 60, 85}

	var length = len(results)
	for i := 0; i < length; i++ {
		fmt.Printf("%d,", results[i])
	}
}
