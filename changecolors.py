# This script switches out colors from a nodes file for use in hive plot html.  
#!/usr/bin/env python2

def strp (var):
	var = var.strip("\t")
	var = var.strip("\n")
	return var

print " "
name = raw_input("Enter nodes file (Enter for 'nodesd3formatted (colored by pathway type).csv'): ")
if len(name) == 0 : name = "nodesd3formatted (colored by pathway type).csv"
handle1 = open(name)
handle1.close()

n1=0
n2=0
nodes = list()
handle1 = open(name)
for line in handle1:
	line = strp(line)
	n1=n1+1
	if line [0:1] == "{": 
		line = line.split("p:")
		oldcolor = line[1]
		if oldcolor[0:1] == "1":
			newcolor = "2"
		elif oldcolor[0:1] == "2":
			newcolor = "5"
		elif oldcolor[0:1] == "3":
			newcolor = "13"
		elif oldcolor[0:1] == "4":
			newcolor = "8"
		elif oldcolor[0:1] == "5":
			newcolor = "9"
		elif oldcolor[0:1] == "6":
			newcolor = "10"
		elif oldcolor[0:1] == "7":
			newcolor = "17"
		remainingline = line[1]
		newline = "\t" + line[0] + "p:" + newcolor + remainingline[1:] 
		nodes.append(newline)
		n2=n2+1
	else:
		continue 
# formatneeded :   {source: nodes[0], target: nodes[17]},

n1=n1-2
print "Read %i lines, replaced %i colors" % (n1, n2)
print ""
print "var nodes = ["
for i in nodes: 
	print i
print "];"

print " "	
savename = raw_input("Save as (Blank to exit without saving, Enter d for 'linksd3formattednewColor.csv'): ")
if len(savename) == 0: quit()
if savename == "d": savename = "linksd3formattedNewColor.csv"
else: savename = savename + ".csv"
f = open(savename,'w')
f.write("var nodes = [\n")
for values in links:
	f.write(values)
	f.write("\n")
f.write("];")
f.close()
print "Saved as:", savename	
