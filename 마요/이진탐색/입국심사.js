function solution(n, times) {
  const getPassedCount = (time) => {
    let count = 0;
    for (const t of times) {
      count += Math.floor(time / t);
      if (count >= n) {
        break;
      }
    }
    return count;
  };

  let left = times[0];
  let right = n * Math.max(...times);
  let answer = right;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    const passedCount = getPassedCount(mid);

    if (passedCount >= n) {
      answer = mid;
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }

  return answer;
}
