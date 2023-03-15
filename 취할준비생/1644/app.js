const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().trim();

// 소수 구하기
let primes = Array(+input+1).fill(true);
primes[0] = false
primes[1] = false

for(let i=2; i*i<=primes.length; i++){
  if(primes[i]){
    for(let j=i*i; j<=primes.length; j+=i){
      primes[j] = false;
    }
  }
}

let result = [];
for(let i=0; i<primes.length; i++){
  if(primes[i]){
    result.push(i)
  }
}

// 투포인터
let left = 0;
let right = 0;
let sum = 0;
let count = 0;

while(right < result.length){
  sum += result[right];
  right++;
  while(sum >= +input){
    if(sum === +input){
      count++;
    }
    sum -= result[left];
    left++;
  }
}
console.log(count)