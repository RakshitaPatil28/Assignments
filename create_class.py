#Creating The Class
class Phone:
    
    def make_call(self):
        print("Making phone call")

    def play_game(self):
        print("Playing game")

    #Adding parameters to the class
        
    def set_color(self,color):
        self.color=color
        
    def set_cost(self,cost):
        self.cost=cost

    def show_color(self):
        return self.color

    def show_cost(self):
        return self.cost

p1=Phone()
p1.make_call()
p1.play_game()
p1.set_color("red")
p1.set_cost(25)
print(p1.show_color())
print(p1.show_cost())

