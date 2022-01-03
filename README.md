# Animated Parse Tree

|               |                   |
|---------------|-------------------|
|   Author      |   Ethan Tan       |
|   Date        |   11/12/2021      |
|   Language    |   Python (py)     |

## Description

This package is meant to provide a high-level API for programmers to visualise parse trees. The eventual goal is to animate the tokenization (extracting symbols from a string), lexing (formatting the tokens), parsing (building the parse tree) and evaluation (reducing the parse tree).

## Setup

It is extremely easy to integrate this package in your existing projects.

In the command line, run:

```console
pip install animated_parse_tree
```

## Sample Usage

### From Command Line

Then in your terminal/shell, enter:

```console
python -m animated_parse_tree
```

The output should look similar to the following:

```console
Greetings...

                "This is a utility program which aims
                    to show the beauty of parse trees
                           in a fun and engaging way"

Don't be intimidated :)
It was designed to be easy to use, yet extensible.

                                               Enjoy!
?>
```

Enter 'help' to display the help menu or 'mode' to change your current mode

### From Source Files

Then in your Python source file / Jupyter Notebook, insert:

```python
from animated_parse_tree import ParseTree

# Instantiate Parse Tree Object
t = ParseTree()

# Read a Mathematical String Expression (separated by singular whitespace characters)
t.read('1 + 2 * 3')

# Retrieve the Result
print('<<< Equation >>>')
print(t.expression, '=', t.evaluate(), end='\n\n')

# Display the Parse Tree
print('<<< Parse Tree >>>')
print(str(t))
```

The output in the terminal will look something like this:

```console
<<< Equation >>>
1 + 2 * 3 = 7

<<< Parse Tree >>>
 +
/  \
1  *
  / \
  2 3
```

## Declaring Custom Operands/Operators

A `Bundle` is simply a list of Operands and/or Operators.

To extend functionality, one simply has to register their own custom operands/operators like so:

```python
# Instantiate Parse Tree Object
t = ParseTree()

# Declaring Custom Operator
op = Operator(symbol='if', func=lambda a,b,c: b if a == 1 else c, priority=7, kind='pre', operands=3)

# Register the Custom Operator(s)
t.register(bundle=[op])

# Use it in Expressions
t.read('if(1, 8, -1)')
print(t.evaluate())
```

## Current Support

* Operands
    * Integers
    * Floats
    * Constants (like pi, e, etc.)
* Operators
    * Unary
        * Pre-fix
        * Post-fix
    * Binary
        * Pre-fix
        * In-fix
    * Multi
        * Pre-fix
* Parentheses
    * Unlimited nesting permitted
    * Not encouraged for animation currently