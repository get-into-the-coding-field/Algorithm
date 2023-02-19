//https://school.programmers.co.kr/learn/courses/30/lessons/12914

// dp를 사용하는 문제 규칙을 찾으면 쉽게 풀 수 있다.
// 0칸일떄 
// 1칸일때 1
// 2칸일떄 2
// 3칸일때 3
// 4칸일떄 5

function solution(n) {
  const dp = [0,1,2];
  for(let i=3; i<=n; i++){
    dp[i] = (dp[i-1] + dp[i-2])%1234567; 
  }
  return dp[n] 
}