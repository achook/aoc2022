const fs = require('fs');

const allFileContents = fs.readFileSync('input.txt', 'utf-8');

let count = 0

allFileContents.split("\n").forEach(line =>  {
    startFirst = parseInt(line.split('-')[0])
    endFirst = parseInt(line.split(',')[0].split('-')[1])

    startSecond = parseInt(line.split(',')[1].split('-')[0])
    endSecond = parseInt(line.split('-')[2])

        // Second contained by first
    if ((startSecond >= startFirst && endSecond <= endFirst) ||
        // First contained by second
        (startFirst >= startSecond && endFirst <= endSecond)) {
            count++
    }
})

console.log(`Count: ${count}`)