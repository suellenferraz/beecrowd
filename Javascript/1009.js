// Salário com Bônus

var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

var nome = lines.shift();
var salario = parseFloat(lines.shift());
var vendas = parseFloat(lines.shift());
salario += vendas * 0.15;
console.log(`TOTAL = R$ ${salario.toFixed(2)}`);
