class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        res = [0]*(len(num1)+len(num2))
        for i in range(len(num1)-1,-1,-1):
            for j in range(len(num2)-1, -1, -1):
                product = int(num1[i]) * int(num2[j])
                total = product + res[i+j+1]
                res[i+j+1] = total % 10
                res[i+j] += total // 10
        str_digits = [str(digit) for digit in res]
        joined = ''.join(str_digits)
        result_str = joined.lstrip('0') or "0"
        return result_str
            
        