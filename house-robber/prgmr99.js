/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function (nums) {
  let maxMoneyAtPrevHouse = 0;
  let maxMoneyAtTwoHousesBack = 0;

  for (let i = 0; i < nums.length; i++) {
    let currentMax = Math.max(
      nums[i] + maxMoneyAtTwoHousesBack,
      maxMoneyAtPrevHouse
    );

    maxMoneyAtTwoHousesBack = maxMoneyAtPrevHouse;
    maxMoneyAtPrevHouse = currentMax;
  }

  return maxMoneyAtPrevHouse;
};
