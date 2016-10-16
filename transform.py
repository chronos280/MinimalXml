import xml.etree.ElementTree as ET

tree = ET.parse('SampleXML.xml')
root = tree.getroot()
print(root.tag)	
def childnodes (nodes, value):
	for subs in nodes:
		print(value + "/" +	 subs.tag)
		subsubs=subs.findall("./")
		childnodes(subsubs,value + "/" +	 subs.tag)
		
childnodes(root,root.tag)