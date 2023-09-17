git add --chmod +x $1

pycodestyle $1

if [  $? -ne 1 ]; then
	git add *
	git commit -m "add file $1"
	git push
fi