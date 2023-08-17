pycodestyle $1
if [ $? -ne 0 ]; then
	echo "Code Style End"
	git --chmod +x $1
	git add * 
	git commit -m "Add File $1"
	git push
	
fi