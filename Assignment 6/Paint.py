from tkinter import *
import tkinter.font
class PaintApp:
    drawing_tool = "pencil"
    left_but = "up"
    x_pos,y_pos = None, None
    x1_line_pt,y1_line_pt,x2_line_pt,y2_line_pt = None,None,None,None
    def __init__(self,root):
        drawing_area = Canvas(root)
        drawing_area.pack()
        slogan = Button(root,text="Pencil",command=lambda: self.changetool("pencil"))
        slogan.pack(side=LEFT)
        slogan = Button(root,text="Line",command=lambda: self.changetool("line"))
        slogan.pack(side=LEFT)
        slogan = Button(root,text="Arc",command=lambda: self.changetool("arc"))
        slogan.pack(side=LEFT)
        slogan = Button(root,text="Oval",command=lambda: self.changetool("oval"))
        slogan.pack(side=LEFT)
        slogan = Button(root,text="Rectangle",command=lambda: self.changetool("rectangle"))
        slogan.pack(side=LEFT)
        drawing_area.bind("<Motion>",self.motion)
        drawing_area.bind("<ButtonPress-1>",self.left_but_down)
        drawing_area.bind("<ButtonRelease-1>",self.left_but_up)
    def changetool(self,s):
        self.drawing_tool=s
    def left_but_down(self,event=None):
        self.left_but = "down"
        self.x1_line_pt = event.x
        self.y1_line_pt = event.y
    def left_but_up(self,event=None):
        self.left_but = "up"
        self.x_pos = None
        self.y_pos = None
        self.x2_line_pt = event.x
        self.y2_line_pt = event.y
        if self.drawing_tool == 'line':
            self.line_draw(event)
        elif self.drawing_tool=='arc':
            self.arc_draw(event)
        elif self.drawing_tool == "oval":
            self.oval_draw(event)
        elif self.drawing_tool == "rectangle":
            self.rectangle_draw(event)
    def motion(self,event=None):
        if self.drawing_tool=='pencil':
            self.pencil_draw(event)
    def pencil_draw(self,event=None):
        if self.left_but == 'down':
            if self.x_pos is not None and self.y_pos is not None:
                event.widget.create_line(self.x_pos,self.y_pos,event.x,event.y,smooth=TRUE)
            self.x_pos = event.x
            self.y_pos = event.y
    def line_draw(self, event=None):
        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt):
            event.widget.create_line(self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt, smooth=TRUE, fill="green")
        
    def arc_draw(self,event=None):
        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt):
            coords = (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt)
            event.widget.create_arc(coords,start=0,extent=150,style=ARC)
    def oval_draw(self, event=None):
        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt,self.y2_line_pt):

            event.widget.create_oval(self.x1_line_pt, self.y1_line_pt,self.x2_line_pt, self.y2_line_pt,fill="midnight blue",outline="yellow",width=2)
  
    def rectangle_draw(self, event=None):
        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt,self.y2_line_pt):
            event.widget.create_rectangle(self.x1_line_pt, self.y1_line_pt,self.x2_line_pt, self.y2_line_pt,fill="midnight blue",outline="yellow",width=2)



root = Tk()
paint_app = PaintApp(root)
root.mainloop()