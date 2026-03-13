class Plant:
	def __init__(self, name, height, age) -> None:
		self.name = name
		self.height = height
		self.age = age
	def grow(self) -> None:
		self.height += 1
	def age_grow(self) -> None:
		self.age += 1

def ft_plant_factory() -> None:
	print("=== Plant Factory Output ===")
	plant_data = [("Rose", 25, 30), ("Oak", 200, 365), ("Cactus", 5, 90),
		("Sunflower", 80, 45), ("Fern", 15, 120)]
	l = []
	for name, height, age, in plant_data:
		plant = Plant(name, height, age)
		l.append(plant)
		print(f"{plant.name}, {plant.height}, {plant.age}")
		l = [1, 2, 3 , 4, 5]
for x in l:
	print(x)
ft_plant_factory()