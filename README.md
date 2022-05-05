# word-search
Initial Comments:

Running in Python 3.10.2

Assume grid is one long string: for such a large grid this uses less memory than a python (linked) list, but this shouldn't matter


My initial thoughts were rather straight forward. This problem is slightly easier split up into 2 segments.

1) Check the grid horizontally. We do this by looping through each row, and checking if a given letter could be the start letter of the word. If it can, iteratively check the next letters in the word. If any of these fail, break and continue checking. If we reach the end of this iterative process and it hasn't broken, we must have found so instantly return True.
2) Check the grid vertically. This segment was a little more involved however here is my thinking:
    - We need to loop through the column, simply adding a ROW_LENGTH to get to the next one in the column
    - We don't need to start from letters which are less than len(word) rows from the bottom of the grid
    - We need to shift along said row by i to match the correct column
    - It'd be nice to function this given most of the code is duplicated, but given that it requires slightly different loops and checking of the grid (and given it's  only 6 lines), theres no point adding the inconvenience of multiple parameters and a function. This could be implemented however by just passing in the loop variables as parameters.

I also included several test cases of various types (including edge cases). All of these passed as expected.

To use multiple cores, typically you'd create multiple threads, however this isn't the case in python.
Python threads all run on a single core, which is great for IO or networking as it can run functions asynchronously,
But it is not good here. There is however multiprocessing, which allows us to create multiple processes and in turn run a function on multiple system threads
The downside to this is that processes can sometimes be slow to start up, but in this case it should be great. It also runs the entire
Program on a new process, so we need to be cautious to check whether we are using the main process, as we don't want to recursively create more processes.

In this instance, we can achieve data parallelisation easily by simply splitting up the word list into chunks, and handing each chunk to a different process which in turn will search the answer.
Theoretically, this will reduce runtime by a factor of num_threads, but there will be a little bit of overhead on this.


This took me maybe 2 hours overall including formatting, cleaning up code, commenting, and multiprocessing

Main implementation ~30 mins?

Average/Worst case runtime = O(m * n^2) (Where m = number of words, n = ROW_LENGTH)
