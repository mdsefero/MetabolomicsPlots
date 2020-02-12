
# This program formats .CSV file formated by number and axis and value into a format for nodes in HTML program D3


  
def strp (var):
	var = var.strip("\n")
	var = "".join(var.split())
	return var

print " "
name = raw_input("Enter file to append string (Enter for 'fornodesd3.csv'): ")
if len(name) == 0 : name = "fornodesd3.csv"
handle1 = open(name)
handle1.close()


list = list()
list.append("var nodes = [")
handle1 = open(name)
for line in handle1:
	line = strp(line)
	line = line.split(",")
	
	# formatneeded :   {name:"A", group:1, x: 0, y: .1},
	
	
	newline = "\t{name:\"%s\", group:%s, x:%s, y:%s}," % (line[1], line[2], line[0], line[3]) 
	list.append(newline)
handle1.close()
list.append("];")

print ""
for i in list: 
	print i

print " "	
savename = raw_input("Save as (Blank to exit without saving, Enter d for 'nodesd3formatted.cs'): ")
if len(savename) == 0: quit()
if savename == "d": savename = "nodesd3formatted.csv"
else: savename = savename + ".csv"
f = open(savename,'w')
for values in list:
	f.write(values)
	f.write("\n")
f.close()
print "Saved as:", savename	
	
