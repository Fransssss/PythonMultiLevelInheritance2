
class Family():

    def __init__(self, f_name):
        self.f_name = f_name

    def display_f_name(self):
        print("The family's name is " + self.f_name)


class GrandParents(Family):

    def __init__(self, grpa_name, grma_name):
        self.gr_pa_name = grpa_name
        self.gr_ma_name = grma_name

    def the_grand_parents(self):
        print("The grandpa's name is " + self.gr_pa_name)
        print("The grandma's name is " + self.gr_ma_name)


class Parents(Family):

    def __init__(self, pops, moms):
        self.pops = pops
        self.moms = moms

    def the_parents(self):
        print("The father is " + self.pops)
        print("The mother is " + self.moms)


class Children(Family):

    def __init__(self, one_child, two_child):           # I assume there are only two children in the family
        self.o_kid = one_child
        self.t_kid = two_child

    def the_children(self):
        print("The 1st child is " + self.o_kid)
        print("The 2nd child is " + self.t_kid)
