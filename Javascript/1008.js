// Salário

var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

var NumeroDoFuncionario = parseInt(lines.shift());
var HorasTrabalhadas = parseInt(lines.shift());
var ValorPorHora = parseFloat(lines.shift());
var Salario = HorasTrabalhadas * ValorPorHora;
console.log('NUMBER = ' + NumeroDoFuncionario);
console.log('SALARY = U$ ' + Salario.toFixed(2));