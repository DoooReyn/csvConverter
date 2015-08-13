import os
import csv
import types

def check_path(path):
    if not os.path.exists(path):
        print(path + ' does not exist')
        return False
    else:
        print(path + ' exists')
        return True

def get_lua_fp(luapath):
    fp = open(luapath, "wt")
    return fp

def write_lua_head(fp):
    fp.write('local data = {\n')

def write_lua_tail(fp):
    fp.write('}\n\nreturn data')

def write_lua_key(key, fp, tab=1):
    fp.write('\t'*tab)
    if key.isdigit():
        fp.write('[')
        fp.write(key)
        fp.write(']')
    else:
        fp.write(key)
    fp.write(' = ')

def write_lua_value(value, fp, isNewLine=True):
    if value.isdigit():
        fp.write(value)
    else:
        fp.write('"')
        fp.write(value)
        fp.write('"')
    fp.write(',')
    if isNewLine:
        fp.write('\n')
