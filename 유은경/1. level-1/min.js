
//100이하의 자연수 A,B,C를 입력받아 그중 최솟값을 출력하는 프로그램을 작성

function solution(a, b, c) {
    let answer;
    answer = a < b ? a : b;
    answer = c < answer ? c : answer;
    return answer;
  }

  console.log(solution(6, 5, 11));