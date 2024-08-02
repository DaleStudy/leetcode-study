var getSum = function (a, b) {
  while (b !== 0) {
    if (b > 0) {
      a++;
      b--;
    } else {
      b++;
      a--;
    }
  }
  return a;
};

// |b| is absolute value of b
// TC: O(|b|)
// SC: O(1)
