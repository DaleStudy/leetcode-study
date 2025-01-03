/*
input : 32 bit unsigned integer n
output : unsigned integer representation of reversed bit
constraint :
1) input is always 32 bit unsigned integer
2) implementation should not be affected by programming language

solution 1)

get unsigned integer bit representation

build string s O(n)
reverse O(n)
get integer O(n)

tc : O(n) sc : O(n)

solution 2) one loop

nth bit indicates (1<<n) if reverse (1<< (32 - n))
add up in one loop
return 

tc : O(n), sc:  O(1)

 */
public class Solution {
  // you need treat n as an unsigned value
  static final int LENGTH = 32;
  public int reverseBits(int n) {
    int answer = 0;
    for(int i = 0; i < LENGTH; i++) {
      if(((1<<i) & n) != 0) {
        answer += (1 << (LENGTH -  i - 1));
      }
    }
    return answer;
  }
}
