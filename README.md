# eol-r

A cmd tool to convert line endings (EOL = end of line) from DOS to UNIX and vice-versa.

https://github.com/uuencode/eol-r

This script converts line endings from DOS to Unix and vice-versa: CRLF to LF OR LF to CRLF
You can convert a single file or multiple files in multiple directories recursively.

![Alt text](/eol-r.gif "void")


## HOW TO INSTALL

Download, make eol-r.py executable and run it from terminal.

## HOW TO USE

Call this script with 2 arguments:

 `PATH-TO/eol-r.py dos2unix file-name` or `PATH-TO/eol-r.py dos2unix dir-name`

* The 1st argument is either dos2unix or unix2dos
* The 2nd argument must be a full path to a single file or a directory.
* If a directory is set as a second argument, it is searched recursively for non-binary files and any non-binary file found is converted! Make a backup first!
* UTF-16 encoded files are considered binary.
* it's unix2dos and dos2unix only - if you have old Mac files with CR EOLs you'll end up with no EOLs at all!
* You need to have Read and Write permissions on the files/directories you are about to convert!
