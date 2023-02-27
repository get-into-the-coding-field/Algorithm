//최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 정수 배열 array가 매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성해보세요. 최빈값이 여러 개면 -1을 return 합니다.


function solution(array) {
    const counts = array.reduce((acc, curr) => { // reduce 함수를 사용하여 배열의 각 요소를 순회하면서 해당 요소가 몇 번 등장하는지 세는 객체 생성
      acc[curr] = (acc[curr] || 0) + 1; 
      return acc;
    }, {});
  
    const maxCount = Math.max(...Object.values(counts));
    const mostFrequent = Object.keys(counts).filter((key) => counts[key] === maxCount); //객체에서 가장 빈도가 높은 요소 탐색
  
    return mostFrequent.length === 1 ? parseInt(mostFrequent[0]) : -1;
  }