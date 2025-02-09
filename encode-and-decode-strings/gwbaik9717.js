// n: len(str)
// Time complexity: O(n)
// Space complexity: O(1)
const encode = function (arr) {
  let answer = "";

  for (const word of arr) {
    answer += `${word.length}${SEPERATOR}`;
  }

  return answer;
};

// n: len(str)
// Time complexity: O(n)
// Space complexity: O(n)
const decode = function (str) {
  const SEPERATOR = "|";
  const words = [];

  let i = 0;
  let wordLength = "";

  while (i < str.length) {
    if (str[i] === SEPERATOR) {
      words.push(str.slice(i + 1, i + 1 + Number(wordLength)));
      i += Number(wordLength) + 1;
      wordLength = "";
      continue;
    }

    wordLength += str[i];
    i += 1;
  }

  return words;
};
