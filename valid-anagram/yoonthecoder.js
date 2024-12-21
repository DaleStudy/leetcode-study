var isAnagram = function (s, t) {
  const sArray = [];
  const tArray = [];

  for (i = 0; i < s.length; i++) {
    sArray.push(s.charAt(i));
  }
  for (i = 0; i < t.length; i++) {
    tArray.push(t.charAt(i));
  }

  return JSON.stringify(sArray.sort()) === JSON.stringify(tArray.sort());
};

// Time complexity : O(nlogn)
// Space complexity : O(n)
