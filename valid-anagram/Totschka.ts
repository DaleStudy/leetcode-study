// https://leetcode.com/problems/valid-anagram/

/**
 * @SC `O(N)`
 * @TC `O(N)`
 */
namespace use_hashmap {
  function isAnagram(s: string, t: string): boolean {
    if (s.length !== t.length) {
      return false;
    }
    const counter = {};
    for (const char of s) {
      counter[char] = (counter[char] || 0) + 1;
    }
    for (const char of t) {
      if (!counter[char]) {
        return false;
      }
      counter[char] = counter[char] - 1;
    }
    return true;
  }
}

/**
 * @SC `O(N)`
 * @TC `O(Nlog(N))`
 */
namespace naive_approach {
  function isAnagram(s: string, t: string): boolean {
    return [...s].sort().join('') === [...t].sort().join('');
  }
}
