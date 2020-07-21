# Bash script to run all python files
echo "Running all python files"
for f in *.py; do echo "Running $f" & python "$f"; done
exit 0
