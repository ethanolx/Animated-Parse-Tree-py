from .parse_tree import ParseTree


# REPL Simulation
def main():
    '''
    Runs the animated_parse_tree program interactively

    Parameters
    ----------
    **kwargs
        Keyword arguments to be passed to ParseTree().animate.

    Commands
    --------
    Evaluate an expression
        'eval', 'evaluate', 'calc', 'calculate'
    Display the parse tree for an expression
        'show', 'display',  'vis', 'viz', 'visualise', 'visualize'

    Returns
    -------
    None
        This program does not return anything.

    Examples
    --------
    ```bash
    ?> display 1 + 2
     +
    / \\
    1 2

    ?> evaluate 1 + 2
    1 + 2 = 3
    ```
    '''
    command = input('?> ')
    while command not in ('', 'exit', 'quit'):
        tokens = command.split(' ')
        key = tokens[0]
        expression = ' '.join(tokens[1:])
        t = ParseTree()
        t.read(expression)
        if key in {'eval', 'evaluate', 'calc', 'calculate'}:
            print(expression, '=', t.evaluate())
        elif key in {'show', 'display',  'vis', 'viz', 'visualise', 'visualize'}:
            print()
            print(str(t))
        else:
            raise ValueError(f'Unknown command {key} encountered')
        command = input('?> ')
    print('Bye :)')


if __name__ == '__main__':
    main()