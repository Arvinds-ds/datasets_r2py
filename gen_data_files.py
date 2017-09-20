from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import tempfile
import pandas as pd
import re
import io
import os
import jinja2

# parse rst file. to revisit. Dont judge!!!
def parse_rst(filename):
    with open(filename) as f:
        title_start = 0
        desc_line_start = 0
        desc_line_end = 0
        format_start = 0
        format_end = 0
        details_start=0
        details_end=0
        source_start = 0
        source_end=0
        final_line = 0
        for i,line in enumerate(f):
            title_start=4
            if line.strip() == 'Description':
                desc_line_start = i + 2
            if line.strip()=='Usage':
                desc_line_end = i - 1
            if line.strip()=='Format':
                if desc_line_end == 0:
                   desc_line_end = i - 1 
                format_start = i + 2
            if line.strip()=='Details':
                if desc_line_end == 0:
                   desc_line_end = i - 1 
                if format_start >0:
                    format_end = i-1;
                details_start= i+2
            if line.strip()=='Source':
                if desc_line_end == 0:
                   desc_line_end = i - 1 
                if format_end == 0:
                    format_end = i-1;
                if details_start > 0:
                    details_end = i-1
                source_start = i+2
            if line.strip()=='References':
                source_end = i - 1
                if format_end == 0:
                    format_end = i-1;
            if line.strip()=='Examples':
                if source_end ==0:
                    source_end = i - 1
                if format_end == 0:
                    format_end = i-1;
            final_line = i
        if source_end == 0:
            source_end = final_line
        if format_end == 0:
            format_end = final_line
    extract_dict = {'title': title_start,
    'desc_start': desc_line_start,
    'desc_end': desc_line_end,
    'format_start': format_start,
    'format_end': format_end,
    'source_start': source_start,
    'source_end': source_end,
    'final_line': final_line,
    'file_name': filename
    }
    for k,v in extract_dict.items():
        if k in ['title', 'desc_start', 'desc_end'] and v == 0:
            print(filename)
            print(k)
            raise Exception
        
    return extract_dict

def extract_rst(extract_dict):
    output = ''
    indent='  '
    with open(extract_dict['file_name']) as f:
        for i,line in enumerate(f):
            if i == extract_dict['title']:
                #print(line)
                output+=line
            if i >= extract_dict['desc_start'] and i < extract_dict['desc_end']:
                #print(line)
                if line == '\n':
                    output+= line
                else:
                    output+=indent+line
            if extract_dict['format_start'] > 0:
                if i >= extract_dict['format_start'] and i < extract_dict['format_end']:
                    #print(line)
                    if line == '\n':
                        output += line
                    else:
                        output += indent + line
            if extract_dict['source_start'] > 0:
                if i >= extract_dict['source_start'] and i < extract_dict['source_end']:
                    #print(line)
                    if line == '\n':
                        output += line
                    else:
                        output += indent + line
        output=output.replace('``','`')
    return output

def gen_context(row):
    package = row['Package']
    function = row['lcitems']
    rst_loc = 'doc/' + package + '/rst/' + row['Item'] +'.rst'
    if not os.path.exists(rst_loc):
       rst_loc = 'doc/' + package + '/rst/' + row['Item'].lower() +'.rst'
    try:
        rows = int(row['Rows'])
    except ValueError:
        print(function)
        rows=''
    try:
        cols = int(row['Cols'])
    except ValueError:
        print(function, rst_loc)
        cols=''
    url = row['csv']
    if len(url) > 62:
        url = url[:62] + "' \\\n" + " "*10 + "'" + url[62:]
    file_name = row['lcitems'] + '.csv'
    try:
        desc = extract_rst(parse_rst(rst_loc))
    except:
        print('Exception occured at : ', rst_loc)
        return None
    context = {'function': function,
               'desc': desc,
               'rows': rows,
               'cols': cols,
               'url': url,
               'file_name': file_name,
              }
    return context

def render(tpl_path, context):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path or './')
    ).get_template(filename).render(context)

def gen_data_test_files(row, file_path='./', test_file_path='./'):
    context = gen_context(row)
    if context is None:
        return
    file_str = render('./template.tpl', context)
    test_file_str = render('./test_template.tpl', context)
    with open(os.path.join(file_path,context['function']+'.py'), 'w') as f:
        f.write(file_str)
    with open(os.path.join(test_file_path,
                           'test_'+context['function']+'.py'), 'w') as f:
        f.write(test_file_str)

def gen_init_file(dataset, path, import_prefix='observations.rdata'):
    def import_names(x):
        return 'from ' + import_prefix + '.' + x + ' import ' + x

    def allowed_modules(x):
        return "    '" + x + "'"
 
    function_imports='\n'.join(dataset.lcitems.map(import_names))
    allowed_symbols=',\n'.join(dataset.lcitems.map(allowed_modules))
    init_file_str=render('./init_template.tpl',
                         {'function_imports': function_imports,
                          'allowed_symbols': allowed_symbols})
    with open(os.path.join(path, '__init__.py'), 'w') as f:
        f.write(init_file_str)
    
    

def gen_data_test_files_from_csv(file, src_path, test_path,
                                 import_prefix='observations.rdata'):
    if not os.path.exists(src_path):
        os.makedirs(src_path)
    if not os.path.exists(test_path):
        os.makedirs(test_path)
    datasets = pd.read_csv(file, encoding='ISO-8859-1')
    gen_init_file(datasets, src_path)
    for i in range(datasets.shape[0]):
        gen_data_test_files(datasets.iloc[i],src_path, test_path)
    
    
if __name__ == "__main__":
    gen_data_test_files_from_csv('datasets_mod.csv', './observations/rdata/',
                               './observations/rdata/tests/')
