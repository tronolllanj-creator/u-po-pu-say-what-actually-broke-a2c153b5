import os

"""Entry for make.fun bounty u-po-pu-say-what-actually-broke-a2c153b5.

Writes one line of software error copy (at most 200 characters
including the trailing newline) to $MAKEFUN_OUTPUT_DIR/entry.txt.
The line tells the user the brutal truth about what broke and makes
them laugh, naming the failure and what to do next.
"""

LINE = "The payment posted twice because your code let the button be clicked twice; refund the user now and add a debounce timer so you stop charging people for their own misclicks.\n"

content = LINE

if not (1 <= len(content) <= 200 and content.strip()):
    raise ValueError("content must be 1 to 200 characters total and not only whitespace")

output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', 'out')
os.makedirs(output_dir, exist_ok=True)

output_path = os.path.join(output_dir, 'entry.txt')

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(output_path)
print(len(content))