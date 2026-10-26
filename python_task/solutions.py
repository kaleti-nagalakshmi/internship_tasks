# Q1. Find the Frequency of Each Word in a Sentence
def word_freq(sen):
    
    split_sen = sen.split()
    dict_word = {}
    for word in split_sen :
        if word not in dict_word:
            dict_word[word]= 1
        else :
            dict_word[word]+= 1
    return dict_word

#Q2. Find the Frequency of Each Character in a Word
def once_char(c):
    char = {}
    for i in c :
        if i not in char :
            char[i]=1
        else :
            char[i]+=1
    for j in char:
        if  char[j] ==1:
            return j
            break
        
    else :
        return "None"


   # Q3. Find the Frequency of Each Character in a Word

def char_freq(char):
    dict_char = {}
    for i in char:
        if i not in dict_char:
            dict_char[i]=1
        else :
            dict_char[i]+=1
    return dict_char

    
#Q4. Check Whether Two Strings Are Anagrams
def anagram(s1,s2):
    if sorted(s1)==sorted(s2):
        return "True"
    else :
        return "False" 
    
#Q5. Find the First Repeating Character in a String
def sec_rep(word):
    char = []
    for i in word :
        if i not in char:
            char.append(i)
        else :
            return i 
        
    
#Q6. Move All Zeros to the End of a List
def move_zeros(l):
    Zero = []
    num = []
    for i in l:
        if i ==0:
            Zero.append(i)
        else :
            num.append(i)
    return num+Zero

#Q7. Find the Second Highest Distinct Number in a List
def sec_high_din_num(l):
    sort = sorted(l,reverse=True)
    li = []
    for i in sort:
        if i not in li :
            li.append(i)
        # else :
        #     li.remove(i)
   
    if len(li)>1:
        return li[1]
    else :
        return "None"
        
    #Q8. Remove Duplicates Without Changing the Original Order

def remove_duplicates(l):
    sort = l 
    li = []
    for i in sort:
        if i not in li :
            li.append(i)
        # else :
        #     li.remove(i)
   
    return li


#Q9. Find the Missing Number from 1 to N
def missing_number(l,n):
    total_sum =n*(n+1)//2
    sum_with_missing = sum(l)
    return total_sum-sum_with_missing

#Q10. Find Two Numbers Whose Sum Equals a Target
def target_sum(l,target):
    e = []
    for i in l :
        for j in l:
            if i==j:
                continue 
            else :
                if i +j == target :
                    e.append([i,j])
                    break
    if len(e)>0:
        return e[0]
    else :
        return None

           
           
 #Q11. Find the Number Closest to Zero
def closest_to_zero(l): 
    s = sorted(l)
    
    for i in s :
        if i >= 0 :
            return i
            break 


#Q12. Find Common Elements Between Two Lists
def common_elements(l1,l2):
    a = []
    for i in l1 :
        for j in l2:
            if i==j :
                a.append(i)
    return a 

#Q13. Rotate a List to the Right by K Positions
def rotate(l,k):
    before_k = l[:k+1]
    after_k = l[k+1:]
    print(after_k+before_k)

rotate([2,3,6,4,9],3)

#Q14. Find the Maximum Sum of Two Consecutive Elements

    
def max_consecutive_sum(nums):
    max_sum = nums[0] + nums[1]

    for i in range(1, len(nums) - 1):
        current_sum = nums[i] + nums[i + 1]

        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum

    

#Q15. Find All Pairs of Numbers Whose Sum Equals a Target
def find_pairs(nums, target):
    pairs = []

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                pair = sorted([nums[i], nums[j]])

                if pair not in pairs:
                    pairs.append(pair)

    pairs.sort(key=lambda x: x[0])
    return pairs


nums = [2, 4, 3, 5, 7, 8, 1]
target = 9

print(find_pairs(nums, target))






        
        









    

   

        
            






           










