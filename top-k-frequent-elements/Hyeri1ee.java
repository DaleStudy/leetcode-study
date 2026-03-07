import java.util.*;

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> maps = new HashMap<>(); //nums[i] 대상, 등장 횟수
        
            for(int i =0; i <nums.length; i++){
                maps.put(nums[i], maps.getOrDefault(nums[i], 0) + 1);
            }
        


        ArrayList<Integer> list = new ArrayList<>();
        //maps를 value기준으로 내림차순 정렬후, list에 k개만큼만 key값 추가
        Map<Integer, Integer> sorts = 
            maps.entrySet()
            .stream()
            .sorted(Map.Entry.<Integer, Integer>comparingByValue().reversed())
            .limit(k)
            .collect(Collectors.toMap(
                Map.Entry::getKey,
                Map.Entry::getValue,
                (a, b) -> a,
                LinkedHashMap::new
            ));

        for(int t : sorts.keySet()){
            list.add(t);
        }

        return list.stream()
                .mapToInt(Integer::intValue)
                .toArray();

            //list.stream().mapToInt(Integer::intValue).toArray(); 
            //Arrays.stream(arr).boxed().toList();
    }
}