const isAnagram = (s, t) => {
  const data = new Array(26).fill(0);
  const a_ascii = 'a'.charCodeAt();

  for (const char of s) {
    data[char.charCodeAt() - a_ascii]++;
  }

  for (const char of t) {
    data[char.charCodeAt() - a_ascii]--;
  }

  return !data.some((el) => el !== 0);
};
