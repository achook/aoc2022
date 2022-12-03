package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func removeDuplicates(input []byte) []byte {
	prev := 1
	for curr := 1; curr < len(input); curr++ {
		if input[curr-1] != input[curr] {
			input[prev] = input[curr]
			prev++
		}
	}

	return input[:prev]
}

func sortBytes(input []byte) {
	sort.Slice(input, func(i, j int) bool {
		return input[i] < input[j]
	})
}

func zeroMap(charMap map[byte]int) {
	for v := byte('a'); v <= 'z'; v++ {
		charMap[v] = 0
	}

	for v := byte('A'); v <= 'Z'; v++ {
		charMap[v] = 0
	}
}

func getCommonByte(charMap map[byte]int) int {
	for key, value := range charMap {
		if value == 3 {
			if key >= 'a' && key <= 'z' {
				return int(key - 'a' + 1)
			}

			if key >= 'A' && key <= 'Z' {
				return int(key - 'A' + 27)
			}
		}
	}

	return 0
}

func main() {
	read, err := os.Open("input.txt")
	if err != nil {
		panic(err)
	}

	fileScanner := bufio.NewScanner(read)
	fileScanner.Split(bufio.ScanLines)

	prioritySum := 0
	linesRead := 0
	charMap := make(map[byte]int)
	zeroMap(charMap)

	for fileScanner.Scan() {
		if linesRead == 3 {
			prioritySum += getCommonByte(charMap)
			linesRead = 0
			zeroMap(charMap)
		}

		line := fileScanner.Text()
		byteText := []byte(line)
		sortBytes(byteText)
		byteText = removeDuplicates(byteText)

		for _, element := range byteText {
			charMap[byte(element)] += 1
		}

		linesRead++
	}

	prioritySum += getCommonByte(charMap)

	read.Close()

	fmt.Printf("Sum: %v\n", prioritySum)
}
