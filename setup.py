import sys
import os
import shutil
reload(sys)
sys.setdefaultencoding('utf-8')

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
PY_DIR   = os.path.join(ROOT_DIR,'scripts')
CSV_DIR  = os.path.join(ROOT_DIR,'csv')
LUA_DIR  = os.path.join(ROOT_DIR,'lua')

def check_path(path):
    if not os.path.exists(path):
        print(path + ' is not set')
        return False
    else:
        return True

def do_python_cmd(path):
    print('do_python_cmd:' + path)
    for root, dirs, files in os.walk(path):
        for filename in files:
            if filename.endswith(".py"):
                if not filename == 'csv2lua_func.py':
                    os.system('python ' + os.path.join(root,filename))
                    print('python ' + filename)
                else:
                    print('csv2lua_func.py is used by other .py files')
            else:
                print('files not found')

if __name__ == '__main__':
    if check_path(PY_DIR) and check_path(CSV_DIR) and check_path(LUA_DIR):
        do_python_cmd(PY_DIR)
    else:
        print('dir not found')
