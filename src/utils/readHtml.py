import os
import time
dir= os.path.abspath('.')
dir_name= os.path.basename(dir)
src =  os.path.abspath('src')

def read_arch_html():
    if dir_name != 'src':
        os.chdir(src)
        
    with open('index.html', 'r') as f:
        return f.read()


if __name__ == '__main__':
    print(dir)
    print(dir_name)