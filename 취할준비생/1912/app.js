// 백준 1912 연속합
const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n')

let N = +input.shift();
let arr = String(input).split(" ").map((Number))

let totalSum = arr[0]
let sum = arr[0]

for(let i=1; i<arr.length; i++){
  sum = Math.max(sum + arr[i], arr[i]);
  totalSum = Math.max(totalSum, sum)
}

console.log(totalSum)
