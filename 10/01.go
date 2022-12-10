package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var testCycles = []int{20, 60, 100, 140, 180, 220}

func main() {
	read, err := os.Open("input.txt")
	if err != nil {
		panic(err)
	}

	fileScanner := bufio.NewScanner(read)
	fileScanner.Split(bufio.ScanLines)

	strengthSum := 0
	currentCycle := 0
	x := 1

	for fileScanner.Scan() {
		line := fileScanner.Text()
		command := line[0:4]

		for _, t := range testCycles {
			if currentCycle == t-1 {
				strengthSum += (currentCycle + 1) * x
			}
		}

		if command == "noop" {
			currentCycle += 1
		}

		if command == "addx" {
			for _, t := range testCycles {
				if currentCycle == t-2 {
					strengthSum += (currentCycle + 2) * x
				}
			}

			v, err := strconv.ParseInt(strings.Split(line, " ")[1], 10, 32)
			if err != nil {
				panic(err)
			}

			currentCycle += 2
			x += int(v)
		}
	}

	fmt.Println(strengthSum)
}
