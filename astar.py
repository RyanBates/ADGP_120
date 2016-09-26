class ADGP_120:
	def init(self, SearchSpace):
		for x in Grid(10):
			for y in Grid(10):
				OPEN = []
				CLOSED = []
				parent = None
				start = (1,1)
				goal = (5,7)
				unwalkable = ((1,1),(0,2),(2,3),(3,1),(4,2),(2,9),(6,2),
				(4,5),(8,3),(5,5),(3,3),(3,4),(9,6),(7,8),(8,8),(2,7))
				walkable != self.unwalkable
				if (x, y) in unwalkable:
					unwalkable = True
					CLOSED.append(unwalkable)
				else:
					unwalkable = False
					OPEN.append(walkable)
				parent = start
				

	def node(self):
		self.width = 20
		self.height = 20
		self.margin = 5
		self.left = (self.margin + self.width) * x + self.margin
		self.top = (self.margin + self.height) * y + self.margin
		self.start = (x, self.height - y)
		self.center = (self.left + (self.width/2)), (self.top + (self.height/2))

	def Current(self):
		parent = False
		self.start = current 
		current = self.parent
		CLOSED.append(current)
			
	def neighbors(self):
		if neighbor == (x,y) in walkable:
			node = walkable
		neighbor = node
		west = current.node - 1
		east = current.node + 1
		north = current.node - width
		south = current.node + width
		northwest = current.node - width - 1
		northeast = current.node - width + 1
		southwest = current.node + width - 1
		southeast = current.node + width + 1
		
			
	def Find(self):
		find = []
		if (current == start and neighbor == walkable):
			find[neighbor]
			
	def Closer(self):
		closer = False
		if (self.goal - self.neighbor <= self.goal - self.current):
			closer = True
			
	def Move(self):
		move = False
		if (self.neighbor <= current and self.walkable and self.closer == True):
			self.move = True
			self.current = self.neighbor
	
	def path(self):
		path = [Grid]
		self.path = path + [start]
		current = self.start
		if(current == start and neighbor.walkable == True and closer == True 
		or current == neighbor.walkable == True and closer == True):
			current = neighbor
		if(current == goal):
			return[path]
		else:
			print(nope)
		Shortest = None
		for node in grid[start]:
			if(node not in path):
				newpath = find_path(grid, node, goal, path)
				if (newpath):
					if(not shortest or len(newpath) < len(shortest)):
						newpath = shortest
		return newpath

	def run(self):
		print Grid
		open = self.OPEN
		closed = self.CLOSED
		done = False
		self.start = self.current
		closed.append(current)
		if(move == True):
			self.current = self.neighbor
		if(self.current == self.goal):
			done = True
		print path[]
		
	def main(self):
		run()	