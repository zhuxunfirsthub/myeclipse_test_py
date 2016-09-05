from xml.dom import WRONG_DOCUMENT_ERR
class Student(object):
    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self,value):
        if value<=2016:
            self._birth=value
        else:
            self._birth='wrong'
s=Student()
s.birth=2017
print(s.birth);

