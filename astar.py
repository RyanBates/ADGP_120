import main
from main import *

class Grid:
	def init(self, x, y, SearchSpace):
		for x in Grid(10):
			for y in Grid(10):
				OPEN = []
				CLOSED = []
				start = (1,1)
				goal = (5,7)
				unwalkable = ((1,1),(0,2),(2,3),(3,1),(4,2),(2,9),(6,2),(4,5),(8,3),(5,5),(3,3),(3,4),(9,6),(7,8),(8,8),(2,7))
				walkable != self.unwalkable
				if (x, y) in unwalkable:
					unwalkable = True
					CLOSED.append(unwalkable)
				else:
					unwalkable = False
					OPEN.append(walkable)
				node = self.walkable, self.unwalkable
				
class Pit:
	def init(self, x, y, Grid):
		hole = self.unwalkable
	
class Wampus:
	def init(self, x, y, Grid):
		finish = self.goal

class Player:
	def init(self, x, y, Grid):
		pos = self.start
	
class ADGP_120:
	def node(self):
		self.width = 20
		self.height = 20
		self.margin = 5
		self.left = (self.margin + self.width) * x + self.margin
		self.top = (self.margin + self.height) * y + self.margin
		self.pos = (x, self.height - y)
		self.center = (self.left + (self.width/2)), (self.top + (self.height/2))

	def current(self):
		

	def neighbor(self, Grid, Player):
		west = current.node - 1
		east = current.node + 1
		north = current.node - width
		south = current.node + width
		northwest = current.node - width - 1
		northeast = current.node - width + 1
		southwest = current.node + width - 1
		southeast = current.node + width + 1
		around = [] and x - 1 from current
		neighors = self.walkable and around[pos]
		CLOSED.append(pos)
		OPEN.append(neighbors)
	
	def path(self, Grid, Pit, Player, Wampus):
		path = []
		self.path = path + [pos]
		current = self.pos
		if(pos == finish):
			return[path]
		else
			print(nope)
		Shortest = None
		for node in grid[pos]:
			if(node not in path):
				newpath = find_path(grid, node, finish, path)
				if (newpath):
					if(not shortest or len(newpath) < len(shortest)):
						newpath = shortest
		return newpath
		
	def print_path(self): 
		node = self.finish
		while node.parent is not self.pos:
			node = node.parent
			print 'path: node: %d,%d' % (node.x, node.y)
		

	def run(self, screen):
		open = self.OPEN
		closed = self.CLOSED
		
		