const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().split('\n');

// while과 replace를 사용해서 풀었었는데 메모리초과가 나와서 스택으로 품

const arr = input[0].trim()
const danger = input[1]

function stringExplosion(input, bomb) {
  const stack = []; 

  for (let char of input) {
    stack.push(char);

    // bomb 글자길이보다 stack길이가 크고 bomb길이만큼 잘랐는데 bomb이랑 같을때
    if (stack.length >= bomb.length && stack.slice(-bomb.length).join('') === bomb) {
      stack.splice(-bomb.length); 
    }
  }
 
  const result = stack.join('');
  return result === '' ? 'FRULA' : result; 
}

const result = stringExplosion(arr, danger);
console.log(result);
