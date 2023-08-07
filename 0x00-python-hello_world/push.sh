pycodestyle $1
echo "Check Code Finish"
git add --chmod +x $1
git add *
git commit -m "Add File $1"
git push