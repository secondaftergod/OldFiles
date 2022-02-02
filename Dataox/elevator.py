import random
from columnar import columnar


class Poverh:
    def __init__(self):
        def rnd1(p):
            rnd = random.randint(0, len(self.poverha_pas) - 1)
            while rnd == p:
                rnd = random.randint(0, len(self.poverha_pas) - 1)
            return rnd

        self.poverha_pas = {a: random.randint(0, 10) for a in range(random.randint(5, 20))}
        self.poverha_pas_finish = self.poverha_pas.copy()
        for i, j in self.poverha_pas.items():
            if j != 0:
                self.poverha_pas[i] = [rnd1(i) for x in range(1, j + 1)]
            if type(self.poverha_pas[i]) == list:
                self.poverha_pas[i].sort()
            elif self.poverha_pas[i] == 0:
                self.poverha_pas[i] = []
        self.poverha_pas[0] = []
        for i in self.poverha_pas_finish.keys():
            self.poverha_pas_finish[i] = []



class Lift(Poverh):
    lift_inside = list()
    lift_poverh = 0
    lift_limit = 5

    def __init__(self):
        super().__init__()

    def up(self):
        for p, l in self.poverha_pas.items():
            self.lift_poverh = p
            try:  # remove from lift
                lst_l_remove = list()
                lst_l_remove.clear()
                for r in self.lift_inside:
                    if r != self.lift_poverh:
                        lst_l_remove.append(r)
                    else:
                        self.poverha_pas_finish[p].append(r)
                self.lift_inside = lst_l_remove
            except IndexError:
                continue
            lst_l = list()
            lst_l.clear()
            if self.lift_limit > len(self.lift_inside):  # add in lift
                for i in l:
                    if self.lift_limit > len(self.lift_inside):
                        if i > self.lift_poverh:
                            self.lift_inside.append(i)
                        else:
                            lst_l.append(i)
                    else:
                        lst_l.append(i)
                self.poverha_pas[p] = lst_l

            headers = ['EXIT', 'INSIDE IN ELEVATOR', 'PASSENGER ON FLOOR']
            data = [[self.poverha_pas_finish[p], self.lift_inside, self.poverha_pas[p]]]
            table = columnar(data, headers, no_borders=True)
            print(f'\t\t\t\tПоверх {self.lift_poverh} UP ^')
            print(table)

    def down(self):
        for p, l in reversed(self.poverha_pas.items()):
            self.lift_poverh = p
            try:  # remove from lift
                lst_l_remove = list()
                lst_l_remove.clear()
                for r in reversed(self.lift_inside):
                    if r != self.lift_poverh:
                        lst_l_remove.append(r)
                    else:
                        self.poverha_pas_finish[p].append(r)
                self.lift_inside = lst_l_remove
            except IndexError:
                continue
            lst_l = list()
            lst_l.clear()
            if self.lift_limit > len(self.lift_inside):  # add in lift
                for i in reversed(l):
                    if self.lift_limit > len(self.lift_inside):
                        if i < self.lift_poverh:
                            self.lift_inside.append(i)
                        else:
                            lst_l.append(i)
                    else:
                        lst_l.append(i)
                self.poverha_pas[p] = lst_l

            headers = ['EXIT', 'INSIDE IN ELEVATOR', 'PASSENGER ON FLOOR']
            data = [[self.poverha_pas_finish[p], self.lift_inside, self.poverha_pas[p]]]
            table = columnar(data, headers, no_borders=True)
            print(f'\t\t\t\tПоверх {self.lift_poverh} DOWN v')
            print(table)

    def check(self):
        chek_list=list()
        chek_list.clear()
        for i,j in self.poverha_pas.items():
            if len(j)!=0:
                chek_list.append(len(j))
        if len(chek_list)==0:
            return False
        else:
            return True


a = Lift()
while a.check():
    a.up()
    a.down()
