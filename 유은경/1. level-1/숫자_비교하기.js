function solution(num1, num2) {
  var answer = 0;
  if (num1 / num2 <= 1) {
    answer = -1;
  } else if (num1 / num2 > 1) {
    answer = 0;
  }

  return answer;
}
