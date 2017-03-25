# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists are mutable arrays and can contain homogeneous data types. Tuples are immutable and can contain multiple data types at once. Tuples can be converted easily into dictionaries, but lists cannot be used as keys for dictionaries. 

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists are ordered arrays that can contain duplicates. Sets are unordered and can't contain duplicates. An array of integers [1,2,3,4,22,2,2,3,4,5,6,4] is a list; a dictionary that displayed counts for each element is an example of a set (i.e. {'one': 1, 'two': 3, 'three': 1 ...} is an example of a specific type of set. If you were to convert the array of integers into a set, it would simply remove the duplicates. Finding elements in a set is much faster than in a list, because items in a set are hashed, allowing for quick lookup, but this means that sets can only contain hashable elements. 

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> The lambda operator is a method for easily creating anonymous functions. General structure is f = lambda arguments: expression. For example: f = lambda x, y: x + y would add x and y inputs. In the sorted() function, the 'key' argument can accept a lambda function. So if I wanted to sort t = [(x1, y1, z1),(x2,y2,z2),(x3,y3,z3)] by the 3rd element, I could use sorted(t, key=lambda item: item[3]) to return a new, sorted list.  

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are operations that take lists and transform them in some manner or other.  A 'map' applies a function to all elements of a list. So a function that increases all elements of a list by 1 would be a map. A 'filter' is an operation that returns only selected values from a list, so a function that returns only the values greater than 5 in a list of integers would be a filter.

 

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days 

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





