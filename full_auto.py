d = get_cost(Unlocks.Speed)
for i in range(50):
	while not can_harvest():
		pass
	harvest()
unlock(Unlocks.Speed)
unlock(Unlocks.Expand)
for i in range(50):
	while not can_harvest():
		pass
	harvest()
	move(North)
unlock(Unlocks.Plant)

while True:
	if can_harvest():
		harvest()
		plant(Entities.Bush)
		move(North)
	if num_items(Items.Wood) > 20:
		break 
# 3*3
unlock(Unlocks.Expand)

def move_abs(x,y):
	x_,y_ = get_pos_x(),get_pos_y()
	if x_ < x :
		for i in range(x-x_):
			move(East)
	else:
		for i in range(x_-x):
			move(West)
	if y_ < y :
		for i in range(y-y_):
			move(North)
	else:
		for i in range(y_-y):
			move(South)
			
def get_grass(n):
	clear()
	while True:
		if num_items(Items.Hay) > n :
			return 
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				if can_harvest():
					harvest()
					move(North)
			move(East)
def get_wood_by_bush(n):
	while True:
		if num_items(Items.Wood) > n :
			return 
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				if can_harvest():
					harvest()
					plant(Entities.Bush)
					move(North)
			move(East)
get_grass(300)
# Grass 2
unlock(Unlocks.Grass)

get_wood_by_bush(20)

# Speed 2
unlock(Unlocks.Speed)

get_wood_by_bush(50)
# Carrot 1
unlock(Unlocks.Carrots)
	
def get_carrot(n):
	cost = get_world_size() * get_world_size() * 2**(num_unlocked(Unlocks.Carrots) - 1) 
	get = n 
	if get < cost :
		get = cost
	else:
		get = ((get-(get%cost))/cost)*cost + cost 		 
	get_grass(get)
	get_wood_by_bush(get)
	while True:
		if num_items(Items.Carrot) >= n :
			return 
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				if can_harvest():
					harvest()
					if get_ground_type() != Grounds.Soil:
						till()
					plant(Entities.Carrot)
					move(North)
			move(East)

get_carrot(20)
get_wood_by_bush(30)

# 4*4 
unlock(Unlocks.Expand)

get_carrot(50)
get_wood_by_bush(50)
# Speed 2
unlock(Unlocks.Speed)

get_carrot(70)
get_wood_by_bush(50)
# Tree 1
unlock(Unlocks.Trees)

def get_wood_by_tree(n):
	size = get_world_size()
	while num_items(Items.Wood) < n :
		for i in range(size):
			for j in range(size):
				if (i + j)  % 2 == 0 :
					if can_harvest():
						harvest()
						plant(Entities.Tree)
				else:
					if can_harvest():
						harvest()
						plant(Entities.Bush)
				move(North)
			move(East)
get_wood_by_tree(50)
# Watering 1 
unlock(Unlocks.Watering)

get_grass(300)
# Trees 2
unlock(Unlocks.Trees)

get_carrot(50)
get_wood_by_tree(100)
# Expand 4 6*6
unlock(Unlocks.Expand)

get_wood_by_tree(450)
# Carrot 2 
unlock(Unlocks.Carrots)
# Watering 2
unlock(Unlocks.Watering)
# Grass 3
get_wood_by_tree(500)
unlock(Unlocks.Grass)

get_carrot(500)
unlock(Unlocks.Sunflowers)

get_wood_by_tree(500)
# Fertilizer 1
unlock(Unlocks.Fertilizer)

def get_power(n):
	if num_items(Items.Power) > n:
		return 
	size = get_world_size() 
	get_carrot(n+ size * size)
	while num_items(Items.Power) < n :	
		#get_carrot(size*size)
		#clear()
		for i in range(size):
			for j in range(size):
				if get_ground_type() != Grounds.Soil:
					till()
					plant(Entities.Sunflower)
				if can_harvest():
					harvest()
					plant(Entities.Sunflower)
				move(North)
			move(East)

get_power(100)

get_carrot(200)
get_wood_by_tree(500)
unlock(Unlocks.Pumpkins)

get_carrot(500)
# Speed 3
unlock(Unlocks.Speed)

get_wood_by_tree(800)
# Watering 2 
unlock(Unlocks.Watering)
get_power(500)
get_grass(1200)
# Trees 3
unlock(Unlocks.Trees)

get_carrot(1000)
# Speed 5
unlock(Unlocks.Speed)

def get_pumkin(n):
	get_carrot(n)
	clear()
	size = get_world_size()
	while num_items(Items.Pumpkin) < n :
		dead = 0
		for i in range(size):
			for j in range(size):
				if get_water() < 0.2:
					use_item(Items.Water)
				if get_ground_type() != Grounds.Soil:
					till()
				if not can_harvest():
					harvest()
					dead +=1 
				plant(Entities.Pumpkin)
				move(North)
			move(East)
		if dead == 0 :
			harvest()
			dead = 0 
get_pumkin(1000)
# Expand 5 8*8
unlock(Unlocks.Expand)
	
get_wood_by_tree(3000)
# Carrot 3
unlock(Unlocks.Carrots)
# Fertilizer 2 
unlock(Unlocks.Fertilizer)

get_carrot(1000)
# Pumkin 2
unlock(Unlocks.Pumpkins)

get_wood_by_tree(2500)
# Grass 4
unlock(Unlocks.Grass)

get_grass(5000)
# Trees 4
unlock(Unlocks.Trees)

get_power(1500)

get_pumkin(5000)
# Cactus 1 
unlock(Unlocks.Cactus)

def get_weird():
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

get_weird()
def get_weird_by_weird(n):
	while num_items(Items.Weird_Substance) < n:
		clear()
		size = get_world_size()
		move_abs(0,0)
		if num_items(Items.Weird_Substance) < 1024 :
			get_weird()
			continue

		for x in range (size):
			for y in range(size):
				move_abs(x,y)
				if x % 2 == 0:
					if x % 4 == 0 and y % 3 == 0:
						plant(Entities.Tree)
						use_item(Items.Weird_Substance)
					elif x % 4 != 0 and y % 3 == 1 :
						plant(Entities.Tree)
						use_item(Items.Weird_Substance)
		move_abs(0,0)
		for x in range (size):
			for y in range(size):
				if can_harvest():
					harvest()
				move(North)
			move(East)
get_weird_by_weird(2000)
# Maze 1
unlock(Unlocks.Mazes)

get_wood_by_tree(7000)
# Carrot 4
unlock(Unlocks.Carrots)

get_wood_by_tree(12500)
# Grass 5
unlock(Unlocks.Grass)

get_grass(20000)
# Tree 5 
unlock(Unlocks.Trees)

get_carrot(5000)
# Pumkin 3 
unlock(Unlocks.Pumpkins)

def dfs():
	clear()
	size = get_world_size()
	for i in range(size):
		for j in range(size):
			plant(Entities.Bush)
			substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
			if num_items(Items.Weird_Substance) < substance :
				get_weird_by_weird(1000)
			use_item(Items.Weird_Substance,substance)
			move(North)
		move(East)
	
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
	mx,my = measure()
	while True:
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

dfs()
def get_gold(n):
	while num_items(Items.Gold) < n :
		dfs()
get_gold(2000)
# 2 drowns
unlock(Unlocks.Megafarm)

def get_cactus_one_turn():
	
	drons = max_drones()
	#set_world_size(16)
	#drons = 16
	
	size = get_world_size() 
	if size % drons != 0 :
		size = size - (size % drons)
		set_world_size(size)
	def sort_x(x,size):
		for i in range(size):
			for j in range(0,size-i-1):
				move_abs(x,j)
				#print(x,j,i)
				if measure() > measure(North):
					swap(North)
	def sort_y(y,size):
		for i in range(size):
			for j in range(0,size-i-1):
				move_abs(j,y)
				#print(x,j,i)
				if measure() > measure(East):
					swap(East)
	clear()
	move_abs(0,0)
	size = get_world_size() 
	alldrons = []
	for n in range(drons):
		def plant_cactus():
			for i in range(get_world_size()/drons):
				for y in range(get_world_size()):
					x = n * get_world_size()/drons +i 
					move_abs(x,y)
					if get_water() < 0.25:
						use_item(Items.Water)
					if get_ground_type() != Grounds.Soil:
						till()
					if can_harvest():
						harvest()
					plant(Entities.Cactus)
		d =  spawn_drone(plant_cactus)
		if d :
			alldrons.append(d)
		else:
			plant_cactus()
		#print(num_drones(),max_drones())
	for d in alldrons:
		if not has_finished(d):
			wait_for(d)
	alldrons = []
	#drons = max_drones()
	for x in range(drons):
		def sort():
			for i in range(size/drons):
				sort_x(x * get_world_size()/drons + i,size)
		d =  spawn_drone(sort)
		if d :
			alldrons.append(d)
		else:
			sort()
		#while True:
			#if spawn_drone(sort):
				#break
	for d in alldrons:
		if not has_finished(d):
			wait_for(d)
	alldrons = []		
	for y in range(drons):
		def sort():
			for i in range(size/drons):
				sort_y(y * get_world_size()/drons + i,size)

		d =  spawn_drone(sort)
		if d :
			alldrons.append(d)
		else:
			sort()
	for d in alldrons:
		if not has_finished(d):
			wait_for(d)
	alldrons = []		
	harvest()
get_cactus_one_turn()
#print(1)
unlock(Unlocks.Hats)
unlock(Unlocks.Dinosaurs)

body_size = 1
moved = False
def move_abs_not_check(x,y):
	x_,y_ = get_pos_x(),get_pos_y()
	if x_ < x :
		for i in range(x-x_):
			move(East)
	else:
		for i in range(x_-x):
			move(West)
	if y_ < y :
		for i in range(y-y_):
			move(North)
	else:
		for i in range(y_-y):
			move(South)
#move_abs = move_abs_not_check
def move_all():
	size = get_world_size()
	def check():
		global apple_x 
		global apple_y
		global body_size
		global moved 
		x,y = get_pos_x(),get_pos_y()
		if x == apple_x and y == apple_y:
			l = measure()
			if l :
				apple_x ,apple_y = l[0],l[1]
				body_size += 1
			else :
				moved = False
	def move_and_check(d):
		global moved 
		if	move(d) :
			moved = True
		else:
			moved = False
		check()
		if num_items(Items.Cactus) < 2000:
			return 
	
	def move_circle():
		global apple_x 
		global apple_y
		global body_size
		for i in range(size-2):
			move_and_check(North)
			x,y = get_pos_x(),get_pos_y()
			if x == apple_x and y == apple_y:
				l = measure()
				if l :
					apple_x ,apple_y = l[0],l[1]
					body_size += 1
				else :
					moved = False
		move_and_check(East)
		x,y = get_pos_x(),get_pos_y()
		if x == apple_x and y == apple_y:
			l = measure()
			if l :
				apple_x ,apple_y = l[0],l[1]
				body_size += 1
			else :
				moved = False
		for i in range(size -2):
			move_and_check(South)
			x,y = get_pos_x(),get_pos_y()
			if x == apple_x and y == apple_y:
				l = measure()
				if l :
					apple_x ,apple_y = l[0],l[1]
					body_size += 1
				else :
					moved = False
			
	def move_abs(x,y):
		x_,y_ = get_pos_x(),get_pos_y()
		if x_ < x :
			for i in range(x-x_):
				move_and_check(East)
		else:
			for i in range(x_-x):
				move_and_check(West)
		if y_ < y :
			for i in range(y-y_):
				move_and_check(North)
		else:
			for i in range(y_-y):
				move_and_check(South)
	global apple_x 
	global apple_y
	global body_size 
	global moved 
	move_circle()
	x = get_pos_x()
	moved = False
	if body_size > (size * (size - 1)) * 0.6 :
		for i in range(size/2 - 1):
			move_and_check(East)
			move_circle()
		x = get_pos_x()
		move_abs(x,0)
		move_abs(0,0)
		move_abs(0,1)
		return 
	while (x + 1) * (size -1) < body_size :
		move_and_check(East)
		move_circle()
		x = get_pos_x()
		if x == size -1 :
			move_abs(x,0)
			move_abs(0,0)
			move_abs(0,1)
			return  
		if not moved :
			change_hat(Hats.Brown_Hat)
			return
		if num_items(Items.Cactus) < 2000:
			return 
			#change_hat(Hats.Dinosaur_Hat)
	

	if (x + 1) * (size -1) >= body_size :
		move_and_check(East)
		x,y = get_pos_x(),get_pos_y()
		while apple_x >= x and x != size - 1 :
			if num_items(Items.Cactus) < 2000:
				return 
			if apple_y == 0 :
				if apple_x > x :
					for i in range (apple_x -x):
						move_and_check(East)
				move_and_check(South)
				#apple_x ,apple_y = measure()
				#body_size += 1 
				x,y = get_pos_x(),get_pos_y()
				move_abs(0,0)
				move_abs(0,1)
				return 
			if apple_x >= x :
				x_moved = apple_x - x 
				for i in range(apple_y - y):
					move_and_check(North)
				for i in range(apple_x - x):
					move_and_check(East)
				#apple_x ,apple_y = measure()
				#body_size += 1 
				
				x,y = get_pos_x(),get_pos_y()
				if x_moved > 0 :
					move_abs(x,1)
				if x != size-1:
					move_and_check(East)
			x,y = get_pos_x(),get_pos_y()
			

		move_abs(x,0)
		move_abs(0,0)
		move_abs(0,1)
			 
apple_x, apple_y = 0,1

def snake():
	global apple_x
	global apple_y 
	global body_size
	body_size = 1 
	move_abs_not_check(0,1)
	change_hat(Hats.Dinosaur_Hat)
	apple_x, apple_y = measure()
	move_abs(0,1)
	while True:
		if num_items(Items.Cactus) < 2000:
			return 
		move_all()
		if not moved:
			change_hat(Hats.Brown_Hat)
			break

def get_bones(n):
	if num_items(Items.Bone) > n :
		return 
	while num_items(Items.Bone) < n :
		snake() 
get_bones(1000)

size = get_world_size() 
def move_abs(x,y):
	x_,y_ = get_pos_x(),get_pos_y()
	if x_ < x :
		for i in range(x-x_):
			move(East)
	else:
		for i in range(x_-x):
			move(West)
	if y_ < y :
		for i in range(y-y_):
			move(North)
	else:
		for i in range(y_-y):
			move(South)
size = get_world_size()
def get_grass_multi(num):
	clear()
	if num_items(Items.Hay) > num :
		return
	size = get_world_size()
	drons = max_drones()
	alldrons = []
	if size % drons != 0 :
		size = size - (size % drons)
		set_world_size(size)
	
	for n in range(drons):
		def plant_and_havest():
			while True:
				for i in range(get_world_size()/drons):
					for y in range(get_world_size()):
						x = n * get_world_size()/drons +i
						move_abs(x,y)
						#print(x,y)
						harvest()
						if num_items(Items.Hay) > num :
							return
		d =  spawn_drone(plant_and_havest)
		if d :
			alldrons.append(d)
		else:
			plant_and_havest()

	for d in alldrons:
		wait_for(d)

def get_wood_multi(num):
	clear()
	if num_items(Items.Wood) > num :
		return
	size = get_world_size()
	drons = max_drones()
	alldrons = []
	if size % drons != 0 :
		size = size - (size % drons)
		set_world_size(size)
	
	for n in range(drons):
		def plant_and_havest():
			while True:
				for i in range(get_world_size()/drons):
					for y in range(get_world_size()):
						x = n * get_world_size()/drons +i
						move_abs(x,y)
						if get_water() < 0.25:
							use_item(Items.Water)
						if (x + y)  % 2 == 0 :
							if can_harvest():
								harvest()
								plant(Entities.Tree)
						else:
							if can_harvest():
								harvest()
								plant(Entities.Bush)
								if num_items(Items.Wood) > num :
									return
		d =  spawn_drone(plant_and_havest)
		if d :
			alldrons.append(d)
		else:
			plant_and_havest()
	for d in alldrons:
		wait_for(d)

def get_carrot_multi(num):
	clear()
	if num_items(Items.Carrot) > num :
		return
	size = get_world_size()
	drons = max_drones()
	cost = get_world_size() * get_world_size() * (2 ** (num_unlocked(Unlocks.Carrots)-1))
	get = (num - (num%cost)) + cost * 5
	get_grass_multi(get)
	get_wood_multi(get)
	alldrons = []
	if size % drons != 0 :
		size = size - (size % drons)
		set_world_size(size)
	
	for n in range(drons):
		def plant_and_havest():
			while True:
				for i in range(size / drons):
					for y in range(size):
						x = n * size / drons + i
						move_abs(x, y)
						if get_water() < 0.5:
							use_item(Items.Water)
						if get_ground_type() != Grounds.Soil:
							till()
						if can_harvest():
							harvest()
						plant(Entities.Carrot)
						if num_items(Items.Carrot) > num :
							return
		d =  spawn_drone(plant_and_havest)
		if d :
			alldrons.append(d)
		else:
			plant_and_havest()

	for d in alldrons:
		wait_for(d)
def get_power_multi(num):
	clear()
	if num_items(Items.Power) > num :
		return
	size = get_world_size()
	drons = max_drones()
	cost = get_world_size() * get_world_size() 
	get_carrot_multi(num + 2 * cost)
	
	clear()
	alldrons = []
	if size % drons != 0 :
		size = size - (size % drons)
		set_world_size(size)
	
	for n in range(drons):
		def plant_and_havest():
			while True:
				for i in range(size / drons):
					for y in range(size):
						x = n * size / drons + i
						move_abs(x, y)
						if get_water() < 0.5:
							use_item(Items.Water)
						if get_ground_type() != Grounds.Soil:
							till()
						if can_harvest():
							harvest()
						plant(Entities.Sunflower)
						if num_items(Items.Power) > num :
							return
		d =  spawn_drone(plant_and_havest)
		if d :
			alldrons.append(d)
		else:
			plant_and_havest()

	for d in alldrons:
		wait_for(d)
def get_pumkin_multi(num):
	clear()
	cost = get_world_size() * get_world_size() * (2 ** (num_unlocked(Unlocks.Pumpkins)))
	pre = get_world_size() * get_world_size() * 6 * (2 ** (num_unlocked(Unlocks.Pumpkins)))
	
	get_carrot_multi(num/ 2+ 2 * cost)
	clear()
	size = get_world_size()
	drons = max_drones()
	#set_world_size(16)
	#drons = 16
	size = get_world_size()
	if size % drons != 0 :
		size = size - (size % drons)
		set_world_size(size)
	alldrons = []
	while True:
		if num_items(Items.Pumpkin) > num or num_items(Items.Carrot) < 1024:
			return
		for n in range(drons):
			def plant_and_havest():
				while True:
					dead = 0
					for i in range(size/drons):
						for y in range(size):
							x = n * size/drons  +i
							move_abs(x,y)
							if get_water() < 0.5:
								use_item(Items.Water)
							if get_ground_type() != Grounds.Soil:
								till()
							if not can_harvest():
								harvest()
								dead +=1
							plant(Entities.Pumpkin)
							if num_items(Items.Carrot) < 1024:
								return 
							#move(North)
					if dead == 0 :
						return
						#dead = 0
			d = spawn_drone(plant_and_havest)
			if d :
				alldrons.append(d)
			else:
				plant_and_havest()
		for d in alldrons:
			if not has_finished(d):
				wait_for(d)
		harvest()

def get_cactus_multi():
	drons = max_drones()
	cost = get_world_size() * get_world_size() * (2 ** (num_unlocked(Unlocks.Cactus)))
	while num_items(Items.Pumpkin) < cost :
		get_pumkin_multi()
	aa = num_items(Items.Pumpkin)
	size = get_world_size() 
	if size % drons != 0 :
		size = size - (size % drons)
		set_world_size(size)
	def sort_x(x,size):
		for i in range(size):
			for j in range(0,size-i-1):
				move_abs(x,j)
				#print(x,j,i)
				if measure() > measure(North):
					swap(North)
	def sort_y(y,size):
		for i in range(size):
			for j in range(0,size-i-1):
				move_abs(j,y)
				#print(x,j,i)
				if measure() > measure(East):
					swap(East)
	clear()
	move_abs(0,0)
	size = get_world_size() 
	alldrons = []
	for n in range(drons):
		def plant_cactus():
			for i in range(get_world_size()/drons):
				for y in range(get_world_size()):
					x = n * get_world_size()/drons +i 
					move_abs(x,y)
					if get_water() < 0.25:
						use_item(Items.Water)
					if get_ground_type() != Grounds.Soil:
						till()
					if can_harvest():
						harvest()
					plant(Entities.Cactus)
		d =  spawn_drone(plant_cactus)
		if d :
			alldrons.append(d)
		else:
			plant_cactus()
		#print(num_drones(),max_drones())
	for d in alldrons:
		if not has_finished(d):
			wait_for(d)
	alldrons = []
	#drons = max_drones()
	for x in range(drons):
		def sort():
			for i in range(size/drons):
				sort_x(x * get_world_size()/drons + i,size)
		d =  spawn_drone(sort)
		if d :
			alldrons.append(d)
		else:
			sort()
		#while True:
			#if spawn_drone(sort):
				#break
	for d in alldrons:
		if not has_finished(d):
			wait_for(d)
	alldrons = []		
	for y in range(drons):
		def sort():
			for i in range(size/drons):
				sort_y(y * get_world_size()/drons + i,size)

		d =  spawn_drone(sort)
		if d :
			alldrons.append(d)
		else:
			sort()
	for d in alldrons:
		if not has_finished(d):
			wait_for(d)
	alldrons = []		
	harvest()
def get_cactus_multi(num):
	if num_items(Items.Cactus) > num :
		return 
	while num_items(Items.Cactus) < num :
		drons = max_drones()
		cost = get_world_size() * get_world_size() * (2 ** (num_unlocked(Unlocks.Cactus))) * 10
		get_pumkin_multi(cost)
		aa = num_items(Items.Pumpkin)
		size = get_world_size() 
		if size % drons != 0 :
			size = size - (size % drons)
			set_world_size(size)
		def sort_x(x,size):
			for i in range(size):
				for j in range(0,size-i-1):
					move_abs(x,j)
					#print(x,j,i)
					if measure() > measure(North):
						swap(North)
		def sort_y(y,size):
			for i in range(size):
				for j in range(0,size-i-1):
					move_abs(j,y)
					#print(x,j,i)
					if measure() > measure(East):
						swap(East)
		clear()
		move_abs(0,0)
		size = get_world_size() 
		alldrons = []
		for n in range(drons):
			def plant_cactus():
				for i in range(get_world_size()/drons):
					for y in range(get_world_size()):
						x = n * get_world_size()/drons +i 
						move_abs(x,y)
						if get_water() < 0.25:
							use_item(Items.Water)
						if get_ground_type() != Grounds.Soil:
							till()
						if can_harvest():
							harvest()
						plant(Entities.Cactus)
			d =  spawn_drone(plant_cactus)
			if d :
				alldrons.append(d)
			else:
				plant_cactus()
			#print(num_drones(),max_drones())
		for d in alldrons:
			if not has_finished(d):
				wait_for(d)
		alldrons = []
		#drons = max_drones()
		for x in range(drons):
			def sort():
				for i in range(size/drons):
					sort_x(x * get_world_size()/drons + i,size)
			d =  spawn_drone(sort)
			if d :
				alldrons.append(d)
			else:
				sort()
			#while True:
				#if spawn_drone(sort):
					#break
		for d in alldrons:
			if not has_finished(d):
				wait_for(d)
		alldrons = []		
		for y in range(drons):
			def sort():
				for i in range(size/drons):
					sort_y(y * get_world_size()/drons + i,size)
	
			d =  spawn_drone(sort)
			if d :
				alldrons.append(d)
			else:
				sort()
		for d in alldrons:
			if not has_finished(d):
				wait_for(d)
		alldrons = []		
		harvest()

get_carrot_multi(16000)

unlock(Unlocks.Pumpkins)

get_cactus_multi(12000)

get_gold(8000)
unlock(Unlocks.Megafarm)
#while num_items(Items.Pumpkin) < 8000 :
#	get_pumkin_multi()
#unlock(Unlocks.Expand)

get_power_multi(5000)
get_cactus_multi(12000)
unlock(Unlocks.Dinosaurs)

get_cactus_multi(12000)
get_pumkin_multi(20000)
unlock(Unlocks.Cactus)
get_cactus_multi(12000)
unlock(Unlocks.Mazes)
get_cactus_multi(72000)
unlock(Unlocks.Dinosaurs)

get_cactus_multi(72000)
unlock(Unlocks.Mazes)
get_power_multi(5000)
get_cactus_multi(72000)
def drone():
	n=0
	trigger=[]
	length = 2
	if length ** 2 <= max_drones():
		num = length ** 2 - 1
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
		if num_items(Items.Gold) >= 1000000 or num_items(Items.Weird_Substance) < 1000:
			break
def get_gold_by_weird():
	size = get_world_size()
	length = 2
	if max_drones() == 16:
		length =4

	n=0
	clear()
	#set_world_size(length)
	if length ** 2 <= max_drones():
		num = length ** 2 - 1
	l = []
	for x in range(length):
		for y in range(length):
			l.append((x,y))
	for pos in l:
		if pos[0] == 0 and pos[1] == 0 :
			continue
		move_abs(pos[0],pos[1])
		spawn_drone(drone)
	move_abs(0,0)
	#for i in range(num):
	#	spawn_drone(drone)
	#	if get_pos_x() == length - 1:	
	#		move(North)
	#	move(East)
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
		if num_items(Items.Gold) >=1000000 or num_items(Items.Weird_Substance) < 1000:
			set_world_size(size)
			break
def get_weird_multi(num):
	clear()
	size = get_world_size()
	drons = max_drones()
	#set_world_size(16)
	#drons = 16
	alldrons = []
	while num_items(Items.Weird_Substance) < num :
		
		for n in range(drons):
			def plant_and_havest():
				for i in range(get_world_size()/drons):
					for y in range(get_world_size()):
						x = n * get_world_size()/drons +i 
						move_abs(x,y)
						if x % 2 == 0:
							if x % 4 == 0 and y % 3 == 0:
								plant(Entities.Tree)
								use_item(Items.Weird_Substance)
								if get_water() < 0.7 :
									use_item(Items.Water)
							elif x % 4 != 0 and y % 3 == 1 :
								plant(Entities.Tree)
								use_item(Items.Weird_Substance)
								if get_water() < 0.7 :
									use_item(Items.Water)
						#move(North)
			d =  spawn_drone(plant_and_havest)
			if d :
				alldrons.append(d)
			else:
				plant_and_havest()
		for d in alldrons:
			wait_for(d)
		for n in range(drons):
			def har():
				for i in range(get_world_size()/drons):
					for y in range(get_world_size()):
						x = n * get_world_size()/drons +i 
						move_abs(x,y)
						while True:
							if can_harvest():
								harvest()
								break 
			d =  spawn_drone(har)
			if d :
				alldrons.append(d)
			else:
				har()
get_power_multi(10*1024)
get_carrot_multi(64000)
unlock(Unlocks.Pumpkins)
get_pumkin_multi(84000)
unlock(Unlocks.Expand)
unlock(Unlocks.Expand)
get_weird_multi(32*1024)
get_gold_by_weird()
unlock(Unlocks.Megafarm)
get_weird_multi(64*1024)
get_gold_by_weird()
unlock(Unlocks.Megafarm)
get_power_multi(10*1024)
get_pumkin_multi(120000)
unlock(Unlocks.Cactus)
get_cactus_multi(432*1024)
unlock(Unlocks.Mazes)
get_power_multi(10*1024)
get_grass_multi(778000)
unlock(Unlocks.Trees)
unlock(Unlocks.Grass)
unlock(Unlocks.Carrots)
unlock(Unlocks.Trees)
get_power_multi(40*1024)
get_weird_multi(80*1024*4)

get_cactus_multi(2590000)
get_power_multi(10*1024)
unlock(Unlocks.Mazes)

get_cactus_multi(2590000)
unlock(Unlocks.Dinosaurs)
get_gold_by_weird()
get_cactus_multi(432000)
unlock(Unlocks.Dinosaurs)
get_power_multi(10*1024)
get_cactus_multi(16000000)
unlock(Unlocks.Dinosaurs)
get_power_multi(10*1024)
get_cactus_multi(16000000)
unlock(Unlocks.Dinosaurs)
get_power_multi(10*1024)
get_cactus_multi(1800000)
get_power_multi(10*1024)
unlock(Unlocks.Trees)
unlock(Unlocks.Grass)
unlock(Unlocks.Carrots)
unlock(Unlocks.Pumpkins)
get_pumkin_multi(512000)
unlock(Unlocks.Expand)
while True:
	snake()
	if num_items(Items.Bone) > 2000000:
		break 
unlock(Unlocks.Leaderboard)


