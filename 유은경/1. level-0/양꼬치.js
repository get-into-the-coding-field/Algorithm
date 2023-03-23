function solution(n, k) {
  // 서비스 음료수 개수 계산
  const service = Math.floor(n / 10);
  // 지불해야 하는 금액 계산
  const price = n * 12000 + (k - service) * 2000;
  return price;
}
