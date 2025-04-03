// Área 

const input = require('fs').readFileSync('/dev/stdin', 'utf8');
const lines = input.split('\n');

const [A, B, C] = lines.shift().split(' ').map(item => parseFloat(item));
const triangulo = (A * C) / 2;
const circulo = 3.14159 * Math.pow(C, 2);
const trapezio = ((A + B) * C) / 2;
const quadrado = Math.pow(B, 2);
const retangulo = A * B;

console.log('TRIANGULO: ' + triangulo.toFixed(3));
console.log('CIRCULO: ' + circulo.toFixed(3));
console.log('TRAPEZIO: ' + trapezio.toFixed(3));
console.log('QUADRADO: ' + quadrado.toFixed(3));
console.log('RETANGULO: ' + retangulo.toFixed(3));
