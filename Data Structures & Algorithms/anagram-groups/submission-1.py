class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort_words = dict()

        for word in strs:
            # print(word)
            lst = list(word)
            lst.sort()
            sw = ''.join(lst)
            # print(f"sorted letters: {sw}")
            if sw in sort_words.keys():
                # print(f"common sorted word found at {sort_words[sw]}")
                # print(f"updating...")
                sort_words[sw].append(word)
                # print(f"Value is now {sort_words[sw]}")
            else:
                sort_words[sw] = [word]



        return list(sort_words.values())