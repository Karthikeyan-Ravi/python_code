def add(arg1,arg2):
    print "in function add"
    print "argument1 =" + str(arg1) + "argument2 =" + str(arg2)
    print "argument1 = "+str(arg1)
    print "argument2 = "+str(arg2)
    result = arg1 + arg2
    return result




if __name__=='__main__':
    #print "argument1 ="+str(arg1) + "argument2 ="+str(arg2)
    print "adding two arguments of any data type"
    result = add(5,6)
    print result
    result = add("ashok ","marannan")
    print result
