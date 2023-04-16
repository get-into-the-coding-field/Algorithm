const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const computerLength = +input[0];

const array = input.slice(2);

// graph만들기
const graph = Array.from(Array(computerLength+1), () => [])

for(let i=0; i<array.length; i++){
    const [x, y] = array[i].split(' ').map(Number);
    graph[x].push(y);
    graph[y].push(x);
}

let visit = 0;
const visited = Array(computerLength).fill(false);

const dfs = (start) => {
    visited[start] = true;
    visit++;

    for(let i=0; i<graph[start].length; i++){
        let node = graph[start][i];
        if(!visited[node]){
            dfs(node)
        }
    }
}

dfs(1);

console.log(visit - 1);