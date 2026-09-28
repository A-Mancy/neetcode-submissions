class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0 or len(strs) == 1:
            return [strs]

        sorted_keys = []
        sorted_keys[:] = set(["".join(sorted(w)) for w in strs])

        anagram_dict = {}
        for key in sorted_keys:
            anagram_dict[key] = []

        for w in strs:
            sorted_w = "".join(sorted(w))
            anagram_dict[sorted_w].append(w)

        return list(anagram_dict.values())



