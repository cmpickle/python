class person:

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def toString(self):
		print(self.name + " is " + str(self.age) + " years old.")

def main():
	a = person("Shawn", 25)
	a.toString()
	print(a.name)

if __name__ == "__main__":
	main()