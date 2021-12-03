const fs = require('fs');
let binary = fs.readFileSync('./input.txt', {encoding: 'utf8'}).split('\n').map(n => n.split(''))
let binary2 = fs.readFileSync('./input.txt', {encoding: 'utf8'}).split('\n').map(n => n.split('')) //idk why this is needed?!

function life_support(array, type) {
    for (var y=0; y<array[0].length; y++) {
        z = 0
        for (var x=0; x<array.length; x++) {
            if (array[x][y] == "0") {
                z++
            }
        }
        if (z > array.length/2) {
            if (type == "O") {
                search = "0"
            } else {
                search = "1"
            }
        } else {
            if (type == "O") {
                search = "1"
            } else {
                search = "0"
            }
        }
        for (var x=0; x<array.length; x++) {
            if (array[x][y] != search) {
                array.splice(x, 1)
                x--
            }
        }
        if (array.length == 1) {
            break
        }
    }
    return array[0].join("")
}

oxygen = life_support(binary, "O")
co2 = life_support(binary2, "co2")
part2 = parseInt(oxygen, 2) * parseInt(co2, 2)
console.log(part2)
