/**
 * @param {string} s
 * @return {number}
 * 
 * complexity
 * time: O(n)
 * space: O(n)
 */
var lengthOfLongestSubstring = function(s) {
  let set = new Set();
  let left = 0;
  let answer = 0;

  for(let i=0; i<s.length; ++i) {
      while(set.has(s[i])){
          set.delete(s[left])
          if(s[i] === s[left]) {
              left ++;
              break;
          }
          left ++;
      }
      set.add(s[i])
      answer = Math.max(answer, i - left + 1)
  }
  return answer;
};

