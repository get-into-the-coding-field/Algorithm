let answer;

class Graph {
  constructor() {
    this.adjacencyList = {};
  }
  addVertex(vertex) {
    this.adjacencyList[vertex] = [];
  }
  addEdge(v1, v2) {
    if (this.adjacencyList[v1] && this.adjacencyList[v2]) {
      this.adjacencyList[v1].push(v2);
      this.adjacencyList[v2].push(v1);
    }
  }
  bfs(start) {
    const queue = [start];
    const result = { 1: 0 };
    let count = 0;
    const visited = {};
    let currentVertex;
    visited[start] = 1;

    while (queue.length) {
      currentVertex = queue.shift();
      result[currentVertex] = count;

      this.adjacencyList[currentVertex].forEach((neighbor) => {
        if (!visited[neighbor]) {
          visited[neighbor] = visited[currentVertex] + 1;
          queue.push(neighbor);
          count++;
          result[neighbor] = count;
        }
      });
    }

    const depth = Object.values(visited);
    const maxNum = Math.max(...depth);

    answer = depth.filter((x) => x === maxNum).length;
  }
}

function solution(n, edge) {
  let g = new Graph();

  for (let i = 1; i < n + 1; i++) {
    g.addVertex(i);
  }

  for (let i = 0; i < edge.length; i++) {
    g.addEdge(edge[i][0], edge[i][1]);
  }

  g.bfs(1);

  return answer;
}
