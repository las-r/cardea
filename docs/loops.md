# Loops (while / do / for)
## While
While loops are defined with the following template:
```rb
while <CONDITION>
	<BODY>
end 
```
Here is an example:
```rb
const int stop = 10
int i = 0
while i < stop 
	print i
	i++ 
end
```
## Do
Do loops are defined with the following template:
```rb
do
	<BODY>
while <CONDITION>
```
## For
For loops are defined with the following templates:
```rb
for <INDEXVAR>, <ITEMVAR>, <ARRAY>
	<BODY>
end
```
Here is an example:
```rb
<str, 3> names = ["John", "Jack", "Bill"]
for _, name, names
	print name
end
```

