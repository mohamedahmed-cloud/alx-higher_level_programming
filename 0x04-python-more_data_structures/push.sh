pycodestyle $1
if [ $? -ne 1 ]; then
	echo "Style end"
	git add --chmod +x $1
	git add * 
	git commit -m "Add File $1"
	git push
fi