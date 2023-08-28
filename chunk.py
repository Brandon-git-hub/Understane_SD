from itertools import islice

def chunk(it, size):
    it = iter(it)
    #r =iter(lambda: tuple(islice(it, size))) #error:'function' object is not iterable
    # so need ,(), make it iterable
    # My real test========================
    #r =iter(lambda: tuple(islice(it, size)), [])
    #print(r)
    #print(next(r)) # (1,2,3)
    #print(next(r)) # (4,5,6)
    #print(next(r))
    # ====================================
    # My real test========================
    # r =iter(tuple(islice(it, size)))
    # print(r)
    # print(next(r)) # (1,2,3)
    # print(next(r)) # (4,5,6)
    # print(next(r))
    # print(next(r))
    # ====================================
    return iter(lambda: tuple(islice(it, size)), ())
# Conclusion:
# iter(it): if not, just (1,2,3) (1,2,3), make it a iterator, because we want to next to another in the whole file
# islice(it,size): make the slice, strat default is 0, step default is 1, so the stop heare is size
# tuple(islice(it,size)): make the islice object to the tuple
# lambda: tuple(islice(it,size)): *Important*, make it a function, because we want to traversal the whole file, everytime we
# next() to another, again use tuple(islice()) cut a batch size package
# iter(__ , ()): make function to a iterator is wrong, so add , () or [] etc, make it iterable

_file = [1,2,3,4,5,6]

#chunk(_file,3)
print(list(chunk(_file,3)))
# [(1, 2, 3), (4, 5, 6)]
print('=================')



### Real Test
with open('prompt.txt') as f:
    prompt_lines = f.read().splitlines()
    print(prompt_lines)
    batch_prompt = list(chunk(prompt_lines, 3))
    print(batch_prompt)

# output: ['Hello', 'Hi', 'Three', 'Four', 'Five', 'Six']
#         [('Hello', 'Hi', 'Three'), ('Four', 'Five', 'Six')]