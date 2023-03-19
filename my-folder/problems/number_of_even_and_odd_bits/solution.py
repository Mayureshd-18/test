class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        a = bin(n)[2:]
        a = a[::-1]
        print(a)
        even = 0
        odd = 0
        
        for i in range(len(a)):
            if i%2==0 and a[i] == "1":
                print(i,a[i])
                even+=1
            elif i%2!=0 and a[i] == "1":
                print(i,a[i])
                odd+=1
                
            print(even,odd)
                
        return [even, odd]