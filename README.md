flatten
-------

A pure python modle implementing sequence flattening with cycle detection.  


# Install

```
    # pip install flatten
```

# Usage


```
>>> from flatten import flatten
>>> for x in flatten([1, [2, 3]]):
...     print x
1
2
3
>>> l = [1, 2, 3]
>>> for x in flatten([l, l]):
...     print x
1
2
3
1
2
3
>>> l = [1, 2, 3]
>>> l.append(l)
>>> for x in flatten([l, l]):
1
2
3

    