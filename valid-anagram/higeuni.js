// complexity
// time: O(n log n)
// - sort: O(n log n)
// - split: O(n)
// - join: O(n)
// space: O(n)
// - sortedS: O(n)
// - sortedT: O(n)
// - else : O(1)

var isAnagram = function(s, t) {
  return s.split('').sort().join('') === t.split('').sort().join('')
};

