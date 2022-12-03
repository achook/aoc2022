package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func main() {
	read, err := os.Open("input.txt")
	if err != nil {
		panic(err)
	}

	fileScanner := bufio.NewScanner(read)
	fileScanner.Split(bufio.ScanLines)

	prioritySum := 0

	for fileScanner.Scan() {
		rucksackContent := fileScanner.Text()

		// Split into two parts
		firstPart := []byte(rucksackContent[:len(rucksackContent)/2])
		secondPart := []byte(rucksackContent[len(rucksackContent)/2:])

		// Sort
		sort.Slice(firstPart, func(i, j int) bool {
			return firstPart[i] < firstPart[j]
		})

		sort.Slice(secondPart, func(i, j int) bool {
			return secondPart[i] < secondPart[j]
		})

		// Remove duplicates from each part
		l1 := len(firstPart)
		prev := 1
		for curr := 1; curr < l1; curr++ {
			if firstPart[curr-1] != firstPart[curr] {
				firstPart[prev] = firstPart[curr]
				prev++
			}
		}
		firstPart = firstPart[:prev]
		l1 = len(firstPart)

		l2 := len(secondPart)
		prev = 1
		for curr := 1; curr < l2; curr++ {
			if secondPart[curr-1] != secondPart[curr] {
				secondPart[prev] = secondPart[curr]
				prev++
			}
		}
		secondPart = secondPart[:prev]
		l2 = len(secondPart)

		// Get common items
		i1 := 0
		i2 := 0
		for i1 < l1 && i2 < l2 {
			if firstPart[i1] == secondPart[i2] {
				common := firstPart[i1]

				if common >= 'A' && common <= 'Z' {
					prioritySum += int(common) - 'A' + 27
				}

				if common >= 'a' && common <= 'z' {
					prioritySum += int(common) - 'a' + 1
				}

				i1++
				i2++

			} else if firstPart[i1] < secondPart[i2] {
				i1++
			} else if firstPart[i1] > secondPart[i2] {
				i2++
			}
		}
	}

	fmt.Println("Sum: ", prioritySum)

	read.Close()
}
