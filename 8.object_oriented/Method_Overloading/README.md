# Method Overloading

---
When you have a class with method of one name defined more than one but with different argument types and/or return type, it is a case of method overloading.
>[!NOTE]
> 
> Python doesn't support this mechanism method overloading

* However, we can use dispatch function from a third party module named MultipleDispatch for this purpose.
>pip install multipledispatch
```python
from multipledispatch import dispatch
class example:
   @dispatch(int, int)
   def add(self, a, b):
      x = a+b
      return x
   @dispatch(int, int, int)
   def add(self, a, b, c):
      x = a+b+c
      return x

obj = example()

print (obj.add(10,20,30))
print (obj.add(10,20))
```