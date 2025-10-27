import f0
clear()
f0.move_abs(8,8)
plant(Entities.Tree)
def plant_companion(x,y,p):
	#f0.move_abs(x,y)
	step = 0 
	pos_list =	[(x-1,y+1),(x,y+2),(x+1,y+1),
				(x-2,y),(x,y),(x+2,y),
				(x-1,y-1),(x,y-2),(x+1,y-1)]
	f0.move_abs(pos_list[0][0],pos_list[0][1])
	pos_dict = {}
	for i in pos_list :
		pos_dict [i] = True
	if p == Entities.Carrot and get_ground_type() != Grounds.Soil:
		till()
	while True :
		x,y = get_pos_x(),get_pos_y() 
		l =  get_companion()
		global dict
		if l == None or (l[1][0],l[1][1]) in dict or (l[1][0],l[1][1]) in pos_dict:
			harvest()
			if p == Entities.Tree:
				plant(Entities.Tree)
			else:	
				if p == Entities.Carrot and get_ground_type() != Grounds.Soil:
					till()
				plant(p)
			continue
		f0.move_abs(l[1][0],l[1][1])
		harvest()
		if l[0] == Entities.Carrot and get_ground_type() != Grounds.Soil:
			till()
		plant(l[0])
		#print(get_pos_x(),get_pos_y(),step,l[0])
		f0.move_abs(x,y)
		if not can_harvest():
			if get_water() < 0.7 :
				use_item(Items.Water)
		else:	 
			harvest()
			if p == Entities.Tree:
				plant(Entities.Tree)
			else:
				plant(p)
		step += 1
		step = step % 9   
		f0.move_abs(pos_list[step % 9][0],pos_list[step %9][1])
		
clear()
pos1 = (2,6)
pos2 = (6,2)
l = []
dict = {}

for i in range(4):
	for j in range(4):
		l.append((pos1[0] + 8*i, pos1[1] + 8*j))
		l.append((pos2[0] + 8*i, pos2[1] + 8*j))
		dict[(pos1[0] + 8*i, pos1[1] + 8*j)] = True
		dict[(pos2[0] + 8*i, pos2[1] + 8*j)] = True
		x,y = pos1[0] + 8*i, pos1[1] + 8*j
		pos_list = 	[(x-1,y+1),(x,y+2),(x+1,y+1),
				(x-2,y),(x,y),(x+2,y),
				(x-1,y-1),(x,y-2),(x+1,y-1)]
		for pos in pos_list:
			dict[pos] = True 
		x,y = pos2[0] + 8*i, pos2[1] + 8*j
		pos_list = 	[(x-1,y+1),(x,y+2),(x+1,y+1),
				(x-2,y),(x,y),(x+2,y),
				(x-1,y-1),(x,y-2),(x+1,y-1)]
		for pos in pos_list:
			dict[pos] = True
#plant_companion(2,6,Entities.Tree)
for pos in l :
	def plant_mix():
		# 需要种植什么，就把这一行的植物改成什么，
		# 可选择 Entities.Grass, Entities.Tree,Entities.Carrot
		plant_companion(pos[0],pos[1],Entities.Carrot)
	d = spawn_drone(plant_mix)
	if d == None:
		plant_mix()

		
	