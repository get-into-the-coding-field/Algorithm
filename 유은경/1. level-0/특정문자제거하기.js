function solution(my_string, letter) {
  // 문자열에서 letter를 모두 제거한 새로운 문자열 생성
  let result = "";
  for (let i = 0; i < my_string.length; i++) {
    if (my_string[i] !== letter) {
      result += my_string[i];
    }
  }
  return result;
}
