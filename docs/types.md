# Types
Every value in Cardea is statically typed, inferred or not.

## Core Data Types
| Type | Description | C Equivalent | Default Value |
| :--- | :--- | :--- | :--- |
| `int` | 64-bit signed integer | `int64_t` | `0` |
| `flt` | 64-bit floating point | `double` | `0.0` |
| `str` | UTF-8 String (Managed pointer) | `char*` | `NULL` / `""` |
| `bit` | Boolean value (`true`/`false`) | `bool` | `false` |
| `void` | Return type for non-returning functions | `void` | N/A |
| `<T, S>` | Contiguous memory of type `T` and size `S` | `T*` | `NULL` |

## Reserved Keywords
### **Declaration & Flow**
* `const`: Defines an immutable variable.
* `return`: Exits a function and returns a value.
* `if`: Conditional branch.
* `else`: Alternative conditional branch.
* `end`: Closes a multi-line function or logic block.
* `while` / `for`: Loop constructs.

### **Built-in Operations**
* `print`: Output to stdout (handled by `runtime/core.c`).
* `input`: Read from stdin.
* `use`: Include a library