package main

import (
	"fmt"
	"log"
	"os"
	"strconv"
)

func fib(arg int) []int {
	rv := make([]int, arg)

	for i := 0; i < arg; i++ {
		if i == 0 || i == 1 {
			rv[i] = 1
			continue
		}
		rv[i] = rv[i-1] + rv[i-2]
	}

	return rv
}

func main() {
	args := os.Args
	if length := len(args); length == 1 || length > 2 {
		log.Fatal("Wrong number of arguments!")
		os.Exit(3)
	}

	val, err := strconv.ParseInt(args[1], 10, 32)
	if err != nil {
		log.Fatal(err)
		os.Exit(2)
	}

	for index, value := range fib(int(val)) {
		fmt.Printf("Element #%d, Value: %d\n", index, value)
	}
}
