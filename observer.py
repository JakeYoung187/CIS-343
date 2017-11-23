from abc import ABCMeta, abstractmethod

#############################################################
#The observer class is used to create observers
#############################################################
class Observer(object):
        __metaclass__ = ABCMeta

        @abstractmethod
        def update(self):
                pass

