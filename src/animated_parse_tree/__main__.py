from .parse_tree import ParseTree


command = input('?> ')
while command != '':
    tokens = command.split(' ')
    key = tokens[0]
    expression = ' '.join(tokens[1:])
    t = ParseTree()
    t.read(expression)
    if key in {'eval', 'evaluate', 'calc', 'calculate'}:
        print(expression, '=', t.evaluate())
    elif key in {'show', 'display',  'vis', 'viz', 'visualise', 'visualize'}:
        print(expression, '>>>')
        print(str(t))
