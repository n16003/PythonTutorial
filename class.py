class Things:
    pass

class Animate(Things):
    pass

class Animals(Animate):
    def breathe(self):
        pass
    def move(self):
        pass
    def eat_food(self):
        pass

class Mammals(Animals):
    def feed_young_from_trees(self):
        print('feeding young')

class Giraffes(Mammals):
    def eat_leaves_from_trees(self):
        print('eating leaves')

    def left_foot_forward(self):
        print('left foot forward')

    def left_foot_back(self):
        print('left foot back')

    def right_foot_forward(self):
        print('right foot forward')

    def right_foot_back(self):
        print('right foot back')

    def dance(self):
        self.left_foot_forward()
        self.left_foot_back()
        self.right_foot_forward()
        self.right_foot_back()
        self.left_foot_back()
        self.right_foot_back()
        self.right_foot_forward()
        self.right_foot_forward()
reginald = Giraffes()
reginald.dance()