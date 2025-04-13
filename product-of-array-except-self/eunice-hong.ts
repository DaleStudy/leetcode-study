function productExceptSelf(nums: number[]): number[] {
  // Check if there are zeros in the array
  const zeroCount = nums.reduce((acc, num) => {
    if (num === 0) { 
      return acc + 1;
        } else {
          return acc;
        }
    }, 0);

    if (zeroCount === 0) {
      // If there are no zeros, calculate the product of all numbers
      const totalProduct = nums.reduce((acc, num) => num * acc, 1);
      return nums.map((num) => {
        return totalProduct / num;
      });
    } else if (zeroCount === 1) {
      // If there is one zero, calculate the product of all numbers except the zero
      const totalProduct = nums.reduce((acc, num) => {
        if (num === 0) {
          return acc;
        } else {
          return num * acc; 
        }
      }, 1);
      return nums.map((num) => {
        if (num === 0) {
          return totalProduct
        } else {
          return 0;
        }
      });
    } else {
      // If there are more than one zero, return an array of zeros
      return nums.map((_) =>  0);
    }
};
