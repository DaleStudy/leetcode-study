var groupAnagrams = function (strs) {
  // Declare hash map to store sorted strs
  let map = new Map();

  for (let str of strs) {
    // Sorted each str
    const sortedStr = str.split("").sort().join("");

    // If there is alread sortedStr on the map, pushed str
    if (map.has(sortedStr)) {
      map.get(sortedStr).push(str);
    } else {
      // If there is no sortedStr on the map, insert [str]
      map.set(sortedStr, [str]);
    }
  }
  return Array.from(map.values());
};

// TC: O(n*klogk)
// SC: O(n*k)
// n -> length of strs array
// k -> amount of character for each element
