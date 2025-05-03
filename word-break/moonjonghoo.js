/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
var wordBreak = function (s, wordDict) {
  const memo = new Map(); // 실패/성공 여부 기억
  const wordSet = new Set(wordDict); // lookup 최적화

  function canBreak(sub) {
    if (sub === "") return true;

    if (memo.has(sub)) return memo.get(sub);

    for (let i = 1; i <= sub.length; i++) {
      const prefix = sub.slice(0, i);
      if (wordSet.has(prefix)) {
        const suffix = sub.slice(i);
        if (canBreak(suffix)) {
          memo.set(sub, true);
          return true;
        }
      }
    }

    memo.set(sub, false); // 실패한 경우도 기억
    return false;
  }

  return canBreak(s);
};
