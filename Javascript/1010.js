// Cálculo simples

var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

var [Codigo1, Quantidade1, Valor1] = lines.shift().split(' ').map(item => parseFloat(item));
var [Codigo2, Quantidade2, Valor2] = lines.shift().split(' ').map(item => parseFloat(item));

var calculo = (Quantidade1 * Valor1) + (Quantidade2 * Valor2);
console.log(`VALOR A PAGAR: R$ ${calculo.toFixed(2)}`);