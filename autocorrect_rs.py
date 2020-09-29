#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 13:12:20 2020
In this code we are comparing words from a text file, needing to be verified and corrected with comparision
 to a dictionary file. 
 Using the concept of autocorrect in the below order, we can either:
     1. Find a correct word from the text (FOUND)
     2. Taking out an extra character leading to an approved word (DROP)
     3. Switching two characters of the string to match the dictionary word (SWAP)
     4. Replace a character with one that matches a dictionary word (REPLACE)
     5. If all else fails, the word will be recorded as NO MATCH.
@author: sathyaramesh
"""
import string
letters_list = string.ascii_lowercase#string turned into list
def FOUND(t,d,result):
    result_op,result_word=result 
    if t == d and t[::-1]==d[::-1]:
        result_op[t]=':FOUND'#FOUND IS DONE
        result_word[t]=d
        result=result_op,result_word
    return result
def NOMATCH(text,result):
        result_op,result_word=result
        result_op[text]=':NO MATCH'
        result_word[text]=text
        result=result_op,result_word
        return result
    
def DROP(t,d,result):
    result=result_op,result_word
    drop_list=[]
    if d not in result_op.keys():
        for i in range(0,len(t)):
            new_t = t[:i]+ t[(i+1):]
            if new_t == d:
                drop_list.append(new_t)
                drop_list.sort()
                new = drop_list[len(drop_list)-1]
                if len(drop_list)>0:
                    result_op[t]=':DROP'
                    result_word[t]=new
        result=result_op,result_word
        return result
    
def SWAP(t,d,rep,result):
    result_op,result_word=result
    if t[rep[0]]==d[rep[1]] and t[rep[1]]==d[rep[0]]:
        result_op[t]=':SWAP'
        result_word[t]=d
    result=result_op,result_word
    return result

def REPLACE(t,d,rep,result): 
    s3_list=[]
    result_op,result_word=result
    for i in letters_list:
        # print(i)
        replace=t.find(t[rep[0]])
        # print(replace,'is replaec fore ',t,d)
        if replace!=-1:
            # s3=t.replace(t[replace],i)
            t1=t
            t1 = t[:rep[0]] + i + t[rep[0]+1:]
            # print(s3,d,'are they equal?')
            if t1==d:
                # print("s3 equals D - matched in replace")
                s3_list.append(t1)

    s3_list.sort()
    # print(s3_list)
    if len(s3_list)>0:
        if s3_list[0]==d:
            result_op[t]=':REPLACE'
            result_word[t]=d          
    else:
        pass
    result=result_op,result_word
    return result

if __name__=='__main__':
    #created a dictionary file input
    diction=input('Dictionary file => ')
    print(diction)
    diction_fh=open(diction)
    #conversion from file to list
    diction_set=set()
    for line in diction_fh:
        line = line.strip('\n')
        diction_set.add(line)

    
#     #created a text file to compare against dictionary list
    text=input('Input file => ')

    print(text)
    text_fh = open(text)
    text_list=[]
    for line in text_fh:
        line = line.strip('\n')
        text_list.append(line)
    # print(text_list,'line56')
        
    # two blank dictionaries: one that stores the autocorrect function 
        
    #the second being the text word against the dictionary word
    result_op={}
    result_word={}
    result=result_op,result_word
    for t in text_list:
        for d in diction_set:
            match = False
            if t==d:
                result=FOUND(t,d,result)
                match = True
                break
        if match== False:
                result=NOMATCH(t,result)
                
    for t in text_list:
        if result_op[t]==':NO MATCH':
            for d in diction_set:
                if len(t)==len(d)+1:
                        result=DROP(t,d,result)
                        # result_op,result_word=result
    for t in text_list:
        if result_op[t]==':NO MATCH':
            for d in diction_set:
                    if len(t)==len(d):
                        rep = [i for i in range(len(d)) if t[i] != d[i]]
                        if len(rep)==2:
                            result=SWAP(t,d,rep,result)
                            result_op,result_word=result

    for t in text_list:
        if result_op[t]==':NO MATCH':
            for d in diction_set:
                if len(t)==len(d):
                    rep=[i for i in range(len(d)) if t[i] != d[i]]
                    if len(rep)==1:
                        result=REPLACE(t,d,rep,result)
                        result_op,result_word=result
    result_op,result_word=result
            
    for key1,value1 in result_op.items():
        for key2,value2 in result_word.items():
            if key1 == key2:
                print(key1.ljust(15,' ')+' -> '+value2.ljust(15,' ')+' '+value1)
            