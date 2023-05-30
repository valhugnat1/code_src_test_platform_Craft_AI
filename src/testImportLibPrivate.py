from chronyk import Chronyk

def testImportLibPrivate () : 
    t = Chronyk("May 2nd, 2016 12:51 am")
    print(t.ctime())