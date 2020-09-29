# python-work

##Fixing of Spelling Errors

In this code, using a provided dictionary file, we will be measuring inaccuracies of a provided text file to affirm the variation of autocorrect to be used. The following functions will be used:
1. Found - the best case scenario when the given word has no inaccuracies according to the dictionary file referenced 

2. Replace - this function cycles through all the letters in the alphabet for an incorrect position counted once until it finds a word that matches in the dictionary file

3. Swap - This function counts two incorrect positions in the given word and attempts to swap to see if this match exists

4. Drop - a word has a length of one extra than expected, and there is one incorrect position that offsets the rest of the correctly indexed letters by 1 position. 

5. No match - this funtion acts as a last resort when all of the above have not produced a result that matches with any words from the dictionary file


These functions must be executed in a particular order, to ensure that the correct autocorrect function is prioritized first, according to the reference output text file attached. 
