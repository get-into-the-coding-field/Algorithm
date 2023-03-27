const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n')

const N = +input[0];
const alphabet = input.slice(1);

const treeNode = {};

for(let i=0; i<N; i++){
  const [node, left, right] = alphabet[i].split(" ");
  treeNode[node] = [left, right];
}

let answer = "";

// 전위 순회 방식
const preOrder = (node) => {
  if(node === "."){
    return;
  }
  const [left,right] = treeNode[node];
  answer += node;
  preOrder(left);
  preOrder(right);
}

// 중위 순회 방식
const inOrder = (node) => {
  if(node === "."){
    return ;
  }
  const [left, right] = treeNode[node];
  inOrder(left);
  answer += node;
  inOrder(right);
}

// 후위 순회 방식
const postOrder = (node) => {
  if(node === "."){
    return;
  }
  const [left, right] = treeNode[node];
  postOrder(left);
  postOrder(right);
  answer += node;
}

preOrder("A")
answer += "\n"
inOrder("A")
answer += "\n"
postOrder("A")

console.log(answer)