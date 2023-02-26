// 백준 11478

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim();

const substrings = [];
// 부분 문자열을 다 배열에 넣어주고
for (let len = 1; len <= input.length; len++) {
  for (let i = 0; i <= input.length - len; i++) {
    const substring = input.substr(i, len);
    substrings.push(substring);
  }
}
// 중복을 제거해서 size를 구함.
let result = new Set([...substrings]);
console.log(result.size)