class Solution:
    def isHappy(self, n: int) -> bool:
        def next_num(num):
            total =0
            while num > 0:
                digit = num % 10
                total = total + digit * digit
                num = num//10
            return total

        slow = n
        fast = next_num(n)

        while fast != 1 and slow != fast:
            slow = next_num(slow)
            fast = next_num(next_num(fast))
        return fast == 1

        