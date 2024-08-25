const isAnagram = function (s, t) {
  const sCharCount = new Array(26).fill(0);
  const tCharCount = new Array(26).fill(0);

  Array.from(s).forEach((char) => {
    const charAsInt = char.charCodeAt(0) - 97;
    sCharCount[charAsInt]++;
  });

  Array.from(t).forEach((char) => {
    const charAsInt = char.charCodeAt(0) - 97;
    tCharCount[charAsInt]++;
  });

  return sCharCount.reduce((acc, cur, i) => acc && cur === tCharCount[i], true);
};
