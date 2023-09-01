git add --chmod +x $1
pycodestyle
if [ $? -ne 1 ]; then
	git add *
	git commit -m "Add File $1"
	git push
fi
