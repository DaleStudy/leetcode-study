# Time Complexity: O(n) -> iterate from 1 to n, updating arr[] in O(1) for each i.
# Space Complexity: O(n) -> store results in an array of size (n+1).

class Solution:
    def countBits(self, n: int) -> List[int]:
        # make an array of size (n+1), initialized with 0s.
        arr = [0] * (n + 1)  
        
        # loop from 1 to n
        for i in range(1, n + 1):  
            if i % 2 == 0:
                # even number -> same count as i//2
                arr[i] = arr[i // 2]  
            else:
                # odd number -> one more bit than i//2
                arr[i] = arr[i // 2] + 1  
        
        return arr
