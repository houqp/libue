#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import print_function

import os
from subprocess import check_call


with open('../README.md') as readme:
    found_code = False
    code_lines = []
    for line in readme:
        if '```C\n' == line:
            found_code = True
            continue
        elif '```\n' == line:
            break
        else:
            if found_code:
                code_lines.append(line)
    sample_code = ''.join(code_lines)

print('Extracted sample code:')
print(sample_code)

tmp_file = 'libue-test.c'

with open(tmp_file, 'w') as fd:
    fd.write(sample_code)

print('Building sample code...')
check_call(['gcc', '-I../', '-o', 'libue-test', tmp_file])

os.remove(tmp_file)
os.remove('libue-test')

print('Done.')
