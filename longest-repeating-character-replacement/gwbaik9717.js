// Time complexity: O(n)
// Space complexity: O(1)

/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function (s, k) {
  let i = 0;
  let j = 0;

  const counter = new Map();
  counter.set(s[i], 1);

  let answer = 1;

  const getMaxCount = () => {
    let maxCount = 0;

    for (const [key, value] of counter) {
      maxCount = Math.max(maxCount, value);
    }

    return maxCount;
  };

  while (true) {
    if (s.length - i <= answer) {
      break;
    }

    const maxCount = getMaxCount();
    const totalCount = j - i + 1;

    if (totalCount - maxCount <= k) {
      j++;
      counter.set(s[j], (counter.get(s[j]) || 0) + 1);
      answer = Math.max(totalCount, answer);
      continue;
    }

    counter.set(s[i], counter.get(s[i]) - 1);
    if (counter.get(s[i]) === 0) {
      counter.delete(s[i]);
    }

    i++;
  }

  return answer;
};
