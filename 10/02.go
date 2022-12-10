package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func drawPixel(screen *[]byte, x int, cycle int) {
	if x-1 <= cycle%40 && cycle%40 <= x+1 {
		*screen = append(*screen, byte('#'))
		return
	}

	*screen = append(*screen, byte('.'))

}

func main() {
	read, err := os.Open("input.txt")
	if err != nil {
		panic(err)
	}

	fileScanner := bufio.NewScanner(read)
	fileScanner.Split(bufio.ScanLines)

	var screen []byte

	currentCycle := 0
	x := 1

	for fileScanner.Scan() {
		drawPixel(&screen, x, currentCycle)

		line := fileScanner.Text()
		command := line[0:4]

		if command == "noop" {
			currentCycle += 1
		}

		if command == "addx" {
			v, err := strconv.ParseInt(strings.Split(line, " ")[1], 10, 32)
			if err != nil {
				panic(err)
			}

			currentCycle += 1
			drawPixel(&screen, x, currentCycle)
			currentCycle += 1
			x += int(v)
		}
	}

	for yPos := 0; yPos < 6; yPos++ {
		for xPos := 0; xPos < 40; xPos++ {
			if screen[yPos*40+xPos] == '.' {
				fmt.Print(" ")
			}

			if screen[yPos*40+xPos] == '#' {
				fmt.Print("█")
			}
		}
		fmt.Println()
	}
}
