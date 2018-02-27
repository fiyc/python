#python class转json
#当将自定义类型转化为json时，需要写转换规则，如下：convertObj
#example1中ensure_ascii=False用来显示中文而非转换
import json

class Object:
	ID = 0
	Name = ''

	def __init__(self, id, name):
		self.ID = id
		self.Name = name



def convertObj(obj):
	d = {}
	d.update(obj.__dict__)
	return d

def example1():
	try:
		alist = []
		a = Object(1, "你好")
		b = Object(1, "世界")
		alist.append(a)
		alist.append(b)

		result = json.dumps(alist, default=convertObj, ensure_ascii=False)
		print(result)
	except Exception as e:
		print(e)

	#temp = alist.__dict__
	#print(temp)

example1()
input()