# DEFINITIONS
## Variable
    Variable is a named storage location that holds a value.
        Name: A unique identifier for the variable.
        Value: The data stored in the variable.
        Data type: The type of data the variable can hold (e.g., integer, string, boolean).

## Type Casting
    Type Casting is the process of converting a variable from one data type to another
    e.g., str(), int(), float(), bool()

## Input Data
    input() is a function that prompts the user to enter data
    Returns the entered data as a String

## if
    Do some code only IF some condition is True
    Else do something else

## Logical Operators
    Evaluate multiple conditions (or, and, not)
    or = at least one condition must be true
    and = both condistion must be true
    not = inverts the condition (not false, not true)

## Conditional expression
    A one-line shortcut for the if-else statement (ternary operator)
    Print or assign one of two values based on a condition
    X if condition else Y

## String Method
    Built-in functions that allow you to perform various operations on strings

## Indexing
    accessing elements of a sequence using [] (indexing operator)
    [start:end:step]

## Format Specifiers
    {:flags} format a value based on what flags are inserted
        .(number)f = round to that many decimal places (fixed point)
        :(number) = allocate that many spaces
        :03 = allocate and zero pad that many spaces
        :< = justify left
        :> = justify right
        :^ = justify center
        :+ = use a plus sign to indicate positive value
        := = place sign to leftmost position
        :  = insert a space before positive numbers
        :, = comma separator
## While Loop
    Execute some code WHILE some condition remains true

## For loops
    Execute a block of code a fixed number of times.
    You can interate over a range, string, sequence, etc.

## Nested Loop
    A loop within another loop (outer, inner)
        outer loop:
            inner loop:

## Collection
    single variable used to store multiple values
        List    = [] ordered and changeable. Duplicates Ok
        Set     = {} unordered and immutable, but Add/remove OK.
        Tuple   = () ordered and unchangeable. Duplicates Ok. Faster

## 2D Collection
    Is a collection that's made up of collections

## Dictionary
    A collection of {key:value} pairs ordered and changeable.
    No duplicates

## Function
    A block of reusable code
    place () after the function name to invoke it

## Default Arguments
    A default value for certain parameters default is used when that argument is omitted make your functions more flexible, reduces # of arguments.
    1. Positional, 2. DEFAULT, 3. Keyword, 4. Arbitary

## Keyword Arguments
    An argument preceded by an identifier helps with readability, order of arguments is doesn't matter

## args & kwargs
    *args allows you to pass multiple non-key arguments
    **kwargs allows you to pass multiple keyword arguments

## Iterables
    An object/collection that can return its elements one at a time, allowing it to be iterated over in a loop
    e.g. tuple, list, set, dictionary

##  Membership operators
    Used to test whether a value or variable is found in a sequence (String, list, tuple, set or dictionary)
    1. in
    2. not in

## List comprehension
    A concise way to create lists in Python compact and easier to read than traditional loops.
    [expression for value in interable if condition]

# ANY TIPS
## print(f{variable})
    use f in print so we can call the variable inside the quotes.
    ex. print(f"{name}") it has the same result as print(name)

## str to int
    if the string contains non-numerical characters, it will not be converted to an integer.

## operation float and int
    it is possible to multiply a float by an integer in math. When a float is multiplied by an integer, the result is a float.

## Import Math
    import module, making its functions and constants available for use

## uses of equals
    a single equals sign (=) is used for assignment value
    a double equals sign (==) is used for equality comparison.

## str.find() not found
    if the substring is not found, whereas find() just returns -1.

## use help
    use help() or dir() to shows help of what attributes and what can the syntax do.

## argument(s)
    when you define a function, you can also to put argument into that function, e.g. birthday(age), age is the argument, it can pass data/value into the function to be processed later.

## return 
    statement used to end a function and send a result back to the caller