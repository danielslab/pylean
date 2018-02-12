class RevealAccess(object):
    """A data descriptor that sets and returns values
       normally and prints a message logging their access.
    """
<<<<<<< HEAD
#add first line
#add second line
=======
#this is a comment
>>>>>>> change learnclass.py in dev
    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print('Retrieving', self.name)
        return self.val

    def __set__(self, obj, val):
        print('Updating', self.name)
        self.val = val

