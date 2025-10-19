clear()
size = get_world_size()
for i in range(size):
	for j in range(size):
		if (i + j)  % 2 == 0 :
			if can_harvest():
				harvest()
				plant(Entities.Tree)
				use_item(Items.Fertilizer)
		else:
			if can_harvest():
				harvest()
				plant(Entities.Bush)
		move(North)
	move(East)
size = get_world_size()
for i in range(size):
	for j in range(size):
		if True:
			if can_harvest():
				harvest()
		move(North)
	move(East)