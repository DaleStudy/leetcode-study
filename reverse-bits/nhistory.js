var reverseBits = function (n) {
  // Make variable to store input
  // toString method doesn't include 0 front of number
  let binary = n.toString(2);

  // Added number of 0s to satisfy 32 bits
  while (binary.length < 32) {
    binary = "0" + binary;
  }

  // Reversed binary string and convert into integer
  return parseInt(binary.split("").reverse().join(""), 2);
};

// TC: O(1)
// SC: O(1)
