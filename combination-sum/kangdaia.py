class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        주어진 숫자 목록에서 목표하는 합을 만들 수 있는 조합을 찾는 함수
        숫자는 동일 숫자를 여러번 사용해도 됨

        방법:
        DFS 방식을 사용함.
            - 현재 인덱스를 기준으로,
                (선택지)
                현재 위치의 숫자값을 현재 조합에 포함할지
                    - 현재 합을 만들기 위해 남은 값 - 현재 값이 0 이상이면 포함 가능
                    - 현재 값을 여러번 쓸 수 있기에 인덱스를 늘리지 x
                현재 위치의 숫자값을 현재 조합에 포함하지 않을지
                - 이 인덱스가 목록길이를 넘어가면 안됨
            - 합의 나머지 값이 0이면 목표에 도달한것 -> 조합 목록에 포함

        Args:
            candidates (list[int]): 사용가능한 숫자 목록. unique
            target (int): 목표하는 합
        
        Returns:
            list[list[int]]: 목표하는 합을 만들 수 있는 가능한 숫자 조합. unique
        """
        combinations = list()
        def getCombination(idx, remain, path):
            """
            현재 함수에서 재귀를 위한 helper 함수
            """
            if remain == 0:
                combinations.append(path)
                return
            if idx < len(candidates):
                curr = candidates[idx]
                if remain - curr >= 0:
                    getCombination(idx, remain - curr, path + [curr])
                getCombination(idx + 1, remain, path)
            return
        getCombination(0, target, [])
        return combinations
