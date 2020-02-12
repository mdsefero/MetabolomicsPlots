
# This program makes a list of links from the nodes created with the nodes fnodesd3.py output.CSV file. 
# The links generated can be copy/pasted into the d3 html program 

  
def strp (var):
	var = var.strip("\n")
	var = var.strip("\t")
	var = "".join(var.split())
	return var

print " "
name = raw_input("Enter nodes file (Enter for 'nodesd3formatted.csv'): ")
if len(name) == 0 : name = "nodesd3formatted.csv"
handle1 = open(name)
handle1.close()

n = 0	
dict = {}
handle1 = open(name)
for line in handle1:
	line = strp(line)
	if line[:1] == "{": 
		line = line.split("\"")
		key = line[1]
		dict[key] = n
		n = n + 1
		# parsing through lines like this {name:"HMDB01206M", group:4, x:3, y:0.339442123},
	else:
		continue
handle1.close()


print " "
name = raw_input("Enter the excel file with your matched links in 2 colums (Enter for 'links.csv'): ")
if len(name) == 0 : name = "links.csv"
handle2 = open(name)
handle2.close()


links = list()
handle2 = open(name)
for line in handle2:
	line = strp(line)
	line = line.split(",")
	if line[0] in dict.keys():
			source = str(dict[line[0]])
			target = str(dict[line[1]])
			source = r"[" + source + r"]"
			target = r"[" + target + r"]"
			newline = "\t{source: nodes%s, target: nodes%s}," % (source, target) 
			links.append(newline)
	else:
		print line, " Not found"  
		continue 
# formatneeded :   {source: nodes[0], target: nodes[17]},


print ""
print "var links = ["
for i in links: 
	print i
print "];"

print " "	
savename = raw_input("Save as (Blank to exit without saving, Enter d for 'linksd3formatted.cs'): ")
if len(savename) == 0: quit()
if savename == "d": savename = "linksd3formatted.csv"
else: savename = savename + ".csv"
f = open(savename,'w')
f.write("var links = [\n")
for values in links:
	f.write(values)
	f.write("\n")
f.write("];")
f.close()
print "Saved as:", savename	
	
