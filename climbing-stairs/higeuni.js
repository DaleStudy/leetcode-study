// complexity
// time: O(n)
// space: O(1)

var climbStairs = function(n) {
  let num1 = 1;
  let num2 = 1;
  let temp = 0;

  for(let i = 2; i<=n; ++i ) {
      temp = num2;
      num2 = num1 + num2;
      num1 = temp;
  }
  
  return num2;
};

