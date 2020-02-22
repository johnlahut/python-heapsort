## Heapsort

Implements a max-heap sorting algorithm described in Cormen et. al.  

The sorted array that is returned by this algorithm is in descending 
order as the heap behind the scenes is a max-heap.


---

### Usage

The user can run the heap.py file to execute a simple sort. Or the module can be imported
and used as the following:

```python
# construct a new heap with an array of values
from heapsort.heap import Heap
heap = Heap([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])

# print the heap contents
heap.look()

# sort the heap and print the sorted values
print(heap.sort())

# display that the original heap remains unchanged, rather a copy is returned
heap.look()
``` 