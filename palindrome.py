#this program calculates the jth palindrome number after a number i
#the first line of input takes the number of times you want to do the test

#take inputs
n = int(input())   #number of test cases
testcases = [[0]*2]*n     #variable to store the test cases
for i in range(n):
    testcases[i] = list(map(int, input().split()))    #inputting test case

#define function to test if number n is palindrome
def ifpalindrome(n):
    temp=n
    rev=0

    while(n>0):
        dig = n%10
        rev = rev*10+dig
        n = n//10

    if(temp == rev):
        return 1
    else:
        return 0

#variable to store output
output = [0]*n

#run through the testcases
for i in range(n):
    start = testcases[i][0]
    count = 0

    while count < testcases[i][1]:
        count += ifpalindrome(start)
        start += 1

    output[i] = start - 1

#print the output
print(*output, sep='\n')
