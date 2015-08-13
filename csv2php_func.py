import os
import csv
import types

def check_path(path):
    if not os.path.exists(path):
        print(path + ' does not exist')
        return False
    else:
        return True

def get_php_fp(phppath):
    fp = open(phppath, "wt")
    return fp

def write_php_head(filename, fp):
    fp.write('<?php\n')
    fp.write('namespace Project\Root;\n')
    fp.write('class '+filename+' {\n')
    fp.write('\tstatic public $list = array (\n')

def write_php_tail(fp):
    fp.write('\t);\n')
    fp.write('}\n')
    fp.write('?>\n')

def write_php_key(key, fp, tab=1):
    fp.write('\t'*tab)
    if key.isdigit():
        fp.write(key)
        fp.write(' => ')
        fp.write('array(')
    else:
        fp.write("'"+key+"'")
        fp.write(' => ')

def write_php_value(value,fp,isNewLine=True):
    if value.isdigit():
        fp.write(value)
    else:
        fp.write("'")
        fp.write(value)
        fp.write("'")
    fp.write(',')
    if isNewLine:
        fp.write('\n')

def write_value_tab(value, fp, tab=1):
    fp.write('\t'*tab)
    fp.write(value)
