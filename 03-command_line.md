# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> > pwd: 'print working directory' - shows current working directory path
mkdir: 'make directory' - makes a new folder
rmdir: 'remove directory' - deletes a folder
touch: creates an empty file (usage: 'touch file.txt' creates an empty file)
rm: 'remove' - deletes a file 
rm -r: 'remove recursively' - deletes a folder and all its contents
mv: 'move' - can be used to move a file to a new directory (i.e. 'mv filename directoryname') or to rename (i.e. 'mv filename newname')
cp: 'copy' - copies a file ('cp filename1 filename2' copies the file to same directory with new name, 'cp filename directoryname/ copies the file to named directory)
ls -a: 'list -all' - shows all files in a directory, even hidden ones

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > ls: lists files \
ls -a: lists all files \
ls -l: lists files in "long listing format" 
ls -lh: same, but supposedly in a human readable format or something? In terms of print size? 
ls -lah: lists all files in long listing format in human readable format
ls -t: lists files in a directory, sorted by time of modification
ls -Glp: lists files in long form, with folders highlighted in blue. The -G flag appears to override the -p flag, which would mark the folders with a / 


---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > ls -R
ls -a 
ls -l
ls -m 
ls -t

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > xargs allows the user to output the product of one command into another command by breaking the output of the first command into smaller pieces so that it can be fed to another command one at a time. 
 

