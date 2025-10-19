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
			if can_harvest():
				harvest()
			plant(Entities.Carrot)
			move(North)
		move(East)