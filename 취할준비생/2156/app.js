const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n')

const N = +input.shift();

let arr = input.map(Number)
let dp = Array(N+1).fill(0); 
dp[1] = arr[0]
dp[2] = arr[0] + arr[1]


for(let i=3; i<dp.length; i++){
  dp[i] = Math.max(dp[i-1], dp[i-3]+arr[i-1]+arr[i-2], dp[i-2]+arr[i-1])
}
console.log(dp[N])


