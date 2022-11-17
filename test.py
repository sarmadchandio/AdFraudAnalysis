class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        
        if x>=0 and x<10:
            return True

        numbers = []
        while(x > 0):
            numbers.append(x%10)
            x = x // 10

        for i in range(len(numbers)):
            if numbers[i] != numbers[len(numbers)-1-i]:
                return False
        
        return True


obj = Solution()
print(obj.isPalindrome(444))