const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().trim().split("\n")

// tape 길이
const tape = +input[0].split(" ")[1];
// 배열 정렬
const arr = input[1].split(" ").map(Number).sort((a,b) => a-b);

// 초기 테이프 설정해주고 count는 1로시작
let initial = arr[0] - 1 + tape;
let count = 1;

// 1부터 for문돌리면서 초기값보다 작으면 냅두고 
// 크면 count++ 하고 initiald에 새로운 값 넣기
for(let i=1; i<arr.length; i++){
    if(initial >= arr[i]){

    }else{
        count++
        initial = arr[i] - 1 + tape;
    }
}

console.log(count)