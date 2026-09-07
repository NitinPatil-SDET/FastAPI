#Problem: Find the Largest Number in an Array
arr = [10, 45, 23, 67, 12]
largest = arr[0]
for num in arr:
    if num > largest:
        largest=num
print(largest)

#Reverse a String
s = 'patil'
rev_s = ''
for ch in s:
    rev_s = ch + rev_s
print(rev_s)

#Count Vowels in a String
s1 = "nitin"
count = 0
for ch in s1:
    if ch in 'aieuo':
        count = count+1
print(count)

#Check Palindrome
s2='Test'
rev_s = ''
for ch in s2:
    rev_s=ch+rev_s
if s2==rev_s:
    print('The Given String is Palindrome')
else :
    print('The Given String is NOT Palindrome')

#Count Frequency of Characters
s3='banana'
freq={}

for ch in s3:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
for key, value in freq.items():
    print(key, ' = ', value)