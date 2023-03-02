//머쓱이네 옷가게는 10만 원 이상 사면 5%, 30만 원 이상 사면 10%, 50만 원 이상 사면 20%를 할인해줍니다. 구매한 옷의 가격 price가 주어질 때, 지불해야 할 금액을 return 하도록 solution 함수를 완성해보세요.
function solution(price) {
    if (100000 <= price && price < 300000) {
      rate = 5;
    } else if (300000 <= price && price < 500000) {
      rate = 10;
    } else if (500000 <= price) {
      rate = 20;
    } else {
      rate=0;
    }
    answer = Math.floor(price * (1 - rate / 100));
    return answer;
  }
  
