def dfs(flag):
	start_time = get_time()
	while flag :
		if get_time() - start_time > 10 :
			return 
		m = measure()
		if m == None:
			continue
		else:
			break
	
	
	path = [] 
	passed = {}
	def back():
		direct = path[-1]
		if direct == North:
			move(South)
		elif direct == South:
			move(North)
		elif direct == East:
			move(West)
		elif direct == West:
			move(East)
		global path 
		path = path[:-1]
	def go_ahead(direction):
		global path 
		moved = False
		if direction == North:
			if can_move(North) and (x,y+1) not in passed:
				move(North)
				path.append(North)
				moved = True
		elif direction == South:
			if can_move(South) and (x,y-1) not in passed:
				move(South)
				path.append(South)
				moved = True
		elif direction == East:
			if can_move(East) and (x+1,y) not in passed:
				move(East)
				path.append(East)
				moved = True
		elif direction == West:
			if can_move(West)and (x-1,y) not in passed :
				move(West)
				path.append(West)
				moved = True
		return moved
			
	x_,y_ = get_pos_x(),get_pos_y()
	m = measure()
	if m == None:
		return  
	mx ,my = m[0],m[1]
	#mx,my = measure()
	while True:
		m = measure()
		if m == None:
			return  
		mx ,my = m[0],m[1]
		x,y = get_pos_x(),get_pos_y()
		if get_entity_type() == Entities.Treasure:
			harvest()
			break 
		
		if (x,y) in passed and (x != x_ or y_ != y):
			back()
			#continue
		elif (x,y) not in passed:
			passed[(x,y)]=True
		#print(passed , path,(x,y))
		moved = False
		x,y = get_pos_x(),get_pos_y()
		d = [North,South,East,West]
		dd = []
		if x < mx : 
			dd.append(East)
		elif x > mx : 
			dd.append(West)
		if y < my:
				dd.append(North)
		elif y > my:
				dd.append(South)
		for direction in d :
			if direction not in dd:
				dd.append(direction)
		for direction in dd:
			moved = go_ahead(direction)
			if moved:
				break 
		if not moved:
			#back()
			pass 
		x,y = get_pos_x(),get_pos_y()
		if get_ground_type() != Grounds.Soil:
			#till()
			pass
pos1 = (2,6)
pos2 = (6,2)

l = []
dict = {}
all_drons = []

for i in range(4):
	for j in range(4):
		#f0.move_abs(pos1[0]+ 8 * i, pos1[1] + 8 * j )
		#till()
		#f0.move_abs(pos2[0]+ 8 * i, pos2[1] + 8 * j )
		#till()
		l.append((pos1[0] + 8*i, pos1[1] + 8*j))
		l.append((pos2[0] + 8*i, pos2[1] + 8*j))
clear()
import f0 
f0.move_abs(0,0)
size = get_world_size()
#for i in range(size):
#	for j in range(size):
#		plant(Entities.Bush)
#		use_item(Items.Weird_Substance,size*size)
#		move(North)
#	move(East)
while True:
	if len(all_drons) != 0 :
		for d in all_drons:
			wait_for(d)
		all_drons = []
	for pos in l :
		def move_and_get_gold():
			f0.move_abs(pos[0],pos[1])
			dfs(True) 
		d = spawn_drone(move_and_get_gold)
		if d == None:
			for i in range(32):
				move(North)
			f0.move_abs(pos[0],pos[1])
			plant(Entities.Bush)
			use_item(Items.Weird_Substance,size*32)
			dfs(False)
		else:
			all_drons.append(d)