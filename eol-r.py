#!/usr/bin/python

'''

eol-r

https://github.com/uuencode/eol-r

This script converts line endings from DOS to Unix and vice-versa.
You can convert a single file or multiple files in multiple directories recursively.
Run it without any arguments to see how to use it.

'''

import sys, os, time

# colors
colppl='\033[95m'
colblu='\033[94m'
colgre='\033[92m'
colyel='\033[93m'
colred='\033[91m'
colbld='\033[1m'
colend='\033[0m'

# checks if a file is text or binary
def istxt(f):
	f=open(f,'rb')
	if b'\x00' in f.read(): return False
	else: return True

# converts line endings of a single file from dos to unix
def dos2unix(f):
	t=open(f,'rb').read().replace('\r\n','\n')
	open(f,'wb').write(t)

# converts line endings of a single file from unix to dos
def unix2dos(f):
	t=open(f,'rb').read().replace('\r','')
	t=t.replace('\n','\r\n')
	open(f,'wb').write(t)

# calls the appropriate function based on sys.argv[1]
def converteol(f):
	if sys.argv[1] == 'dos2unix': dos2unix(f)
	else: unix2dos(f)

# timestamp im miliseconds
def tstamp():
	return round(time.time()*1000)

# --------------------

# clear the screen
os.system('clear')

# print title
print '\n '+colbld+'eol-r'+colend+' (Line endings from DOS to Unix {'+colbld+'\\r\\n -> \\n'+colend+'} and vice-versa)'

# if no arguments print some help
if len(sys.argv)<3: 
	print '\n You have to call this script with 2 arguments:\n'
	print ' '+colyel+'eol-r.py dos2unix file-name'+colend+' or '+colyel+'eol-r.py dos2unix dir-name'+colend
	print '\n - The 1st argument is either dos2unix or unix2dos'
	print ' - The 2nd argument must be a full path to a single file or a directory.'
	print ' - If a directory is set as a second argument, it is searched recursively for non-binary files'
	print '   and any non-binary file found is converted! Make a backup first!'
	print ' - You need to have Read and Write permissions on the files/directories you are about to convert!\n'; exit()
	
# if argv[1] not recognized print error
if sys.argv[1]!='dos2unix' and sys.argv[1]!='unix2dos':
	print '\n '+colred+'ERROR: The first argument should be dos2unix or unix2dos!'+colend+'\n'; exit()

# if argv[2] is not file/folder print error
if not os.path.isfile(sys.argv[2]) and not os.path.isdir(sys.argv[2]):
	print '\n '+colred+'ERROR: The second argument should be a full path to a file or a directory!'+colend+'\n'; exit()

# change the success message based on argv[1]
if sys.argv[1]=='dos2unix': successmsg='EOL converted from DOS to Unix'
else: successmsg='EOL converted from Unix to DOS'

# --- convert a single file: begin --- #
if os.path.isfile(sys.argv[2]): # if argv[2] is a file and NOT dir
	fname='\n '+colbld+sys.argv[2]+colend

	if not istxt(sys.argv[2]):  # if argv[2] is binary
		print  fname
		print colred+' This file is a binary file and cannot be converted.'
		print ' Note that UTF-16 encoded files are considered binary.'+colend+'\n'; exit()

	converteol(sys.argv[2])
	print fname,'\n'
	print colblu, successmsg,colend+'\n'; exit()
# --- convert a single file: end --- #

# convert multiple files

starttime=tstamp()

filepaths=[] # list of filepaths to convert
fconverts=[] # successfully converted
fskippeds=[] # skipped (binary)

# build a list of files to convert
for folder, subs, files in os.walk(sys.argv[2]):
	for filename in files:
		filepaths.append(os.path.abspath(os.path.join(folder, filename)))

# remove 'self' if exists
if sys.argv[0] in filepaths: filepaths.remove(sys.argv[0])

# process the files in a loop and add entries to fconverts and fskippeds
for entry in filepaths:
	if istxt(entry): # check if binary or text
		converteol(entry); fconverts.append(entry)
	else: fskippeds.append(entry)

totaltime=(tstamp()-starttime)/1000

# print result

fcountc=len(fconverts); fcounts=len(fskippeds); 

print '\n '+colbld+sys.argv[2]+colend
print '\n '+colblu+successmsg+colend+'\n'
print colgre,fcountc,'text files converted...'+colend
print colred,fcounts,'binary files skipped...'+colend
print ' execution time:',totaltime,'sec'
print '\n'

# show log
showlog=raw_input(' Would like to see a log (y) or (n): ')
if(showlog!='y'): print '\n'; exit()

fconverts='\n'.join(fconverts)
fskippeds='\n'.join(fskippeds)

print '\n'
print colgre+fconverts+colend
print colred+fskippeds+colend
print '\n'
