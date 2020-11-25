import math
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
items = []
mean = 0
length = -1
def deter(a, b, c ,d):
    ans = (a * d) - (b * c)
    return ans
class Default(Screen):
    pass
class Quadratic(Screen):
    def btn(self):
        if self.ids.a.text == "" or self.ids.b.text == "" or self.ids.c.text == "":
            self.ids.x1.text = "Please insert a numerical value for all parameters"
            self.ids.x2.text = ""
        else:
            a = float(self.ids.a.text)
            b = float(self.ids.b.text)
            c = float(self.ids.c.text)
            if((b**2) - (4 * a * c) < 0):
                self.ids.x1.text = "error"
                self.ids.x2.text = ""
            else:
                m = math.sqrt(((b**2) - (4 * a * c)))
                x1 = ((-1 * b) + m)/(2 * a)
                x2 = ((-1 * b) - m)/(2 * a)
                self.ids.x1.text = "x1 = " + str(x1)
                self.ids.x2.text = "x2 = " + str(x2)
    def clear(self):
        self.ids.a.text = ""
        self.ids.b.text = ""
        self.ids.c.text = ""
        
class LawOfSINCOS(Screen):
    pass
class LOS(Screen):
    def sub1(self):
        if self.ids.a.text == "" or self.ids.A.text == "" or self.ids.b.text == "":
            self.ids.angle.text = "Please insert a numerical value for all parameters"
        else:
            a = float(self.ids.a.text)
            A = float(self.ids.A.text)
            b = float(self.ids.b.text)
            B1 = (math.sin(A)/a) * b
            B = math.asin(B1)
            self.ids.angle.text = "Final angle = " + str(B) + "°"
    def sub2(self):
        if self.ids.a.text == "" or self.ids.A.text == "" or self.ids.B.text == "":
            self.ids.side.text = "Please insert a numerical value for all parameters"
        else:
            a = float(self.ids.a.text)
            A = float(self.ids.A.text)
            B = float(self.ids.B.text)
            b = (a/math.sin(A)) * math.sin(B)
            self.ids.side.text = "Final side = " + str(B) + "°"
    def clear(self):
        self.ids.a.text = ""
        self.ids.A.text = ""
        self.ids.b.text = ""
        self.ids.B.text = ""
class LOC(Screen):
    def btn(self):
        if self.ids.a.text == "" or self.ids.b.text == "" or self.ids.c.text == "":
            self.ids.ans.text = "Please insert a numerical value for all parameters"
        else:
            a = float(self.ids.a.text)
            b = float(self.ids.b.text)
            c = float(self.ids.c.text)
            p = (math.pi * c)/180
            ans = (a ** 2) + (b ** 2) - (2 * a * b * math.cos(p))
            if(ans < 0):
                self.ids.ans.text = "error"
            else:
                an = math.sqrt(ans)
                self.ids.ans.text = "c = " + str(an)
    def clear(self):
        self.ids.a.text = ""
        self.ids.b.text = ""
        self.ids.c.text = ""
class MatrixMult(Screen):
    pass
class Standard(Screen):
    def set(self):
        global length
        if self.ids.n.text == "":
            self.ids.std.text = "Please insert a numerical value for all parameters"
        else:
            length = int(self.ids.n.text)
            self.ids.num.text = str(length) + " entries left"
    def std(self):
        global items, mean, length
        if length <= 1:
            self.ids.std.text = "Please put in a valid input for the # of entries"
        else:
            if self.ids.d.text == "":
                self.ids.std.text = "Please insert a numerical value for all parameters"
            else:
                if abs(len(items) - length) >= 1:
                    num = float(self.ids.d.text)
                    mean += num
                    items.append(num)
                    self.ids.num.text = str(abs(len(items) - length)) + " entries left"
                    if abs(len(items) - length) == 0:
                        self.ids.d.text = "Press submit for standard deviation"
                    else:
                        self.ids.d.text = ""
                else:
                    sums = 0
                    avg = mean/float(length)
                    for i in range(0, len(items)):
                        sums += (items[i] - avg) * (items[i] - avg)
                    h = sums/float(len(items))
                    std = h ** 0.5
                    self.ids.std.text = "Standard Deviation: " + str(std)
    def clear(self):
        global items, mean
        items = []
        mean = 0
        self.ids.n.text = ""
        self.ids.d.text = "" 
class Slope(Screen):
    def btn(self):
        if self.ids.x1.text == "" or self.ids.x2.text == "" or self.ids.y1.text == "" or self.ids.y2.text == "":
            self.ids.ans.text = "Please insert a numerical value for all parameters"
        else:
            x1 = float(self.ids.x1.text)
            x2 = float(self.ids.x2.text)
            y1 = float(self.ids.y1.text)
            y2 = float(self.ids.y2.text)
            slope = (y1 - y2)/(x1 - x2)
            self.ids.m.text = "Slope = " + str(slope)
    def clear(self):
        self.ids.x1.text = ""
        self.ids.x2.text = ""
        self.ids.y1.text = ""
        self.ids.y2.text = ""
class RADEG(Screen):
    def dr(self):
        if self.ids.d1.text == "":
            self.ids.r1.text = "Please insert a numerical value for all parameters"
        else:
            d = float(self.ids.d1.text)
            r = d/180.0
            self.ids.r1.text = "Radians: " + str(r) + "π"
    def clear(self):
        self.ids.d1.text = ""
        self.ids.r2.text = ""
    def rd(self):
        if self.ids.r2.text == "":
            self.ids.d2.text = "Please insert a numerical value for all parameters"
        else:
            r = float(self.ids.r2.text)
            d = r * 180
            self.ids.d2.text = "Degrees: " + str(d) + "°"         
class TWO(Screen):
    def btn(self):
        if self.ids.a.text == "" or self.ids.b.text == "" or self.ids.c.text == "" or self.ids.d.text == "":
            self.ids.ans.text = "Please insert a numerical value for all parameters"
        else:
            a = float(self.ids.a.text)
            b = float(self.ids.b.text)
            c = float(self.ids.c.text)
            d = float(self.ids.d.text)
            det = deter(a, b, c, d)
            self.ids.ans.text = "Determinant: " + str(det)
            
    def clear(self):
        self.ids.a.text = ""
        self.ids.b.text = ""
        self.ids.c.text = ""
        self.ids.d.text = ""
class THREE(Screen):
    def btn(self):
        if self.ids.a.text == "" or self.ids.b.text == "" or self.ids.c.text == "" or self.ids.d.text == "" or self.ids.e.text == "" or self.ids.f.text == "" or self.ids.g.text == "" or self.ids.h.text == "" or self.ids.i.text == "":
            self.ids.ans.text = "Please insert a numerical value for all parameters"
        else:
            a = float(self.ids.a.text)
            b = float(self.ids.b.text)
            c = float(self.ids.c.text)
            d = float(self.ids.d.text)
            e = float(self.ids.e.text)
            f = float(self.ids.f.text)
            g = float(self.ids.g.text)
            h = float(self.ids.h.text)
            i = float(self.ids.i.text)
            seca = a * deter(e, f, h, i)
            secb = b * deter(d, f, g, i)
            secc = c * deter(d, e, g, h)
            det = seca - secb + secc
            self.ids.ans.text = "Determinant: " + str(det)
            
    def clear(self):
        self.ids.a.text = ""
        self.ids.b.text = ""
        self.ids.c.text = ""
        self.ids.d.text = ""
        self.ids.e.text = ""
        self.ids.f.text = ""
        self.ids.g.text = ""
        self.ids.h.text = ""
        self.ids.i.text = ""

class WM(ScreenManager):
    pass

kv = Builder.load_file("math.kv")

class MathApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    MathApp().run()
