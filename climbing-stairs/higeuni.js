// complexity
// time: O(n)
// - for loop: O(n)
// space: O(1)
// - n에 관계없이 상수개의 변수만 사용되므로 O(1)

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

