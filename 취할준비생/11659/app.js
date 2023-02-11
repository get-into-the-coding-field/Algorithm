// 백준 11659

const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

let numbers = input[1].split(" ").map((a) => +a);
// 구간합 미리 저장
const sums = [0];

for(let i=0; i<numbers.length; i++){
    sums[i+1] = sums[i] + numbers[i];
}

let answer = [];

for(let i=2; i<input.length; i++){
    let temp = input[i].split(" ")

    answer.push(sums[temp[1]]- sums[+temp[0]-1])
      
}

console.log(answer.join("\n"))