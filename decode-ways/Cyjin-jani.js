//! 다시 풀어야 하는 문제

// Time limit 초과
const numDecodings_timeLimit = function (s) {
  let answer = 0;

  function recursion(idx, remains) {
    if (idx === remains.length) {
      answer++;
      return;
    }

    const one = remains.slice(idx, idx + 1);
    if (+one >= 1 && +one <= 9) {
      recursion(idx + 1, remains);
    }

    if (idx + 1 < remains.length) {
      const two = remains.slice(idx, idx + 2);
      if (+two >= 10 && +two <= 26) {
        recursion(idx + 2, remains);
      }
    }
  }

  recursion(0, s);

  return answer;
};

// 메모이제이션 적용
const numDecodings = function (s) {
  function recursion(idx, remains, memo = {}) {
    if (idx === remains.length) return 1;

    if (idx in memo) return memo[idx];

    let answer = 0;

    const one = remains.slice(idx, idx + 1);
    if (+one >= 1 && +one <= 9) {
      answer += recursion(idx + 1, remains, memo);
    }

    if (idx + 1 < remains.length) {
      const two = remains.slice(idx, idx + 2);
      if (+two >= 10 && +two <= 26) {
        answer += recursion(idx + 2, remains, memo);
      }
    }

    memo[idx] = answer;
    return answer;
  }

  return recursion(0, s, {});
};
