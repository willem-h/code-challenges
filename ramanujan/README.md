# Calculating Ramanujan's Number

Ramanujan's number, 1729, is a smallest number that can be expressed by the sum
of two cubes in two different ways:

1729 = 1^3 + 12^3 = 9^3 + 10^3

It was a fun little challenge figuring out how to calculate it efficiently
with no assumptions on the search space. My first implementation calculated all
the cubes for numbers less that 20 and then added them in pairs and compared
them. This requires prior knowledge of the number to do efficiently and also was
terribly inefficient for numbers higher than 20.

The implementation I landed on keeps track of additions of cubes for ever
increasing initial integers. Once a sum of cubes is found that matches a
previously calculated value the program returns the initial integers and the
equation in the form listed above.

More information about this number can be found on [Wikipedia](https://en.wikipedia.org/wiki/1729_%28number%29).
