﻿        #해석
        #s는 start index, e는 ending index로 할당한다. 
        #area 에 (e-s)*min(height[e], height[s]) 로 면적의 넓이를 구한다.
        #만약 height[s]가 height[e] 보다 작다면, 현 area보다 더 큰 결괏값을 위해 변화를 준다. 
        #   (e-s)에서 e를 줄어들면 필연적으로 area 값이 기존보다 적어진다. 따라서 s에 1을 더해 인덱스를 오른쪽으로 이동시켜 height[s] 에 변화를 준다. 
        #그 외의 상황에는 height[e]를 변화시키기 위해 e에 1를 빼 왼쪽 인덱스로 이동시킨다.  
        #해당 루프는 s가 e보다 작을때 작용된다. 만약 s의 증가와 e의 감소로 두 변수가 마주치면 종료한 후 max_area를 return시킨다. 
       


        #Big O
        #- N: height의 element 갯수

        #Time Complexity: O(N) 
        #- while : s와 e가 만날때까지 최대 N번 반복된다. 각 반복에서의 연산들은 O(1)에 해당된다. -> O(N)
        

        #Space Complexity: O(1)
        #- s,e,max_area: 변수는 상수로 작용된다 -> O(1)
        ####
        #
        #
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0 #Saving for answer
        s,e=0,len(height)-1 #Assign the first index and last index
        while s<e:
            area = (e-s) * min(height[s],height[e]) #Current area using e,s
            max_area = max(area, max_area) #Re-assing the max_area comparing with area
            if height[s]< height[e]:
                s+=1
            else:
                e -=1
        return max_area


