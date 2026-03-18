from pathlib import Path

n = 0
for f in Path('..').glob('**/*.ipynb'):
    print(f.parts[-1])
    n += 1

print(f'Total number of notebooks: {n}')
