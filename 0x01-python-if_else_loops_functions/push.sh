pycodestyle $1
echo "Code style End"
git add --chmod +x $1
git add *
git commit -m "Add File $1"
git push 