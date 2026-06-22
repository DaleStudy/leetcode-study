const isAnagram = function (s, t) {
  if (s.length !== t.length) return false;

  const data = new Map();

  for (let char of s) {
    data.set(char, (data.get(char) || 0) + 1);
  }

  for (let char of t) {
    if (!data.get(char)) return false;
    data.set(char, data.get(char) - 1);
  }

  return true;
};

// Time Limit Exceeded로 fail..
// tc: O(n^2);
// sc: O(n)
const groupAnagrams_naive = function (strs) {
  if (strs.length < 2) return [strs];

  const answer = [];

  while (strs.length > 0) {
    let temp = [strs[0]];

    if (strs.length < 2) return answer;

    strs.splice(0, 1);

    for (let j = 0; j < strs.length; j++) {
      if (isAnagram(temp[0], strs[j])) {
        // 같다면, temp 배열에 넣음
        temp.push(strs[j]);
      }
    }
    answer.push(temp);

    temp.forEach((t) => {
      const idx = strs.indexOf(t);
      if (idx !== -1) {
        strs.splice(idx, 1);
      }
    });

    if (strs.length === 1) {
      answer.push(strs);
    }
  }

  return answer;
};

// splice 같은 로직이 없어서 겨우 TLE을 통과했지만 여전히 O(n²)인 점은 변함이 없음.
const groupAnagrams_set = function (strs) {
  const visited = new Set();
  const answer = [];

  for (let i = 0; i < strs.length; i++) {
    if (visited.has(i)) continue;

    const group = [strs[i]];

    for (let j = i + 1; j < strs.length; j++) {
      if (!visited.has(j) && isAnagram(strs[i], strs[j])) {
        group.push(strs[j]);
        visited.add(j);
      }
    }

    answer.push(group);
  }

  return answer;
};

//! AI로부터 힌트를 얻어 풀어봤습니다..
// tc: O(nlogn)
// sc: O(n)
const groupAnagrams = function (strs) {
  const map = new Map();

  for (const str of strs) {
    const key = str.split('').sort().join('');

    if (!map.has(key)) {
      map.set(key, []);
    }
    map.get(key).push(str);
  }

  return [...map.values()];
};
