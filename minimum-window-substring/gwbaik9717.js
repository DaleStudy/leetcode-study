// n: len(s), m: len(t)
// Time complexity: O(n+m)
// Space complexity: O(n+m)

/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
var minWindow = function (s, t) {
  let i = 0;
  let j = 0;

  const current = new Map();
  const target = new Map();

  current.set(s[i], 1);

  for (const chr of t) {
    if (target.has(chr)) {
      target.set(chr, target.get(chr) + 1);
      continue;
    }

    target.set(chr, 1);
  }

  let answer = null;

  while (i < s.length) {
    let pass = true;
    for (const [key, value] of target) {
      if (!current.has(key)) {
        pass = false;
        break;
      }

      if (current.get(key) < value) {
        pass = false;
        break;
      }
    }

    if (pass) {
      if (!answer) {
        answer = s.slice(i, j + 1);
      }

      if (answer && j - i + 1 < answer.length) {
        answer = s.slice(i, j + 1);
      }

      current.set(s[i], current.get(s[i]) - 1);
      if (current.get(s[i]) === 0) {
        current.delete(s[i]);
      }
      i++;

      continue;
    }

    if (j < s.length) {
      j++;
      current.set(s[j], (current.get(s[j]) || 0) + 1);
    } else {
      break;
    }
  }

  if (answer === null) {
    return "";
  }

  return answer;
};
