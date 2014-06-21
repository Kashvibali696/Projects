package main

import (
	"fmt"
	"log"
	"math"
	"os"
	"strconv"
)

const (
	MAX = 25
)

func main() {
	programArgs := os.Args

	if argsLen := len(programArgs); argsLen == 1 || argsLen > 2 {
		log.Fatal("Wrong number of arguments!")
		os.Exit(1)
	}

	howMany, err := strconv.ParseInt(programArgs[1], 10, 64)
	if err != nil {
		log.Fatal(err)
		os.Exit(2)
	}

	if howMany > MAX {
		log.Fatalf("Max is %v.\n", MAX)
		os.Exit(3)
	}

	var format string = "%." + strconv.Itoa(int(howMany)) + "f"
	fmt.Printf("Pi number with %d decimal numbers "+format+"\n", howMany, math.Pi)
}
