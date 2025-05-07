class Solution {
    func groupAnagrams(_ strs: [String]) -> [[String]] {
        var groups: [String: [String]] = [:]
        
        for str in strs {
            let sortedStr = String(str.sorted())
            
            var values = groups[sortedStr] ?? []
            values.append(str)
            
            groups[sortedStr] = values
        }
        
        return Array(groups.values)
    }
}
