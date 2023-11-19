import argparse
# import sqlparse

from jinja2 import Template
    
parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("output")
args = parser.parse_args()

def read(filename):
    with open(filename, 'r') as f:
        content = f.read()
    return content
 
with open(args.input, 'r', encoding='utf8') as f:
    templateContent = f.read() 

template = Template(templateContent)
template.globals['read'] = read
    
with open(args.output, 'w', encoding='utf8') as f:
    output = template.render()
    # if args.output.endswith('.sql'):
        # output = sqlparse.format(output, reindent=True, keyword_case='upper')
    f.write(output) 
