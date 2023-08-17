pycodestyle $1
if [ $? -ne 1 ];then
	git add --chmod +x $1
	echo "Style Ended"
	git add *
	git commit -m "add File $1"
	git push
fi
