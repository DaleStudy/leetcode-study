/*

bit manipulation

find carry of each binary digits sum
example

  1 0 1 1
 +0 0 1 0
-----------
      0 1
      ^carry 1  (1<<2)
    1
   1 


 */
class Solution {
  public int getSum(int a, int b) {
    int carryBitSet;
    while(b != 0) {
      carryBitSet = a & b;
      a = a ^ b;
      b = carryBitSet << 1;
    }
    return a;
  }
}
