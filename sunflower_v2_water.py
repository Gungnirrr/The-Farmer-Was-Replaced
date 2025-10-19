clear()
size = get_world_size()
for i in range(size):
	for j in range(size):
		till()
		move(North)
	move(East)
while True:
	for i in range(size):
		for j in range(size):
			if get_water() < 0.2:
				use_item(Items.Water)
			if can_harvest():
				harvest()
			plant(Entities.Sunflower)
			move(North)
		move(East)