# Types
Every value in Cardea is statically typed, inferred or not.

## Type List
A star (⭐) means the type is generally considered the one of the default types for a value type group, and any variable with a type that must be inferred will be inferred to that type.
### Integers
- `int64`: Signed 64-bit integer
- `int`, `int32`: Signed 32-bit integer ⭐
- `int16`: Signed 16-bit integer
- `int8`: Signed 8-bit integer
- `uint64`: Unsigned 64-bit integer
- `uint`, `uint32`: Unsigned 32-bit integer
- `uint16`: Unsigned 16-bit integer
- `uint8`: Unsigned 8-bit integer

### Floats
- `half`, `float16`: 16-bit (half-precision) floating-point number
- `float`, `float32`: 32-bit (single-precision) floating-point number ⭐
- `double`, `float64`: 64-bit (double-precision) floating-point number

### Booleans
- `bool`: 8-bit boolean value (`true` or `false`) ⭐

### Text
- `char`: A single ASCII character
- `str`: A sequence of characters ⭐

### Special Returns
- `void`: Indicates a function that returns no value

### Type Qualifiers
- `const`: Indicates a constant variable.
- `vola`: Indicates a volatile variable.