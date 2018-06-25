#-*- coding: UTF-8 -*-

class demoInterface(object):
    def __init__(self):
        pass

    def say(self):
        pass

    def hander(self):
        print("this is hander")



class impl(demoInterface):
    def __init__(self):
        pass

    def say(self):
        print("hello")


a = impl()
a.hander()