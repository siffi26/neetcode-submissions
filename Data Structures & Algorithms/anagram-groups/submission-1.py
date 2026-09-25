class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hmap = {}
        for each in strs:
            news_s = ''.join(sorted(each))
            # print(news_s)
            if news_s in hmap:
                hmap[news_s].append(each)
            else:
                hmap[news_s] = [each]

        res = []   
        for key, value in hmap.items():
            res.append(value)

        return res


            
                
