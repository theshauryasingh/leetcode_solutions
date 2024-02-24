class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        # initialEnergy = 5     energy     = [1,4,3,2]
        # initialExperience = 3 experience = [2,6,3,1]
        # +6 energy
        # +1 experience  
        extraEnergy = 0
        energySum = 0
        for item in energy:
            energySum += item
        if energySum >= initialEnergy:
            extraEnergy = 1 + energySum - initialEnergy
        extraExperience = 0
        for item in experience:
            if initialExperience > item:
                initialExperience +=  item
            else:
                temp = 1 + item - initialExperience
                extraExperience += temp
                initialExperience += temp+item
                # print('.... ', temp)
        # print(extraEnergy, extraExperience)
        return extraEnergy + extraExperience
                