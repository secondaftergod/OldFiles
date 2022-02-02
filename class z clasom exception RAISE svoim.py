class NonPositiveError(Exception):
    pass
class PositiveList(list):
    def append(self,par):
        if par>0:
            super(PositiveList, self).append(par)
        else:
            raise NonPositiveError

pl=PositiveList()
pl.append(-1)
print(pl)