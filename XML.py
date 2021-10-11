#XML 1 - Find the Score



def get_attr_number(node):
    # your code goes here
    count = 0
    for i in node.iter():
        count += len(i.attrib)
    return count

#XML2 - Find the Maximum Depth



maxdepth = 0
def depth(elem, level):
    global maxdepth
    if(level == maxdepth):
        maxdepth += 1
    
    for x in elem:
        depth(x,level+1)
    # your code goes here

