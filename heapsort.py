##pros/cons
# O(n lg n) running time
# sorts in place
# heap property is useful for structuring priority queues

##definitions for heapsort
# heap size is equal to the size of the array for building, and then a variable size at sorting time to sort in place
# parent(i) = i/2 (integer)
# left(i) = 2i
# right(i) = 2i + 1
# heap property states that for every node (i) other than the root
# of the tree (A[1]), A[parent(i)] >= A[i]

##obtain input of an (probably)unsorted list of items through I/O or from file

##build a heap with the size of the array
# for each index in the array from max length down to 1
# heapify recursively(max binary log of size nested calls) or iterates through a dynamic length stack
# when heapify ends the array will satisfy the heap property

##heapifyRecursive changes the order of items in the array in order to maintain the heap property
# at any given index (i) in the heap,
# compare the values of i and the left and right children of i
# determine the largest
# if the largest is NOT the value at the original index
# swap the largest and the index positions in the heap
# heapify the new index of largest
# to fix any violations of the heap property
# caused by exchanging (left or right) with i
# if the largest is the original index, the tree at (i) is a heap, no action required by heapify

##heapifyIterative has the same goal, but uses a control loop instead of recursion
# define a stack to use for flagging the end of the loop
# pass in an amount of elements to add to the stack,
# will always be the front half of the array (called from build heap) or one element
# while there are items in the stack
# pop the first item, do internal logic of heapify
# (compare left, right, i -> largest goes to A[i])
# if largest is NOT original index
# swap largest and original, add the index of largest to the stack
# ends when stack is empty

##heapsort uses the built heap to sort into an ordered array of size n
# iterate over the array from max length down to index (2)
# take the element at A[1] and replace it with A[i]
# call heapify at A[1] with the new value to restore the heap property
# result is a sorted list of items