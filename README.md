# KheironHome
A take-home exercise for Kheiron Medical ML job

Completed all Part1, Part2 and Bonus exercises. 

Requirements:

Python 3.7.9

collections (built-in)

flask (pip install flask)

Make sure that all of the input to all three applications is space separated for each element! F.e. ( 1 + 5 ) + ( 2 * ( 3 + 1 ) )

Edge cases (like division by zero, etc) are not handled as suggested by the task.

## Part One

python Part1.py 

Give space-separated prefix input.

### Used the same sample input as exercise (caret prompt for clarity only):
```
> 3
3
> + 1 2
3
> + 1 * 2 3
7
> + * 1 2 3
5
> - / 10 + 1 1 * 1 2
3.0
> - 0 3
-3
> / 3 2
1.5
```

## Part Two

python Part2.py 

Give space-separated infix input.

### Used the same sample input as exercise (caret prompt for clarity only):
```
> ( 1 + 2 )
3
> ( 1 + ( 2 * 3 ) )
7
> ( ( 1 * 2 ) + 3 )
5
> ( ( ( 1 + 1 ) / 10 ) - ( 1 * 2 ) )
-1.8
```

## Part Three
pip install flask

python Bonus.py 

Open browser and navigate to http://localhost:5000/

Give same prefix input as in Part 1.


