'''Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains . The second line contains an array   of  integers each separated by a space.

Constraints

Output Format

Print the runner-up score.

Sample Input 0

5
2 3 6 6 5'''

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    a=set(arr) #set() removes duplicates
    b=list(a)  #made a list as there are limited functions that the 'set' can take
    c=max(b) 
    b.remove(c) #find the largest entry in the list and remove it 
    d=max(b)  # now find the largest entry in the new list and print
    print(d)

    
