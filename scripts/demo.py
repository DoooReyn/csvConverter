#!/usr/bin/python
# -*- coding: utf-8 -*-
# fundInfo.py
# generated by multi_rename_suffix.py
#
import os
import sys
import csv
import types
sys.path.append('../')
import csv2lua_func as csv2lua
import csv2php_func as csv2php
reload(sys)
sys.setdefaultencoding('utf-8')

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
CSV_DIR  = ROOT_DIR+'/../csv/'
LUA_DIR  = ROOT_DIR+'/../lua/'
PHP_DIR  = ROOT_DIR+'/../php/'
CSV_FILE = 'demo.csv'
LUA_FILE = 'demo.lua'
PHP_FILE = 'demo.php'
CSV_ABS_PATH = CSV_DIR+CSV_FILE
LUA_ABS_PATH = LUA_DIR+LUA_FILE
PHP_ABS_PATH = PHP_DIR+PHP_FILE


def get_reader_keys(csvReader):
    for line in csvReader:
        header = []
        for key in line:
            header.append(key)
        return header

def do_convert_lua():
    filename,extendname = os.path.splitext(CSV_ABS_PATH)

    if os.path.isfile(CSV_ABS_PATH) and extendname == '.csv':
        csvReader = csv.reader(file(CSV_ABS_PATH, 'rt'))
        fp = csv2lua.get_lua_fp(LUA_ABS_PATH)
        if not fp:
            print(LUA_FILE + ' write error')
            return
        else:
            print(CSV_ABS_PATH)
            print(LUA_ABS_PATH)
            print('[converting] ' + CSV_FILE + ' => ' + LUA_FILE)
            csv2lua.write_lua_head(fp)
            keys = get_reader_keys(csvReader)
            for line in csvReader:
                for index in range(len(line)):
                    value = line[index]
                    if index == 0:
                        csv2lua.write_lua_key(value, fp)
                        fp.write(' {\n')
                        csv2lua.write_lua_key(keys[0],fp,2)
                        csv2lua.write_lua_value(line[0], fp)
                    else:
                        csv2lua.write_lua_key(keys[index],fp,2)
                        if keys[index] == 'target':
                            fp.write('{\n')
                            splitext = value.split('|')
                            for idx in range(len(splitext)):
                                splitext2 = splitext[idx].split('_')
                                fp.write('\t\t\t{ ')
                                for idx2 in range(len(splitext2)):
                                    if idx2 == 0:
                                        csv2lua.write_lua_key('condition',fp,0)
                                    elif idx2 == 1:
                                        csv2lua.write_lua_key('rewardid',fp,0)
                                    csv2lua.write_lua_value(splitext2[idx2],fp,False)
                                fp.write(' },\n')
                            fp.write('\t\t},\n')
                        else:
                            csv2lua.write_lua_value(line[index], fp)
                fp.write('\t},\n\n')
            csv2lua.write_lua_tail(fp)
        fp.close()

def do_convert_php():
    filename,extendname = os.path.splitext(CSV_ABS_PATH)
    csvbasename = os.path.basename(CSV_ABS_PATH)
    phpbasename = os.path.splitext(csvbasename)[0]

    if os.path.isfile(CSV_ABS_PATH) and extendname == '.csv':
        csvReader = csv.reader(file(CSV_ABS_PATH, 'rt'))
        fp = csv2php.get_php_fp(PHP_ABS_PATH)
        if not fp:
            print(PHP_FILE + ' write error')
            return
        else:
            print(CSV_ABS_PATH)
            print(PHP_ABS_PATH)
            print('[converting] ' + CSV_FILE + ' => ' + PHP_FILE)
            csv2php.write_php_head(phpbasename,fp)
            keys = get_reader_keys(csvReader)
            for line in csvReader:
                for index in range(len(line)):
                    value = line[index]
                    if index == 0:
                        csv2php.write_php_key(value,fp,2)
                        fp.write('\n')
                        csv2php.write_php_key(keys[0],fp,3)
                        csv2php.write_php_value(line[0],fp)
                    else:
                        csv2php.write_php_key(keys[index],fp,3)
                        if keys[index] == 'target':
                            fp.write('array(\n')
                            splitext = value.split('|')
                            for idx in range(len(splitext)):
                                splitext2 = splitext[idx].split('_')
                                csv2php.write_value_tab('array(',fp,4)
                                for idx2 in range(len(splitext2)):
                                    if idx2 == 0:
                                        csv2php.write_php_key('condition',fp,0)
                                    elif idx2 == 1:
                                        csv2php.write_php_key('rewardid',fp,0)
                                    csv2php.write_php_value(splitext2[idx2],fp,False)
                                csv2php.write_value_tab('),\n',fp,0)
                            csv2php.write_value_tab('),\n',fp,3)
                        else:
                            csv2php.write_php_value(line[index], fp)
                csv2php.write_value_tab('),\n\n',fp,2)
            csv2php.write_php_tail(fp)
        fp.close()


if __name__ == '__main__':
    if csv2lua.check_path(CSV_DIR) and csv2lua.check_path(LUA_DIR) and csv2lua.check_path(PHP_DIR):
        do_convert_lua()
        do_convert_php()