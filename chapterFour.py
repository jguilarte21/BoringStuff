"""
Chapter Four - Lists 

List - a value that contains multiple values in an ordered sequence 
    Ex. A list value looks like this: ['cat', 'bat', 'rat', 'elephant']

spam = ['cat', 'bat', 'rat', 'elephant']
    This means that spam[0] is 'cat', so on and so forth 

Lists can also contain other lists
    Ex. spam = [['cat', 'bat'], [10, 20, 30,40 50]]
    This means that spam[0] is ['cat', 'bat']
    And spam[0][1] is 'bat'
        First index dictates which list value to use, and the second indicates the value within the list value 

spam[-x] -x will start in the back of the list 
    Ex. spam[-1] is 'elephant'

You can use slicing to get a sequence form a list 
    Ex. spam[0:4] <- list starting from beginning to 4; Same as spam[:4]
    spam[2:] <- starts at the 2 indexed value and goes to end 

+ operator will combine two lists 

* and int will replicate string 

for i in range(len(LISTNAME)) <- iterates through whole list

'in' and 'not in' check to see if a value is in a list 

Tuples are very identical to lists, they are immutable 
    Created with '()'
    Ex. eggs = ('hello', 42, 0.5)





"""