#!/usr/bin/env python3

import pathlib

pendings = [pathlib.Path('/home')]
resolved = []
errors = []

while len(pendings) != 0:
	p = pendings.pop()
	for i in p.iterdir():
		try:
			if i.is_dir():
				pendings.append(i)
			else:
				resolved.append(i)
		except:
			print('errors ' + str(i))
			errors.append(i)

print(resolved)
print(len(resolved))