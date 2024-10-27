"""TC: O(n), SC: O(1)

n은 intervals로 주어진 인터벌의 개수.

아이디어:
- 주어진 인터벌들을 앞에서부터 순회하면서 새 인터벌(newInterval)과 겹치는지 보고,
    - 겹치면 합친다. 합친 인터벌로 newInterval을 업데이트 한다.
    - 안 겹치면 newInterval과 현재 확인 중인 인터벌(curInterval) 중에 필요한 인터벌을
      결과 리스트에 넣어주어야 한다.
- 안 겹치면,
    - 이때, curInterval이 newInterval보다 앞에 있으면 이후 인터벌들 중 newInterval과 합쳐야 하는
      인터벌이 존재할 수 있다. newInterval은 건드리지 않고 curInterval만 결과 리스트에 넣는다.
    - curInterval이 newInterval보다 뒤에 있으면 newInterval을 결과 리스트에 더해주고, 그 다음
      curInterval도 결과 리스트에 더해주어야 한다.
        - 그런데 curInterval이 들어있는 리스트가 정렬되어 있으므로, 이후에 순회할 curInterval
          중에는 더 이상 newInterval과 겹칠 인터벌이 없다. newInterval은 이제 더 이상 쓰이지
          않으므로 None으로 바꿔준다.

SC:
- newInterval 값만 업데이트 하면서 관리. O(1).

TC:
- intervals에 있는 아이템을 순회하면서 매번 체크하는 시행이 O(1).
- 위의 시행을 intervals에 있는 아이템 수만큼 진행하므로 O(n).
"""


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        res = []
        for curInterval in intervals:
            if newInterval:
                # 아직 newInterval이 None으로 변경되지 않았다.
                if curInterval[1] < newInterval[0]:
                    # cur, new가 겹치지 않고, curInterval이 더 앞에 있음.
                    res.append(curInterval)
                elif curInterval[0] > newInterval[1]:
                    # cur, new가 겹치지 않고, newInterval이 더 앞에 있음.
                    res.append(newInterval)
                    res.append(curInterval)
                    newInterval = None
                else:
                    # 겹치는 부분 존재. newInterval을 확장한다.
                    newInterval = [
                        min(curInterval[0], newInterval[0]),
                        max(curInterval[1], newInterval[1]),
                    ]
            else:
                # 더 이상 newInterval과 연관된 작업을 하지 않는다. 순회 중인
                # curInterval을 결과 리스트에 더하고 끝.
                res.append(curInterval)

        if newInterval:
            # intervals에 있는 마지막 아이템이 newInterval과 겹쳤을 경우 아직
            # 결과 리스트에 newInterval이 더해지지 않고 앞선 순회가 종료되었을
            # 수 있다. 이 경우 newInterval이 아직 None이 아니므로 리스트에 더해준다.
            res.append(newInterval)

        return res
