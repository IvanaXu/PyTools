import mistune

content = """
# Data
|A|B|
|-|-|
|1|2|
# View
* 123
"""

with open("124.Test_Mistune.html", "w") as f:
    f.write(mistune.html(content))
