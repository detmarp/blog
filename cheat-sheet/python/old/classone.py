class ClassOne(object):
    """My sample class
        Note that inheriting from (object) is a python 2.2 "new-object" concept.
        In python 3, we no longer need to do this, since I assume that all
        classes are "new" style.  (having said that, the internet still says:
            'in Python 3 [it is] however recommended that you still subclass from object.' )
        See:
          * https://docs.python.org/release/2.2.3/whatsnew/sect-rellinks.html
          * http://stackoverflow.com/questions/54867/what-is-the-difference-between-old-style-and-new-style-classes-in-python
    """
    def __init__(self):
        self.x = 0
        self.y = 0
        
    @classmethod # means that the first argument is the *class*, not the instance
    def from_xy(cls, x, y):
        this = cls() # here we are basically calling ClassOne.__init__() (the constructor)
        this.x = x
        this.y = y
        return this
        
    @classmethod
    def from_ClassOne(cls, other):
        this = cls()
        this.x = other.x
        this.y = other.y
        return this
        
    def add(self, other):
        """does not modify self; just returns a new object"""
        copy = ClassOne.from_ClassOne(self)
        copy.x += other.x
        copy.y += other.y
        return copy
        
    def __str__(self): # str(object) will call this
        return "({0}, {1})".format(self.x, self.y)
