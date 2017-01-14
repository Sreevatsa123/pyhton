name1=" "
name2=" "
def simply():
    print "Enter the name1"
    global name1
    name1=raw_input()
    print "Enter the name2"
    global name2
    name2=raw_input()
    print "i am %s and he is %s"%(name1,name2)
    
def simply1():
    print "HI %s and HI %s"%(name1,name2)
    


simply()
simply1()
