class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        # distance = [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        # s = "abaccb"
        hash_table = {}
        for ind, letter in enumerate(s):
            first_occurence = hash_table.get(letter, -1)
            # print(first_occurence)
            if first_occurence < 0:
                hash_table[letter] = ind
            else:
                # print(distance[ord(letter)-97], hash_table, ind - hash_table[letter] - 1, )
                if not distance[ord(letter)-97] == ind - hash_table[letter] - 1:
                    return False
        return True
        