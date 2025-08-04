const encode = function (strs) {
  const separator = '\\';
  return strs.join(separator);
}


const decode = function (str) {
  const separator = '\\';
  return str.split(separator);
}

// 문제가 너무 별로다
// 문제에서 제시하고 있는 해답도 별로다
// 이모지같은 걸 구분자로 쓰거나, length를 앞에 넣어서 구별하거나 해도 사실 제대로 암호화했다고 말할 수 없음
// 그런 걸 정답으로 제공할 거면 이런 문제를 왜 내는 거여
// 이 문제가 Blind 75에 속해 있는 이유가 뭘까...?!
