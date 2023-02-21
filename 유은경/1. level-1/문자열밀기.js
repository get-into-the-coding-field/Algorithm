//문자열 "hello"에서 각 문자를 오른쪽으로 한 칸씩 밀고 마지막 문자는 맨 앞으로 이동시키면 "ohell"이 됩니다. 이것을 문자열을 민다고 정의한다면 문자열 A와 B가 매개변수로 주어질 때, A를 밀어서 B가 될 수 있다면 밀어야 하는 최소 횟수를 return하고 밀어서 B가 될 수 없으면 -1을 return 하도록 solution 함수를 완성해보세요.

function solution(A, B) {
  if (A.length !== B.length) {
    return -1; //A와 B의 길이가 다를시 회전시켜도 같은 문자열이 될수 없기 떄문에 -1 리턴
  }
  const len = A.length;
  for (let i = 0; i < len; i++) {
    //이동 횟수는 A 문자열의 길이보다 작아야함
    if (A === B) {
      return i;
    }
    A = A.slice(len - 1) + A.slice(0, len - 1);
  }
  return -1;
}
