def drone():
	n=0
	trigger=[]
	while 1:
		n=n+1
		if get_entity_type() == Entities.Treasure:
			use_item(Items.Weird_Substance, length * 2**(num_unlocked(Unlocks.Mazes) - 1))
			trigger.insert(0,n)
		if get_entity_type() == Entities.Treasure and not (len(trigger) <= 3):			
			if trigger[0] == trigger[1] + 1 and trigger[0] == trigger[2] + 2:
				harvest()
		if n >1000000:
			n=0
		if num_items(Items.Gold) >= 119863168:
			break
length = 5
n=0
clear()
set_world_size(length)
if length ** 2 <= max_drones():
	num = length ** 2 - 1

for i in range(num):
	spawn_drone(drone)
	if get_pos_x() == length - 1:	
		move(North)
	move(East)
while 1:
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, length * 2**(num_unlocked(Unlocks.Mazes) - 1))
	n=n+1
	if n < 299:
		if get_entity_type() == Entities.Treasure:
			use_item(Items.Weird_Substance, length * 2**(num_unlocked(Unlocks.Mazes) - 1))
	else:
		if get_entity_type() == Entities.Treasure:
			harvest()
			n=0
	if num_items(Items.Gold) >=119863168:
		break