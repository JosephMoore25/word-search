#JOSEPH MOORE PEXIP HOMEWORK - WORD SEARCH
#Running in Python 3.10.2

import multiprocessing as mp
import math

#Test Cases for me to try, comment out if not needed, but allows it to at least compile
ROW_LENGTH = 5
grid = "accdefhhijhellokemnoprrst"
#Trying all types of test cases:
#"Hello" and "Cheer" test row and column respectively, and are the same length as the row. These should pass (True - Test Passed)
#"Heer" and "Lo" should also pass, these are typical cases. (True - Test Passed)
#"Helloo" is an edge case. A substring is in, but the word is 1 letter off passing. This should fail. (False - Test Passed)
#"Thisisntinhere" is a typical case that should fail for the most part (although its longer than the row), but it isnt in there. This should fail. (False - Test Passed)
#"a" is a small case, but should pass. (True - Test Passed)
#"x" is a small case and should fail. (False - Test Passed)
#"" is an empty case and unclear whether it should pass or fail. I think it should fail as it's not a word. (False - Test Passed)
#"cheek" is a normal word which is 1 letter away from passing. This should fail. (False - Test Passed)
#"123" is an invalid word. This shouldn't break, but it also shouldn't pass as it won't be found. (False - Test Passed)
words_to_find = ["hello", "cheer", "heer", "lo", "helloo", "thisisntinhere", "a", "x", "", "cheek", "123"]

class WordSearch:
    def __init__(self, grid):
        #Not needed if grid is global, but good practice so it doesn't need to be
        self.grid = grid
        #Nothing else needed I believe.
        pass

    def is_present(self, word):
        #Nice case which takes minimal runtime to check but could instantly fail words if their length is greater than the row length
        #Given that ROW_LENGTH = 10000 and max word length = 24, commented out, but could be nice in variations

        #if len(word) > ROW_LENGTH:
            #return False

        #This loop acts like a loop for the rows for the top bit, and a loop for the columns for the bottom bit
        for i in range(0, ROW_LENGTH):

            #Loop through this row
            for j in range(i*ROW_LENGTH, (i+1)*ROW_LENGTH-len(word)+1):
                #For each letter in word
                for k in range(0, len(word)):
                    #Start checking if this next run could be the word, if its not, break
                    if self.grid[j+k] != word[k]:
                        break
                    #If we haven't broken by the end of the loop, we must have found it so return True
                    if k == (len(word)-1):
                        #If we haven't broken yet, we must have found it so return True
                        return True
            
            #Loop through each column
            for j in range(i, ROW_LENGTH*(ROW_LENGTH-len(word)) + i + 1, ROW_LENGTH):
                #For each letter in word
                for k in range(0, len(word)):
                    #Start checking if this next run could be the word, if its not, break
                    if self.grid[j+(k*ROW_LENGTH)] != word[k]:
                        break
                    if k == (len(word)-1):
                        #If we haven't broken yet, we must have found it so return True
                        return True

        #If not returned True by now, we haven't found it
        return False


ws = WordSearch(grid)

#For each process, simply perform the check on a given list
def CheckWords(words_to_find):
    for word in words_to_find:
        if ws.is_present(word):
            print("found {}".format(word))

def MultiProcess():
    #Multiprocessing in python runs multiple instances of the program, so we want to check if this is the main process
    #So we don't infinitely create new processes
    if __name__ == '__main__':
        #Check CPU count to make the most use out of all threads (or specify this!)
        num_threads = mp.cpu_count()
        #num_threads = 2

        #We now want to parralelise the data. We can simply partition the list into num_threads partitions and create a process on each sublist
        words_per_core = []
        #We may have more threads than words so figure out how words per partition
        partitions = math.ceil(len(words_to_find)/num_threads)
        #Select and add "partition" words to a list
        for i in range(0, len(words_to_find), partitions):
            words_per_core.append([words_to_find[i:i+partitions]])
        #Lets us keep track of processes
        processes = []
        #For the number of processes we need, create all of these on Check Words with their sublists
        for i in range(0, len(words_per_core)):
            p = mp.Process(target=CheckWords, args=(words_per_core[i]))
            processes.append(p)
        #Start each process
        for p in processes:
            p.start()

#Call this function to run MultiProcessing
#For single core, either run the code specified in the homework or change num_threads to 1
MultiProcess()