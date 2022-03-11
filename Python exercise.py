#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 1.Morse Code
def morse_code(s):
    chars = "abcdefghijklmnopqrstuvwxyz0123456789,.?;:-/)( "
    codes = """.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..-
                -.-- --.. ----- .---- ..--- ...-- ....- ..... -.... --... ---.. ----. --..-- .-.-.- ..--.. -.-.-.
                ---... -....- -..-. ..--.- ..--.-"""
    codes = codes.split()
    codes.append(' ')
    dict_morse = dict(zip(chars,codes))
    s = s.lower()
    print(' '.join(dict_morse[c] for c in s))
while True:
    try:
        s = input()
        morse_code(s)
    except:
        break


# In[1]:


#2 Unique Letters
import collections
def  unique_letters(s):
    ans = collections.defaultdict(int)
    s = s.upper()
    for c in s:
        if c.isalpha():
            ans[c] += 1
    return (list(ans.keys()),len(ans.keys()))
while True:
    try:
        s = input()
        print(unique_letters(s))
    except:
        break


# In[ ]:


#3 Case Count
def case_count(s):
    upper_num = 0
    lower_num = 0
    for c in s:
        if c.isalpha():
            if c.isupper():
                upper_num += 1
            else:
                lower_num += 1
    ans1 = "Uppercase: %d"%upper_num
    ans2 = "Lowercase: %d"%lower_num
    ans = (ans1,ans2)
    return ans
while True:
    try:
        s = input()
        print(case_count(s))
    except:
        break

