# Variables
Variables store data and are one of the most important concepts in programming.

In Cardea, variables are defined as:
```rb
<const> <TYPE> NAME = VALUE
```

The mutability (whether a variable is constant or not) and type do not necesarily need to be defined. If the mutability is not defined, it will assumed that the variable is mutable. The type, on the other hand, will be inferred based on the variables first value.

If a value is not given, the variable is empty. A variable cannot be empty without a type.

Here are a few examples:
```rb
str hello = "World"
hello = 4            # throws an error; int cannot be assigned to str

const num = 1        # inferred as integer
num = 2              # throws an error; var is immutable

pi = 3.14159         # inferred as float

str emptyvar
anotheremptyvar      # throws an error; empty var cannot be defined w/o type
```