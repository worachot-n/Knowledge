---
id: 3y7po3rh141wfgmfl0tnoyb
title: Object Oriented Programming
desc: ''
updated: 1655828257124
created: 1655824764894
---
## 1.Object-Oriented Programming: Introduction

จำลองการเขียนโปรแกรมเป็นเสมือนวัตถุชนิดหนึ่งที่มีหน้าที่หรือฟังก์ชั่นการใช้งานของตัวเอง

ยกตัวอย่าง เช่น รถยนต์ มีส่วนขับเคลื่อน ส่วนควบคุม วิทยุ ฯ

Excel แต่ละเซลล์ จะเป็น object 1 object มีคุณสมบัติการเพิ่มขนาดฟอนต์ การใส่สูตร
โดย เซลล์ จะใช้ class เซลล์ในการแสดงและประมวลผล

## 2.สร้าง class ง่า

```python
class Player:
 def __init__(self): # __ (dunder) -> double underscores
  self.fname = ""
  self.lname = ""
  self.number = 0

class Player2:
 def __init__(self, fname, lname, number):
  self.fname = fname
  self.lname = lname
  self.number = number
 

if __name__ == '__main__':
 p1 = Player()
 p1.fname = "Loris"
 p1.lname = "Karius"
 p1.number = 1

 p2.fname = "Alex"
 p2.lame = "Manniger"
 p2.number = 13

 p1a = Player("Loris", "Karius", 1)
 p2a = Player("Alex", "Manniger", 13)

 print(p1a.fname)
 print(p2a.lname)

 p1t = ("Loris", "Karius", 1) # Tuple
 print(p1t)
 print(p1t[0])

 p1d = {"fname": "Loris", "lname": "Karius", "number": 1}
 print(p1d)
 print(p1d["lname"])
```

## 3.เปรียบเทียบการเก็บข้อมูลด้วย tuple, dict, class instance

```python
def demo_tuple():
 p12 = "Joe", "Gomez", 12
 print(p12)
 print(p12[1])

def demo_dict():
 p12 = {"fname": "Joe", "lname": "Gomez", "number": 12}
 print(p12)
 print(p12["lname"])

class Player:
 pass

class Player2:
 def __init__(self):
  self.fname = ""
  self.lname = ""
  self.number = 0

class Player3:
 def __init__(self, fname, lname, number):
  self.fname = fname
  self.lname = lname
  self.number = number

def demo_simple_player_class():
 p12 = Player() # p12 => instance
 p12.fname = "Joe" # attribute/property
 p12.lname = "Gomez"
 p12.number = 12
 print(p12.lname)


def demo_simple_player2_class():
 p12 = Player2()
 p12.fname = "Joe" # attribute/property
 p12.lname = "Gomez"
 p12.number = 12
 print(p12.lname)

def demo_simple_player3_class():
 p12 = Player3("Joe", "Gomez", 12)

if __name__ == '__main__':
 #demo_tuple()
 #demo_dict()
 demo_simple_player_class()
```

## 4.รู้จัก __init__() หรือ constructor

```python
class Person:
 def __init__(self):
  self.fname = ""
  self.lname = ""
  self.country = "Thailand"
 
 def __init__(self, fname, lname, country):
  self.fname = fname
  self.lname = lname
  self.country = country
 '''
 Error จะเกิดเพราะมี 2 init
 โปรแกรมจะใช้ init ตัวล่าสุด
 '''

if __name__ in '__main__':
 p1 = Person() # create new instance
 print(p1.fname)
 print(p1.country)
 p2 = Person("Worachot", "Nakduk", "England") # create new instance
 print(p2)
 '''
 Error จะเกิดเพราะมี 2 init
 โปรแกรมจะใช้ init ตัวล่าสุด
 '''

# การแก้ไขคือ

class Person2:
 def __init__(self, fname=None, lname=None, country="Thailand"):
  self.fname = fname
  self.lname = lname
  self.country = country

 def __str__(self):
  return "fname: {} lname:{} country:{}".format(self.fname, self.lname, self.country)
if __name__ in '__main__':
 p1 = Person2() # create new instance
 print(p1.fname) # None
 print(p1.country) # Thailand

 p2 = Person2(fname="Peter") # create new instance
 print(p2.fname) # None
 print(p2.country) # Thailand

 p3 = Person2("Peter", "Parker")
 print(p3)

 p4 = Person2(lname="Swift", fname="Taylor", country"USA")
 print(p4)
```

## 5.การ import class ที่สร้างขึ้นมาแบบต่างๆ

```python
# ชื่อไฟล์ medal.py
class Medal:
 def __init__(self, country, gold, silver, bronze):
  self.country = country
  self.gold = gold
  self.silver = silver
  self.bronze = bronze

 def total(self): 
  return self.gold + self.silver + self.bronze

class Athlete:
 def dummy(self):
  return "hello"
```

```python
# ชื่อไฟล์ demo_medal.py
from medal import Medal, Athlete

if __name__ == '__main__':
 jp = Medal("Japan", 10, 5, 2)
 print(jp.total())
 a = Athlete()
 print(a.dummy())

import medal

if __name__ == '__main__':
 jp = medal.Medal("Japan", 10, 5, 2)
 print(jp.total())
 a = medal.Athlete()
 print(a.dummy())
 
import medal as md

if __name__ == '__main__':
 jp = md.Medal("Japan", 10, 5, 2)
 print(jp.total())
 a = md.Athlete()
 print(a.dummy())

```

## 6.รู้จักกับ self

```Python
class Medal:
 def __init__(self, country, gold, silver, bronze):
  self.country = country
  self.gold = gold
  self.silver = silver
  self.bronze = bronze

 def total(self): # instance method
  return self.gold + self.silver + self.bronze

 #def total(this):
 # return this.gold + this.silver + this.bronze  # same as total(self)

 def dummy(self, a, b):
  return a + b
 
if __name__ == '__main__':
 th = Medal("Thailand", 5, 3 ,2)
 print(th.country)
 print(th.total())
 print(Medal.total(th)) # same as print(th.total())
 print(th.dummy(1, 2))
 print(Medal.dummy(th, 1 ,2))
 th.rank = 10
 print(th.rank) # python เป็นภาษาไดนามิก สามารถสร้าง attribute ได้ใหม้ทุกครั้งที่รันครับ
```

## 7.แปลงโค้ดที่เขียนแบบ procedural ให้เป็น class

```Python
#โค้ดที่เขียนแบบ procedural 
def bmi(w_kg, h_cm):
 return w_kg / (h_cm / 100) ** 2

def category(w_kg, h_cm):
 diag = ""
 bmi_value = bmi(w_kg, h_cm)
 if bmi_value < 18.5:
  diag = "ต่ำกว่าเกณฑ์"
 elif 18.5 <= bmi_value <= 25:
  diag = "ตามเกณฑ์"
 elif 25 <= bmi_value <= 30:
  diag = "เกินเกณฑ์"
 elif bmi_value > 30:
  diag = "อ้วน"
 return diag

if __name__ == '__main__':
 w = 70
 h = 170
 print(bmi(w, h))
 print(category(w, h))
```

```Python
#โค้ดที่เขียนแบบ class 
class Bmi:
 def __init__(self, w_kg, h_cm):
  self.w_kg = w_kg
  self.h_cm = h_cm

 def bmi(self):
  return self.w_kg / (self.h_cm / 100) ** 2

 def category(self):
  diag = ""
  if self.bmi() < 18.5:
   diag = "ต่ำกว่าเกณฑ์"
  elif 18.5 <= self.bmi() <= 25:
   diag = "ตามเกณฑ์"
  elif 25 <= self.bmi() <= 30:
   diag = "เกินเกณฑ์"
  elif self.bmi() > 30:
   diag = "อ้วน"
  return diag

 def __str__(self): # toString() in Java
  return "BMI = {:.2f} ({})".format(self.bmi(), self.category())  

if __name__ == '__main__':
 a = Bmi(70, 170)
 #print(a.bmi())
 #print(a.category())
 print(a)
```

## 8.ความแตกต่างระหว่าง str() และ repr()

```python

# __str__()

class Medal:
 def __init__(self, country, gold, silver, bronze):
  self.country = country
  self.gold = gold
  self.silver = silver
  self.bronze = bronze

 def total(self): # instance method
  return self.gold + self.silver + self.bronze

 def __str__(self): # toString in Java
  return "{:15} gold: {:3} silver: {:3} bronze: {:3} total: {:3}".format(self.country, self.gold, self.silver, self.bronze, self.total())

if __name__ == '__main__':
 th = Medal("Thailand", 5, 6 ,10)
 print(th) # both is same
 print(th.country, "gold:", th.gold, "silver:", th.silver, "broze:",th.broze, "total", th.total())

if __name__ == '__main__':
 m = [
  Medal("Thailand", 5, 6, 10),
  Medal("Japan", 15, 20, 10),
  Medal("China", 55, 40, 105)
 ]
 for c in m:
  print(c)
```

```python

# __repr__()

class Medal:
 def __init__(self, country, gold, silver, bronze):
  self.country = country
  self.gold = gold
  self.silver = silver
  self.bronze = bronze

 def total(self): # instance method
  return self.gold + self.silver + self.bronze

 def __repr__(self): # string representation
  return "{}{}".format(self.__class__.__name__, repr((self.country, self.gold, self.silver, self.bronze)))

if __name__ == '__main__':
 m = [
  Medal("Thailand", 5, 6, 10),
  Medal("Japan", 15, 20, 10),
  Medal("China", 55, 40, 105)
 ]
 for c in m:
  print(c)

 # print -> Medal("Thailand", 5, 6, 10),
 # Medal("Japan", 15, 20, 10),
 # Medal("China", 55, 40, 105)

 # print(th) -> print(str(th)) -> print(th.__str__()) -> print(th.__repr__())
```

## 9.การใช้ vars() และ getattr() ในการแสดงชื่อ attribute และ value ของ instance

```python

class Person: 
 def __init__(self, fname, lname, age):
  self.fname = fname
  self.lname = lname
  self.age = age

 def __str__(self): # not sort by your order
  # return "fname: {},lname: {}, age: {}".format(self.fname, self.lname, self.age)
  a = vars(self)
  print(a)
  s = ["{:10}: {}".format(k, v) for k, v in a.items()]
  return "\n".join(s)

 def __str__(self): # sort by your order
  attrs = ("fname", "lname", "age")
  s = ["{:10}: {}".format(a, getattr(self, a)) for a in attrs]
  return "\n".join(s)

if __name__ == '__main__':
 p = Person("Peter", "Parker", 26)
 print(p)
```

## 10.หลักการ mutable และ immutable objects

```python
# immutable
def immutable_demo():
 n = 5
 print("id(n) = {}, n = {}". format(id(n), n))
 n = n + 4
 print("id(n) = {}, n = {}". format(id(n), n))
 s = "rain"
 print("id(s) = {}, s = {}". format(id(s), s))
 s = s + "bow"
 print("id(s) = {}, s = {}". format(id(s), s))

if __name__ == '__main__':
 immutable_demo()
 # id(n) = 20121938832, n = 5
 # id(n) = 20121938960, n = 9
 # id(s) = 1753614695544, s = rain
 # id(s) = 1753614695480, s = rainbow

```

```python
# mutable
def mutable_demo():
 p = ["Peter"]
 print("id(p) = {}, p = {}". format(id(p), p))
 p[0] = "Spiderman"
 print("id(p) = {}, p = {}". format(id(p), p))
 q = p
 print("id(p) = {}, p = {}\nid{q} = {}, q = {}". format(id(p), p, id(q), q))
 q.append("sunshine")
 print("id(p) = {}, p = {}\nid{q} = {}, q = {}". format(id(p), p, id(q), q))
 

if __name__ == '__main__':
 mutable_demo()
 # id(p) = 2491716061832, p = ['Peter']
 # id(p) = 2491716061832, p = ['Spiderman']
 # id(p) = 2491716061832, p = ['Spiderman']
 # id(q) = 2491716061832, q = ['Spiderman']
 # id(p) = 2491716061832, q = ['Spiderman', "sunshine"]
 # id(q) = 2491716061832, q = ['Spiderman', "sunshine"]
```

```python
# mutable
class Contact:
 def __init__(self):
  self.name = name
  self.phone = phone

 def __str__(self):
  return "id(self) = {}, name = {}, phone = {}".format(id(self), self.name, self.phone)

if __name__ == '__main__':
 a = Contact("Fah", "0812223333")
 print(a)
 a.phone = "0992223333"
 print(a)
 b = a
 b.phone = "0773334444"
 print(a)
 print(b)
 # id(self) = 1213009052784, name = Fah, phone = 0812223333
 # id(self) = 1213009052784, name = Fah, phone = 0992223333
 # id(self) = 1213009052784, name = Fah, phone = 0772223333
 # id(self) = 1213009052784, name = Fah, phone = 0772223333
```

## 11.เข้าใจหลักการในการอ้างถึง Object/Instance

```python
class Wallet:
 def __init__(self):
  self.amount = 0

 def earn(self, a):
  self.amount += a

 def spend(self, a):
  self.amount -= a

 def __str__(self):
  return "amount = {}".format(self.amount)

if __name__ == '__main__':
 dad = Wallet()
 dad.earn(100)
 print("dad's wallet", dad)
 mom = dad
 print(mom is dad)
 # True
 print("mom's wallet", mom)
 mom.spend(20)
 print("dad's wallet", dad)
 print("mom's wallet", mom)
 print(id(dad), id(mom)) # both is same
 kid = Wallet()
 kid.earn(500)
 mom = kid
 print(id(dad), id(mom), id(kid)) # dad is not change, mom and kid are same
 mom.earn(40)
 print("kid's wallet", kid)
```

## 12.การใช้ single underscore (ขีดล่าง)

```python

# file: underscore_demo.py

for _ in range(5):
 print("hello")

for _ in range(5):
 print(_)

import random
for _ in range(5)
 print(random.randint(1, 6))

_recipe = "a7b3c15" # private
vat = .07

def _rectangle(w, h):
 return w*h

def circle(r):
 return 22 / 7 * r

class Alpha:
 @staticmethod
 def foo():
  print("hello")

class _Beta:
 def bar():
  print("wow")

```

```python
import underscore_demo # file: underscore_demo.py

print(underscore_demo._recipe)
# a7b3c15
print(underscore_demo.vat)
# 0.07

from underscore_demo import *
print(_recipe)
# NameError: name '_recipe' is not defined
print(vat)

print(_rectangle(3, 4))
# NameError: name '_rectangle' is not defined
print(circle(10))

Alpha.foo()
# hello
_Beta.bar()
# NameError: name '_Beta' is not defined

from underscore_demo import Alpha. _Beta
Alpha.foo()
# hello
_Beta.bar()
# wow
```

```python
# file: underscore_demo.py
__all__ = ["circle", "Alpha", "_Beta"]

def circle(r):
 return 22 / 7 * r

class Alpha:
 @staticmethod
 def foo():
  print("hello")

class _Beta:
 def bar():
  print("wow")

```

```python
from underscore_demo import *

print(circle(10))
# 31.428571....
Alpha.foo()
# hello
_Beta.bar()
# wow

```

## 13.การใช้ double underscore หรือ dunder

```python

# file.dunder.py

# dunder -> double underscore

class Alpha:
 normal = 1
 _lucky = 13
 __secret = 777 # name mangled -> change _classname__attri

 def fx(self):
  print("this is fx in A")
 def _fy(self):
  print("this is fy in A")
 def __fx(self):
  print("this is fz in A")

class Beta(Alpha):
 def __init(self):
  self.greeting = "hello from beta"

 def __foo__(self): # not famous
  pass

 def __fz(self):
  print("THIS IS fz in B")

class __Gamma:
 def bar(self):
  print("hello from Gamma")

if __name__ == '__main__':
 print(Alpha.normal)
 # 1
 print(Alpha._lucky)
 # 13
 print(Alpha.__secret)
 # AttrubuteError: type object 'Alpha' has no attribute '__secret'
 print(Alpha.__dict__)
 # {'__module__': '__main__', '_lucky': 13, 'normal': 1, '__dict__': <attribute '__dict__' of 'Alpha' object>, '_Alpha__secret': 777, ....}
 print(Alpha._Alpha___secret)
 # 777
 Alpha.normal = 99
 Alpha._lucky = 123
 Alpha.__secret = 9999
 print(Alpha.normal)
 # 99
 print(Alpha._lucky)
 # 123
 print(Alpha.__secret) # create new variable
 # 9999
 print(Alpha._Alpha___secret)
 # 777

 print(Alpha.__dict__)
 # {'__module__': '__main__', '_lucky': 13, 'normal': 1, '__dict__': <attribute '__dict__' of 'Alpha' object>, '_Alpha__secret': 777, '__secret': 9999, 'fx': <function Alpha.fx at 0x101e7aa60>, '_fy': <function Alpha._fy at 0x101e7aae8>, '_Alpha.__fz': <function Alpha.__fz at 0x101e7ab70>, ....}
 a = Alpha()
 a.fx()
 # this is fx in A
 a._fy()
 # this is fy in A
 a.__fz()
 # AttrubuteError: 'Alpha' object has no attribute '__fz'
 a._Alpha__fz()
 # this is fz in A

 b = Beta()
 b._Beta__fz()
 # THIS IS fz in B
 b._Alpha__fz()
 # this is fz in A

 g = __Gamma()
 g.bar()
 # hello from Gamma
```

```python
from dunder import *

g = __Gamma()
g.bar()
# NameError: name '__Gamma' is not defined

from dunder import __Gamma

g = __Gamma()
g.bar()
# hello from Gamma

import dunder
g = dunder.__Gamma()
g.bar()
# hello from Gamma
```

## 14.การใช้ @property decorator

```python

# wrong way

class Student:
 def __init__(self, s_id, fname, lname):
  self.lname = lname
  self.fname = fname
  self.s_id = s_id
  self.full_name = "{} {}".format(self.fname, self.lname)

if __name__ == '__main__':
 s = Student("5841234526", "Fah", "Puinoon")
 print(s.full_name)
 # Fah Puinoon
 s.full_name = "Songkarn Fahsai" # user can edit it
 print(s.full_name) # wrong way
 # Songkarn Fahsai 
```

```python

# correct way

class Student:
 def __init__(self, s_id, fname, lname):
  self.lname = lname
  self.fname = fname
  self.s_id = s_id

 def full_name(self):
  return "{} {}".format(self.fname, self.lname)

 def email(self):
  return "{}.{}{}@cbs.chula.ac.th".format(self.fname, self.lname[:2], self.join_yy)

 @property
 def full_name2(self):
  return "{} {}".format(self.fname, self.lname)

 @property
 def join_yy(self):
  return self.s_id[:2]

 @property
 def degree(self):
  return self.s_id[2]

 @property
 def seq(self):
  return self.s_id[3:7]

 @property
 def check_digit(self):
  return self.s_id[-3]

 @property
 def school(self):
  return self.s_id[-2:]

if __name__ == '__main__':
 s = Student("5841234526", "Fah", "Puinoon")
 print(s.full_name())
 # Fah Puinoon
 s.full_name = "Songkarn Fahsai" 
 print(s.full_name()) 
 # TypeError: 'str' object is not callable
 print(s.full_name2)
 # Fah Puinoon
 print(s.join_yy)
 # 58
 print(s.s_id[:2])
 #58
 print(s.school)
 # 26
 print(s.email())
 # Fah.Pu58@@cbs.chula.ac.th
```

## 15.การสร้าง getter, setter ให้กับ attributes/properties(Java style)

```python
class Student:
 def __init__(self, fname, lname, blood):
  self.fname = fname
  self.lname = lname
  self.blood = blood # A, B, AB, O

 def __str__(self):
  return "{} {}, blood group: {}".format(self.fname, self.lname, self.blood)

class Person:
 def __init__(self, fname, lname, blood):
  self.fname = fname
  self.lname = lname
  # self.blood = blood # A, B, AB, O
  self.setBlood(blood)

 def getBlood(self):
  return self.__blood

 def setBlood(self, blood):
  if blood.upper() in ["A", "B", "AB", "O"]:
   self.__blood = blood.upper()
  else: 
   raise ValueError("invalid blood group.")

 def __str__(self):
  return "{} {}, blood group: {}".format(self.fname, self.lname, self.__blood)

if __name__ == '__main__':
 s1 = Student("Peter", "Parker", "A")
 s1.blood = "Y"
 print(s1)
 # Peter Parker, blood group: Y

 p1 = Person("Peter", "Parker", "Y")
 print(p1)
 # ValueError: invalid blood group.
 p2 = Person("Peter", "Parker", "Ab")
 # Peter Parker, blood group: AB
 p2.setBlood("O")
 print(p2)
 # Peter Parker, blood group: O
 p2.__blood = "B" # not change to B
 # Peter Parker, blood group: O
 p2._Person__blood("B")
 print(p2)
 # Peter Parker, blood group: B
 print(p2.getBlood())
 # B
```

## 16.การสร้าง getter, setter ให้กับ attributes/properties(Pythonic way)

```python

class Person:
 def __init__(self, fname, lname, blood):
  self.fname = fname
  self.lname = lname
  self.blood = blood # A, B, AB, O

 @property
 def fname(self):
  return self.__fname

 @fname.setter
 def fname(self, fname):
  self.__fname = fname.strip().title()

 @property
 def blood(self): # getter
  return self.__blood

 @blood.setter
 def blood(self, blood): # setter
  if blood.upper() in ["A", "B", "AB", "O"]:
   self.__blood = blood.upper()
  else: 
   raise ValueError("invalid blood group.")

 def __str__(self):
  return "{!r} {}, blood group: {}".format(self.fname, self.lname, self.blood)
  # !r = print raw 

if __name__ == '__main__':
 p1 = Person("Peter", "Parker", "A")
 print(p1)
 # Peter Parker, blood group: A
 p1.blood = "O"
 print(p1)
 # Peter Parker, blood group: O
 print(p1.blood)
 # O
```

## 17.หลักการสืบทอด (Inheritance) ตอนที่ 1

```python

class Person:
 def __init__(self, fname, lname):
  self.fname = fname
  self.lname = lname

 def __str__(self):
  return "{} {}".format(self.fname, self.lname)

class Student(Person):
 def __init__(self, s_id, fname, lname):
  self.s_id = s_id
  self.fname = fname
  self.lname = lname

 def __str__(self):
  return "{} {}".format(self.s_id, super().__str__())

class ExchangeStudent(Student):
 def __init__(self, s_id, fname, lname, partner_univ):
  super().__init__(s_id, fname, lname)
  self.partner_univ = partner_univ

if __name__ == '__main__':
 s1. = Student("1234", "Fon", "Sairoong")
 print(s1)
 # 1234 Fon Sairoong
 s2 = ExchangeStudent("7890", "Peter", "Parker", "ABC Univ")
 print(s2) # same as s1
 # 7890 Peter Parker 

```

## 18.หลักการสืบทอด (Inheritance) ตอนที่ 2

```python

class Person:
 def __init__(self, fname, lname, sex):
  self.fname = fname.strip().title()
  self.lname = lname.strip().title()
  self.sex = sex

 def __str__(self):
  return "{!r} {!r} sex: {}".format(self.fname, self.lname, self.sex)

class Student(Person):
 def __init__(self, s_id, fname, lname, sex):
  super().__init__(fname, lname, sex)
  self.s_id = self.remove_non_digit(s_id)

 def __str__(self):
  return "{} {}".format(self.s_id, super().__str__())

 @staticmetod
 def remove_non_digit(s):
  return re.sub(r"[\D]", "", s)

 def email(self):
  return "{}.{}{}@cbs.chula.ac.th".format(self.fname, self.lname[:2], self.s_id[:2])

class ExchangeStudent(Student):
 def __init__(self, s_id, fname, lname, sex, partner_univ):
  super().__init__(s_id, fname, lname, sex)
  self.partner_univ = partner_univ

 def foo(self, s):
  return self.remove_non_digit(s)

if __name__ == '__main__':
 s1. = Student("584  12345-26", "fon", "Sairoong", "F")
 print(s1)
 # 5841234526 'Fon' 'Sairoong' sex: F
 print(s1.email())
 # Fon.Sa58@cbs.chula.ac.th
 s2 = ExchangeStudent("584-12345(26)", "peter", "Parker", "M", "ABC Univ")
 print(s2) # same as s1
 # 5841234526 'Peter' 'Parker' sex: M
 print(s1.email())
 # Peter.Pa58@cbs.chula.ac.th

```

## 19.สร้าง Abstract Class

```python
from abc import ABC, abstracmethod # Abstract Base Class

class Member(ABC):
 def __init__(self, m_id, fname, lname):
  self.m_id = m_id
  self.fname = fname
  self.lname = lname

 def __str__(self):
  return "ID: {} {} {}".format(self.m_id, self.fname, self.lname)

 @abstractmethod
 def discount(self):
  pass

class Gold(Member):
  pass

class Silver(Member):
  pass

if __name__ == '__main__':
 m = Member("007", "James", "Bond")
 print(m)
 # TypeError: Can't instantiate abstract class Member with abstract method discount
 g = Gold("123", "Peter", "Parker")
 print(g)
 # TypeError: Can't instantiate abstract class Gold with abstract method discount
 
```

```python
from abc import ABC, abstracmethod # Abstract Base Class

class Member(ABC):
 def __init__(self, m_id, fname, lname):
  self.m_id = m_id
  self.fname = fname
  self.lname = lname

 def __str__(self):
  return "ID: {} {} {}".format(self.m_id, self.fname, self.lname)

 @abstractmethod
 def discount(self):
  pass

 def full_name(self):
  return "{} {}".format(self.fname, self.lname)

class Gold(Member):
 def discount(self):
  return .10

class Silver(Member):
 def discount(self):
  return .05

if __name__ == '__main__':
 g = Gold("123", "Peter", "Parker")
 print(g)
 # ID: 123 Peter Parker
 print(g.discount())
 # 0.1
 print(g.full_name)
 # Peter Parker
 s = Silver("888", "Jane", "Mark")
 print(s)
 # ID: 888 Jane Mark 
 print(s.full_name)
 # Jane Mark
 
```

## 20.การสืบทอดจากหลายคลาสแม่พร้อมกัน(Multiple Inheritance)

```python
class Camera:
    def take_photo(self):
        print("take a photo")
    
    def delete_photo(self):
        print("delete a photo")

    # same as Phone.browse()
    def browse(self):
        print("browse photo alblum")

class Phone:
    def call(self, number):
        print("calling {}".format(number))

    def send_sms(self, number, message):
        print("sending {} to {}".format(message, number))

class MediaPlayer:
    def plat(self):
        print("playing a song/video")

    def browse(self):
        print("browse media library")

class SmartPhone(camera, Phone, Mediaplayer):
    def share(self):
        print("share...")

if __name__ == '__main__':
    s = SmartPhone()
    s.take_photo()
    # take a photo
    s.send_sms("1234123", "HI")
    # sending Hi to 1234123
    s.play()
    # playing a song/video
    s.browse()
    # browse photo alblum
    
```

## 21.Composition เบื่องต้น

```python
from datetime import date

class Person:
    def __init__(self, title, fname, lname, dob):
        self.title = title
        self.fname = fname
        self.lname = lname
        self.dob = dob

    def __str__(self):
        return "{} {} {} {}".format(self.title, self.fname, self.lname, self.dob)

class PersonV2:
    def __init__(self, title, fname, lname, titleTh, fnameTh, lnameTh,  dob):
        self.title = title
        self.fname = fname
        self.lname = lname
        self.titleTh = titleTh
        self.fnameTh = fnameTh
        self.lnameTh = lnameTh
        self.dob = dob

    def __str__(self):
        return "{} {} {}\n{} {} {}\n{}".format(self.title, self.fname, self.lname, self.titleTh, self.fnameTh, self.lnameTh, self.dob)

class PersonName:
    def __init__(self, title, fname, lname):
        self.title = title
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return "{} {} {}".format(self.title, self.fname, self.lname)

class PersonV3:
    def __init__(self, nameEn, nameTh, dob):
        self.nameEn = nameEn
        self.nameTh = nameTh
        self.dob = dob

    def __str__(self):
        return "{}\n{}\n{}".format(self.nameEn, self.nameTh, self.dob)

if __name__ == '__main__':
    p1 = Person("Mr.", "Peter", "Parker", date(1995, 10, 4))
    print(p1)
    print("*" * 40)
    p2 = PersonV2("Mr.", "Peter", "Parker", "นาย",
                  "ปีเตอร์", "ปาร์คเกอร์", date(1995, 10, 4))
    print(p2)
    print("*" * 40)
    p3 = PersonV3(PersonName("Mr.", "Peter", "Parker"), PersonName(
        "นาย", "ปีเตอร์", "ปาร์คเกอร์"), date(1995, 10, 4))
    print(p3)
```

## 22.
