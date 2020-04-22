#!/usr/bin/zsh
# The style is the github markdown.
# https://github.com/sindresorhus/github-markdown-css

# get path of this file and src directory
src=`dirname $0`
# stylesheet absolute path
style=$src/style.css
pycmd=$src/md2html.py
echo $src

# get absolute path where this command executed
relativedirpath="${1%/*}"

if [ -d $relativedirpath ]; then
    cd $relativedirpath
fi
absdirpath=`pwd`

# get filename without extention
noextention_filenmae=`basename $1 .md`

# md to html
python $pycmd $absdirpath/$noextention_filenmae.md $absdirpath/$noextention_filenmae.html $style
echo "create $noextention_filenmae.html"

# html to pdf
# 2000 means 2000 mili seconds for javascript runnig time.
wkhtmltopdf --javascript-delay 2000 $absdirpath/$noextention_filenmae.html $absdirpath/$noextention_filenmae.pdf
echo "create $noextention_filenmae.pdf"

# rm html
#rm -f $absdirpath/$noextention_filenmae.html

exit 0
