// Extremamente básico

// Esse tipo de código não funciona no ambiente do Beecrowd:
A = parseInt(prompt()); 
B = parseInt(prompt());

X = A + B;

console.log("X = " + X);

// Aqui está o código correto:

var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

var A = parseInt(lines.shift());
var B = parseInt(lines.shift());

var X = A + B;

console.log("X = " + X);