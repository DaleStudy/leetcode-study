// First Approach - hash map
var isAnagram = function (s, t) {
  let map = {};
  for (const char of s) {
    // count character occurence of s
    map[char] ? map[char]++ : (map[char] = 1);
  }
  for (const char of t) {
    // compare character occurence of t to the map object
    if (map[char]) {
      map[char]--; // decrement each time
    } else {
      return false; // if there's a new character, return false
    }
  }
  for (const el of Object.values(map)) {
    // if all the values of the map object is 0, return true
    if (el !== 0) return false; // otherwise return false;
  }
  return true;
};

// test cases
console.log(isAnagram("anagram", "nagarma"));
console.log(isAnagram("rat", "car"));

// time - O(s + t) - iterate through both input strings
// space - O(n) - map obj

//Second Approach - sorted strings
var isAnagram = function (s, t) {
  return s.split("").sort().join("") === t.split("").sort().join("");
};

// test cases
console.log(isAnagram("anagram", "nagarma"));
console.log(isAnagram("rat", "car"));

// time - O(nlogn) - using sort method
// space - O(1) - no extra space memory
