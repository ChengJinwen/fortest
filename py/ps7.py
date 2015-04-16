# -*- coding: utf-8 -*-
class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before
    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name

def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links 
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
    """
    tmp1 = atMe
    tT = True
    if atMe.name[0] < newFrob.name[0]:
        while tmp1.name[0] < newFrob.name[0]:
            if tmp1.after == None:
                tmp1.setAfter(newFrob)
                newFrob.setBefore(tmp1)
                tT = False
                break
            else:
                tmp1 = tmp1.after
        if tT:
            if tmp1.after == None and tmp1.name[0] < newFrob.name[0]:
                tmp1.setAfter(newFrob)
                newFrob.setBefore(tmp1)
            else:
                tmp2 = tmp1.before
                tmp1.setBefore(newFrob)
                tmp2.setAfter(newFrob)
                newFrob.setBefore(tmp2)
                newFrob.setAfter(tmp1)
    elif atMe.name[0] > newFrob.name[0]:
        while tmp1.name[0] > newFrob.name[0]:
            if tmp1.before == None:
                tmp1.setBefore(newFrob)
                newFrob.setAfter(tmp1)
                tT = False
                break
            else:
                tmp1 = tmp1.before
        if tT:
            if tmp1.before == None and tmp1.name[0] > newFrob.name[0]:
                tmp1.setBefore(newFrob)
                newFrob.setAfter(tmp1)
            else:
                tmp2 = tmp1.after
                tmp2.setBefore(newFrob)
                tmp1.setAfter(newFrob)
                newFrob.setBefore(tmp1)
                newFrob.setAfter(tmp2)
    else:
        tmp2 = tmp1.after
        tmp2.setBefore(newFrob)
        tmp1.setAfter(newFrob)
        newFrob.setBefore(tmp1)
        newFrob.setAfter(tmp2)

eric = Frob('eric')
andrew = Frob('andrew')
ruth = Frob('ruth')
fred = Frob('fred')
martha = Frob('martha')


insert(eric, andrew)
insert(eric, ruth)
insert(eric, fred)
insert(ruth, martha)