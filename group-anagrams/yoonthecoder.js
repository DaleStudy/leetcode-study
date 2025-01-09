var groupAnagrams = function (strs) {
  const map = new Map();

  for (const str of strs) {
    // split the string into each character (returns an array) => sort it => convert it to string
    const sortedStr = str.split('').sort().join('');
    // use the sorted Str as unique keys in the map
    if (map.has(sortedStr)) {
      map.get(sortedStr).push(str);
    } else map.set(sortedStr, [str]);
  }
  // convert values into an array
  return [...map.values()];
};
