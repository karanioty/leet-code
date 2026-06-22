''' 11 question answers
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        m=0
        while(l<r):
            w=r-l
            h=min(height[r],height[l])
            m=max(m,w*h)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return m 
        '''
'''
121 question answer
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        c=prices[0]
        l=set()
        for i in range(len(prices)):
            if c>prices[i]:
                c=prices[i]
            else:
                l.add(prices[i]-c)
        return max(l)
        '''
'''
125 question answer 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        a="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        r=""
        for i in s:
            if i in a:
                r+=i.lower()
        
        return r==r[::-1]'''
'''
136 question answer
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
       for i in nums:
         if nums.count(i)==1:
            return i'''
'''
151 question answer
class Solution:
    def reverseWords(self, s: str) -> str:
        s.split(" ")
        l=[]
        r=""
        for i in s:
            if i!=" ":
                r+=i
            else:
                l.append(r)
                r=""
        l.append(r)
        l1=[]
        c=0
        for i in l:
            if i!="":
                l1.append(i)
        r1=""
        for j in range(len(l1)-1,-1,-1):
            r1+=l1[j]
            if j!=0:
                r1+=" "
        return r1'''
'''class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m={}
        for i in range(len(nums)):
            m[nums[i]]=m.get(nums[i],0)+1
        k=max(m.values())
        d=0
        for i,j in m.items():
            if j==k:
                d=i
                break
        return d'''
'''class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rotate(arr,i,j):
            while(i<j):
                arr[i],arr[j]=arr[j],arr[i]
                i+=1
                j-=1
        def call(arr,n,s):
            rotate(arr,0,n-1)
            rotate(arr,0,s-1)
            rotate(arr,s,n-1)
            return arr
        if len(nums)>1:
            call(nums,len(nums),k%len(nums))'''
        