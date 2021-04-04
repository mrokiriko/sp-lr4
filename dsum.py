#! /usr/bin/env python
# -*- coding: utf-8 -*-
# чтобы не ругался на русские комментарии

import subprocess
import sys
from os import walk
import sys
import hashlib

if (len(sys.argv) < 2):
	raise Exception('no directory provided, use cli argument')
	exit()

mypath = sys.argv[1]

f = []
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)
    break

sha1 = hashlib.sha1() # для подсчета хэша самой директори

for filename in filenames:

	filepath = dirpath + filename # составим относительный путь до файла

	# вызов процесса для подсчета хэша одного файла
	result = subprocess.run(
		[sys.executable, "fsum.py", filepath], capture_output=True, text=True
	)
	if (result.stderr):
		print("Error occured: " + result.stderr)
		exit()

	filehash = result.stdout.strip()

	sha1.update(filehash.encode())

	print(" - hashsum for file " + filename + " is " + filehash)

print("hash for directory " + mypath + " is " + sha1.hexdigest())
