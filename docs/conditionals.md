# Conditionals (If)
If conditions are the backbone of every language's logic.

An if condition is defined with the following templates:
```rb
# If
if <CONDITION>
	<BODY>
end

# If/else
if <CONDITION>
	<BODY>
else
	<BODY>
end

# If/else if/else
if <CONDITION>
 <BODY>
else if <CONDITION>
	<BODY>
else
	<BODY>
end
```

An if condition returns the last expressed value. This allows for inline blocks such as this:
```rb
str cond = "yeah" if val else "nah"
str opt = 1 if num < 10 else 2 if num < 20 else 3  # nested inline blocks
```
When a block is inline, it does not need `end` to indicate the end of the block, though it is not strict on whether it's required or not.

