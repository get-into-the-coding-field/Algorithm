//첫 번째 분수의 분자와 분모를 뜻하는 numer1, denom1, 두 번째 분수의 분자와 분모를 뜻하는 numer2, denom2가 매개변수로 주어집니다. 두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.

function solution(numer1, denom1, numer2, denom2) {
  const numer = numer1 * denom2 + numer2 * denom1; // 두 분수를 더한 분자
  const denom = denom1 * denom2; // 두 분수의 분모를 곱한 분모

  // 최대공약수 구하기
  const gcd = (a, b) => {
    return b === 0 ? a : gcd(b, a % b);
  };
  const divisor = gcd(numer, denom); // 분자와 분모의 최대공약수

  // 기약 분수로 만들기
  const answer = [numer / divisor, denom / divisor];
  return answer;
}
