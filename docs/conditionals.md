# Conditionals
## Basic Definition
An if condition is defined with the following templates:
```rb
# If
if CONDITION
	BODY
end

# If/else
if CONDITION
	BODY
else
	BODY
end

# If/else if/else
if CONDITION
 	BODY
else if CONDITION
	BODY
else
	BODY
end
```

## Inline Definition
An if condition can be written inline as well, using the following templates:
```rb
# If
NAME = VALUE if CONDITION  # Sets var to nil if cond isn't true

# If else
NAME = VALUE if CONDITION else VALUE
```
Inline blocks can be nested to create elseif logic, as the block itself evaluates to a single expression. However, the use of nested inline if blocks is generally disliked as it hurts code readability. Using basic if blocks is highly recommended when elseif is needed.