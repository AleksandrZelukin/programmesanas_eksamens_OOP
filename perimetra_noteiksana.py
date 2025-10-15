# Perimetra noteikšana
class Fig():
    def __init__(self, a=0, b=0, c=0, w=0, h=0):
        self.a = a
        self.b = b
        self.c = c
        self.w = w
        self.h = h
    def tr_pr(self):
        perimetrs = self.a + self.b + self.c
        print("Trijstūra perimetrs ir:", perimetrs)
    def sq_pr(self):
        perimetrs = self.a * 4
        print("Kvadrāta perimetrs ir:", perimetrs)
    def rect_pr(self):
        perimetrs = 2 * (self.w + self.h)
        print("Taisnstūra perimetrs ir:", perimetrs)


tr = Fig(3, 4, 5)
tr.tr_pr()

sq = Fig(4)
sq.sq_pr()

rect = Fig(w=4, h=6)
rect.rect_pr()