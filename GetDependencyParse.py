import os
import re
sentence = "children are roses."

os.popen("echo '"+sentence+"' > ~/Documents/stanfordtemp.txt")
parser_out = os.popen("~/softwares/stanford_parser/lexparser.sh ~/Documents/stanfordtemp.txt").readlines()
#print parser_out
print "---"
dependency_parse=[]
for i in parser_out:
	 if len(i.strip()) > 0 and i.strip()[0] != "(":
		line=i.strip()
		dependency_parse.append(filter(lambda x:x.isalpha(),re.findall(r"[\w']+", line)))
		
print dependency_parse
