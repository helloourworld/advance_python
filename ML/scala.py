# -*- coding: utf-8 -*-

import codecs
import os
import shutil
import re





def replace_file(filename, pattern, repl):
    # backup the origin file.
    shutil.copyfile(filename, filename + '.bak')
    # replace file according replace regrex
    ptn = re.compile(pattern)
    with codecs.open(filename, 'r') as fo:
        temp = fo.read()
        re.sub(ptn, repl, temp)
        fo.close()
    with codecs.open(filename, 'w') as fw:
        fw.write(temp)
        fw.close()
    return "0"


def main(filetype):
    for root, dirs, files in os.walk(os.getcwd()):
        for f in files:
            if f.lower().endswith(filetype):
                filename = os.path.join(root, f)
                try:
                    replace_file(filename, r'description: *\n', """\1 catalog: yes""")
                    print filename + ': replace successfully!'
                    print 'Orign:', orign, '\nNow:', now, '\n'
                except Exception, e:
                    print filename, e


if __name__ == '__main__':
    os.chdir("C:\\Users\\david\\Desktop\\test")
    main('.md')
