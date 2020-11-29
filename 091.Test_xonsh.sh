# Xonsh is the Shell. 
cat /etc/passwd|head -n 1
ls /

# Xonsh is Python.
2 + 2
import json
json.dumps({"sum": 21+21})

# Xonsh is the Shell in Python.
for i in range(0, 10):
	echo -e @(i)|grep 5

# Xonsh is Python in the Shell.
var = 'he' + 'llo'
echo @(var)|sed 's/he/a/'
