git add --chmod +x $1
pycodestyle $1
if [ $? -ne 1 ]; then
	git add *
	git commit -m "Add File $1"
	git push
fi