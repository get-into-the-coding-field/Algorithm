function solution(clothes) {
  let answer = 0;
  const hash = new Map();

  for (let i = 0; i < clothes.length; i++) {
    const pre = hash.get(clothes[i][1]);
    hash.set(clothes[i][1], pre === undefined ? 1 : pre + 1);
  }

  for (let key of hash.keys()) {
    hash.set(key, hash.get(key) + 1);
  }
  console.log(hash);
  let mul = 1;
  for (let value of hash.values()) {
    mul *= value;
  }
  answer = mul - 1;
  return answer;
}
