class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [[""]]
        grouped_list = defaultdict(list)
        final_str_list = []
        for word in strs:
            sortedWord = ''.join(sorted(word))
            grouped_list[sortedWord].append(word)
        
        for group in grouped_list.values():
            final_str_list.append(group)
        
        return final_str_list
            
                
