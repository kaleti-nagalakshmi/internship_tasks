#Find a String
#https://www.hackerrank.com/challenges/find-a-string/problem

def count_substring(string, sub_string):
    sub_string_1 = sub_string[0]
    s = 0
    for i in range (len(string)-len(sub_string)+1):
        if string[i:i+len(sub_string)]==sub_string:
            s+=1
        
   
    return s
            
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
