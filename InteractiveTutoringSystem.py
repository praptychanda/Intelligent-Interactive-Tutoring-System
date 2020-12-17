from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
import random
from PIL import ImageTk, Image


root = Tk()
root.geometry("800x800")
root.configure(bg='white')
fig = plt.figure()


root.title("Linear Equations Plot")

# Frames creation

frame1 = Frame(root, padx=10, pady=10,bg='white')
frame2 = Frame(root, padx=10, pady=10,bg='white')
frame3 = Frame(root, padx=10, pady=10,bg='white')
frame4 = Frame(root, padx=10, pady=10,bg='white')
frame5 = Frame(root, padx=10, pady=10,bg='white')
test_frame = Frame(root, padx=10,pady=10,bg='white')

#graphImages Creation
graph1 = Image.open("graph1.png")
resized_graph1 = graph1.resize((250,250),Image.ANTIALIAS)
new_graph1 = ImageTk.PhotoImage(resized_graph1)

graph2=Image.open("no soln.png")
resized_graph2 = graph2.resize((250,250),Image.ANTIALIAS)
new_graph2 = ImageTk.PhotoImage(resized_graph2)

graph3=Image.open("infinite soln.png")
resized_graph3 = graph3.resize((250,250),Image.ANTIALIAS)
new_graph3 = ImageTk.PhotoImage(resized_graph3)

graph4=Image.open("unique soln.png")
resized_graph4 = graph4.resize((250,250),Image.ANTIALIAS)
new_graph4 = ImageTk.PhotoImage(resized_graph4)

#ALL FUNCTIONS

#1
def randno():
    no=random.randint(-8,8)
    if no==0:
        return randno()
    else:
        return no

#2
def slope_from_eq(a,b,c):
    m=-(a/b)
    return m

#3
def intercept_from_eq(a,b,c):
    d=c/b
    return d

#4
def slope_from_points(p1,p2):
    m = (p2[1] - p1[1]) / (p2[0] - p1[0])
    return m

#5
def intercept_from_points(p1,p2):
    m = (p2[1] - p1[1]) / (p2[0] - p1[0])
    c = p2[1] - (m * p2[0])
    return c

#6
def interPoint_equations(A, B):
    determinant = A[0] * B[1] - A[1] * B[0]

    if (determinant == 0):
        # The lines are parallel. The function returns 0
        return 0
    else:
        final_point = []
        x = (B[1] * A[2] - A[1] * B[2]) / determinant
        y = (A[0] * B[2] - B[0] * A[2]) / determinant
        final_point.append(x)
        final_point.append(y)
        return final_point

#7
def graph_from_points(p1, p2):
    x_values = [p1[0], p2[0]]
    y_values = [p1[1], p2[1]]
    coefficients = np.polyfit(x_values, y_values, 1)
    polynomial = np.poly1d(coefficients)
    x_axis = np.linspace(-20, 20, 10)
    y_axis = polynomial(x_axis)

    m = (p2[1] - p1[1]) / (p2[0] - p1[0])
    c = p2[1] - (m * p2[0])

    ax = plt.gca()
    ax.plot(x_axis, y_axis,'r')
    plt.plot(p1[0], p1[1], 'go')
    plt.plot(p2[0], p2[1], 'go')
    ax.grid(True)
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')
    plt.xlim(-8, 8)
    plt.ylim(-8, 8)

    plt.show()

#8
def graph():
    ax=plt.gca()
    ax.grid(True)
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')
    plt.xlim(-8, 8)
    plt.ylim(-8, 8)
    plt.show()

#9
def plot_first_point(p1):

    ax = plt.gca()
    ax.plot(p1[0], p1[1])
    plt.plot(p1[0], p1[1], 'go')

    ax.grid(True)
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')
    plt.xlim(-8, 8)
    plt.ylim(-8, 8)
    plt.show()

#10
def plot_third_point(p1,p2,p3):
    x_values = [p1[0], p2[0]]
    y_values = [p1[1], p2[1]]
    coefficients = np.polyfit(x_values, y_values, 1)
    polynomial = np.poly1d(coefficients)
    x_axis = np.linspace(-20, 20, 10)
    y_axis = polynomial(x_axis)

    m = (p2[1] - p1[1]) / (p2[0] - p1[0])
    c = p2[1] - (m * p2[0])

    ax = plt.gca()
    ax.plot(x_axis, y_axis,'r')
    plt.plot(p1[0], p1[1], 'go')
    plt.plot(p2[0], p2[1], 'go')
    plt.plot(p3[0], p3[1], 'go')
    ax.grid(True)
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')
    plt.xlim(-8, 8)
    plt.ylim(-8, 8)

    plt.show()

#11
def plot_two_lines(p1,p2,p3,p4):
    x_values = [p1[0], p2[0]]
    y_values = [p1[1], p2[1]]
    coefficients = np.polyfit(x_values, y_values, 1)
    polynomial = np.poly1d(coefficients)
    x_axis = np.linspace(-20, 20, 10)
    y_axis = polynomial(x_axis)

    m = (p2[1] - p1[1]) / (p2[0] - p1[0])
    c = p2[1] - (m * p2[0])


    x_values1 = [p3[0], p4[0]]
    y_values1 = [p3[1], p4[1]]
    coefficients1 = np.polyfit(x_values1, y_values1, 1)
    polynomial1 = np.poly1d(coefficients1)
    x_axis1 = np.linspace(-20, 20, 10)
    y_axis1 = polynomial1(x_axis1)

    m1 = (p4[1] - p3[1]) / (p4[0] - p3[0])
    c1 = p4[1] - (m1 * p4[0])

    ax = plt.gca()
    ax.plot(x_axis, y_axis,'r')
    ax.plot(x_axis1, y_axis1,'r')
    plt.plot(p1[0], p1[1], 'go')
    plt.plot(p2[0], p2[1], 'go')
    plt.plot(p3[0], p3[1], 'go')
    plt.plot(p4[0], p4[1], 'go')


    ax.grid(True)
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')
    plt.xlim(-8, 8)
    plt.ylim(-8, 8)

    plt.show()

#12
def plot_interPoint_equations(A, B):
    plt.close(fig)
    x1 = list(range(-20, 20))
    d1 = A[2] / A[1]
    y1 = [(m1 * i + d1) for i in x1]

    x2 = list(range(-20, 20))
    m2 = -(B[0] / B[1])
    d2 = B[2] / B[1]
    y2 = [(m2 * i + d2) for i in x2]

    interPoint = interPoint_equations(A, B)

    ax = plt.gca()
    ax.plot(x1, y1)
    ax.plot(x2, y2)

    plt.plot(interPoint[0], interPoint[1], 'go')

    plt.text(interPoint[0], interPoint[1], '({}, {})'.format(interPoint[0], interPoint[1]))

    ax.grid(True)
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')
    plt.xlim(-8, 8)
    plt.ylim(-8, 8)

    plt.show()


#13

#FRAME1
frame1.grid(padx=50, pady=50)


Label(frame1,text="             ",bg='white').grid(row=0,column=1)
Label(frame1,text="             ",bg='white').grid(row=1,column=1)
Label(frame1,text="             ",bg='white').grid(row=2,column=1)
Label(frame1, text="Welcome to the linear algebra tutoring system",bg='white',font="Times 25 bold italic").grid(row=3,column=1)
Label(frame1,text="             ",bg='white').grid(row=4,column=1)




def gotoframe2():

    frame1.destroy()

    global new_graph1

    frame2.grid(padx=20, pady=20)

    Label(frame2, text="Algebraic Equation", bg='white', font="Times 14 bold").grid()
    string2 = '''
    An algebraic equation is an equality involving variables,constants and coefficients.
    The expression on the left of the equality sign is the Left Hand Side(LHS) and
    the expression on the right of the equality sign is the Right Hand Side(RHS).
    The LHS and RHS are equal only for certain values of the variables. These values are the solutions of the equation.
    The solutions may be of the following 3 types:
    •	Unique Solution – Equation has 1 solution
    •	Infinite Solution – Equation has many solutions
    •	No Solution – Equation does not have any solution
    '''
    Label(frame2, text=string2, bg='white', font="Times 12").grid()
    Label(frame2,text="Graphical Method for Solving Equations",bg="white",font="Times 14 bold" ).grid()
    string2_2='''To get the solutions of equations, we can plot a line corresponding to each equation and solve it.
    Here is how we can plot a graph from an equation:
                                                        2x – y +2 = 0
    Substituting x=0                                                                                                          Substituting y=4
    2*0 – y + 2 = 0                                                                                                                2x – 4 + 2 = 0
    y = 2                                                                                                                                 2x – 2 = 0
    (0 , 2)                                                                                                                               2x = 2
                                                                                                                                              x = 1
                                                                                                                                             (1 , 4)
    Therefore a line joining the two points (0,2) and (1,4) should be plotted.
    '''

    Label(frame2, text=string2_2,bg='white',font="Times 12").grid()

    Label(frame2,image=new_graph1).grid()
    Label(frame2,text=" ",bg='white').grid()
    Button(frame2, text="NEXT", command=gotoframe3).grid()


Button(frame1, text="START", command=gotoframe2).grid(row=5,column=1)


def gotoframe3():
    frame2.destroy()


    global new_graph2

    frame3.grid(padx=20, pady=20)

    Label(frame3, text="To solve a pair of equations", bg='white', font="Times 14 bold").grid()
    string3 = '''We plot the lines corresponding to each equation.
    •	If the two lines plotted are parallel to each other, then there are no solutions.
    •	If the two lines plotted are incident on each other, then there are infinite solutions.
    •	If the two lines plotted intersect each other at a point, then the point of intersection is the unique solution.'''

    Label(frame3, text=string3, bg='white', font="Times 12").grid()

    Label(frame3,text="Example for no solution:", bg='white', font="Times 14 bold").grid()
    string3_2='''Equations:
    x-2y+2=0                                                                                            x-2y-2=0

    x	-2	2                                                                                                   x	2	-2
    y	0	2                                                                                                   y	0	-2
    '''
    string3_3 = "Therefore, the pair of equation has no solution."
    Label(frame3, text=string3_2,bg='white', font="Times 12").grid()

    Label(frame3,image=new_graph2).grid()

    Label(frame3, text=string3_3,bg='white', font="Times 12").grid()
    Label(frame3, text=" ",bg='white').grid()

    Button(frame3, text="NEXT", command=gotoframe4).grid()


def gotoframe4():
    frame3.destroy()

    global new_graph3

    frame4.grid(padx=20, pady=20)


    Label(frame4,text="Example for infinite solution",bg="white",font="Times 14 bold").grid()
    string4 = '''Equations:
    x+y=4                                                                                                        2x+2y=8
    X	0	4                                                                                                               X	2	6
    Y	4	0                                                                                                             Y	2	-2

        '''

    string4_2 = '''A,B have been plotted corresponding to the 1st equation and
    C,D have been plotted corresponding to the 2nd equation.
    Since both pairs of points lie on the same line,thus the lines plotted are
    incident and have infinite solutions.
    '''
    Label(frame4, text=string4,bg='white',font="Times 12").grid()

    Label(frame4,image=new_graph3).grid()
    Label(frame4, text=" ",bg='white').grid()
    Label(frame4, text=string4_2,bg='white',font="Times 12").grid()
    Label(frame4, text=" ",bg='white').grid()
    Button(frame4, text="NEXT", command=gotoframe5).grid()


def gotoframe5():

    frame4.destroy()


    global new_graph4

    frame5.grid(padx=20, pady=20)

    Label(frame5, text="Example for unique solution", bg="white", font="Times 14 bold").grid()
    string5 = '''Equations:
    2x-y+2=0                                                                                                  x-y-1=0


    X	0	1                                                                                                                   x	0	1
    y	2	4                                                                                                                   Y	-1	0
    '''

    string5_2 = '''The point of intersection of the two lines is the  unique solution, which is (-3,-4).'''
    Label(frame5, text=string5,bg='white',font="Times 12").grid()

    Label(frame5, image=new_graph4).grid()
    Label(frame5, text=" ",bg='white').grid()
    Label(frame5, text=string5_2,bg='white',font="Times 12 bold").grid()
    Label(frame5, text=" ",bg='white').grid()
    Button(frame5, text="GO TO TEST MODE",command=testmode).grid()

#GLOBAL variables
x_coeff_1=1
y_coeff_1=1
const_1 = 5

x_coeff_2=2
y_coeff_2=1
const_2 =6


coords=[]
r = StringVar()
e = Entry(test_frame)

def onclick(event):
    global ix, iy
    ix, iy = event.xdata, event.ydata

    global coords
    coords.append(round(ix*2)/2)
    coords.append(round(iy*2)/2)


    if len(coords) == 2:
        fig.canvas.mpl_disconnect(cid)

    p1 = [coords[0], coords[1]]

    plot_first_point(p1)

def onclick2(event):
    global ix2, iy2
    ix2, iy2 = event.xdata, event.ydata

    global coords
    coords.append(round(ix2*2)/2)
    coords.append(round(iy2*2)/2)

    if len(coords) == 4:
        fig.canvas.mpl_disconnect(did)

    p1 = [coords[0], coords[1]]
    p2 = [coords[2], coords[3]]

    graph_from_points(p1, p2)

def onclick3(event):
    global ix3, iy3
    ix3, iy3 = event.xdata, event.ydata

    global coords
    coords.append(round(ix3*2)/2)
    coords.append(round(iy3*2)/2)

    if len(coords) == 6:
        fig.canvas.mpl_disconnect(eid)

    p1 = [coords[0], coords[1]]
    p2 = [coords[2], coords[3]]
    p3 = [coords[4], coords[5]]

    plot_third_point(p1,p2,p3)

def onclick4(event):
    global ix4, iy4
    ix4, iy4 = event.xdata, event.ydata

    global coords
    coords.append(round(ix4*2)/2)
    coords.append(round(iy4*2)/2)

    if len(coords) == 8:
        fig.canvas.mpl_disconnect(fid)

    p1 = [coords[0], coords[1]]
    p2 = [coords[2], coords[3]]
    p3 = [coords[4], coords[5]]
    p4 = [coords[6], coords[7]]

    plot_two_lines(p1,p2,p3,p4)

cid = fig.canvas.mpl_connect('button_press_event', onclick)
did = fig.canvas.mpl_connect('button_press_event', onclick2)
eid = fig.canvas.mpl_connect('button_press_event', onclick3)
fid = fig.canvas.mpl_connect('button_press_event', onclick4)

answer_list=[]
val=""

def answer(coord):
    global x_coeff_1
    global y_coeff_1
    global const_1
    global x_coeff_2
    global y_coeff_2
    global const_2
    global r
    global e
    global answer_list
    global val
    A=[x_coeff_1,y_coeff_1,const_1]
    B=[x_coeff_2,y_coeff_2,const_2]

    p1=[]
    p2=[]
    p3=[]
    p4=[]
    p1.append(coord[0])
    p1.append(coord[1])

    p2.append(coord[2])
    p2.append(coord[3])

    p3.append(coord[4])
    p3.append(coord[5])

    p4.append(coord[6])
    p4.append(coord[7])

    correct_slope_1= slope_from_eq(x_coeff_1,y_coeff_1,const_1)
    student_slope_1= slope_from_points(p1,p2)

    correct_intercept_1= intercept_from_eq(x_coeff_1,y_coeff_1,const_1)
    student_intercept_1= intercept_from_points(p1,p2)

    if (correct_intercept_1==student_intercept_1 and correct_slope_1==student_slope_1):
        answer_list.append(True)
        #answer_list[0]=True
    else:
        answer_list.append(False)
        #answer_list[0] = False

    correct_slope_2 = slope_from_eq(x_coeff_2, y_coeff_2, const_2)
    student_slope_2 = slope_from_points(p3, p4)

    correct_intercept_2 = intercept_from_eq(x_coeff_2, y_coeff_2, const_2)
    student_intercept_2 = intercept_from_points(p3, p4)

    if (correct_intercept_2 == student_intercept_2 and correct_slope_2 == student_slope_2):
        answer_list.append(True)
        #answer_list[1] = True
    else:
        answer_list.append(False)
        #answer_list[1] = False


    intersectionPoint= interPoint_equations(A, B)

    if (correct_slope_1==correct_slope_2 and correct_intercept_1==correct_intercept_2):
        val="infinite solutions"
    elif len(intersectionPoint)==2:
        val="unique solution"
    else:
        val="no solution"

    if val==r.get():
        answer_list.append(True)
        #answer_list[2] = True
    else:
        answer_list.append((False))
        #answer_list[2] = False

    point=[]
    point = [float(x) for x in e.get().split(',')]
    if (intersectionPoint==len(point)-1):
        answer_list.append(True)
        #answer_list[3] = True
    elif intersectionPoint[0]==point[0] and intersectionPoint[1]==point[1]:
        answer_list.append(True)
        #answer_list[3] = True
    else:
        answer_list.append(False)
        #answer_list[3] = False


    if answer_list[0]==False:
        Label(test_frame,text="The first line drawn is INCORRECT",bg='white',font="Times 14").grid()

    if answer_list[1]==False:
        Label(test_frame, text="The second line drawn is INCORRECT",bg='white',font="Times 14").grid()
    if answer_list[2]==False:
        Label(test_frame, text="Oops!  INCORRECT! The given equations have " + val,bg='white',font="Times 14").grid()
    if answer_list[3]==False and val=="no solution":
        Label(test_frame, text="There is NO intersecting point",bg='white',font="Times 14").grid()
    elif answer_list[3]==False and val=="infinite solutions":
        Label(test_frame, text="There is NO unique solution.",bg='white',font="Times 14").grid()
    elif answer_list[3]==False:
        Label(test_frame, text="The intersecting point is INCORRECT. The correct intersection point is "+str(intersectionPoint[0])+","+str(intersectionPoint[1]),bg='white',font="Times 14").grid()

    marks= answer_list.count(True)
    global percentage
    percentage=(marks/4)*100
    if percentage>=75:
        Label(test_frame, text="CONGRATULATIONS!!! You have scored " + str(percentage) + "%",bg='white',fg="red",font="Times 14").grid()
    else:
        Label(test_frame,text="You have scored "+str(percentage)+"%",bg='white',font="Times 14").grid()

    if answer_list.count(False)>0:
        plot_interPoint_equations(A,B)


def quit():
    root.destroy()
    exit()


def testmode():
    frame5.destroy()

    global x_coeff_1
    global y_coeff_1
    global const_1
    global x_coeff_2
    global y_coeff_2
    global const_2
    global e
    global r
    global flag

    test_frame.grid(padx=20, pady=20)

    Label(test_frame, text="            ",bg='white').grid(row=0, column=0)

    Label1 = Label(test_frame, text="Plot the following linear equations on graph.",bg='white',font="Times 14 bold")
    Label1.grid(row=1, column=0)

    Label(test_frame, text="            ",bg='white').grid(row=2, column=0)

    first_eq = Label(test_frame, text="x + y = 5",bg='white',font="Times 14")
    first_eq.grid(row=3, column=0)

    second_eq = Label(test_frame, text="2x + y = 6",bg='white',font="Times 14")
    second_eq.grid(row=4, column=0)

    Label(test_frame, text="            ",bg='white').grid(row=5, column=0)

    new_Button = Button(test_frame, text="Plot on Graph", command=graph)
    new_Button.grid(row=3, column=1)

    r.set("infinite solutions")

    Label(test_frame, text="The given set of equation has:",bg='white',font="Times 14 bold").grid(row=6, column=0)

    Radiobutton(test_frame, text="Infinite solutions", variable=r, value="infinite solutions",bg='white',font="Times 12").grid(row=7, column=0)
    Radiobutton(test_frame, text="No solution", variable=r, value="no solution",bg='white',font="Times 12").grid(row=8, column=0)
    Radiobutton(test_frame, text="Unique solution", variable=r, value="unique solution",bg='white',font="Times 12").grid(row=9, column=0)

    Label(test_frame, text="                                         ",bg='white').grid(row=10, column=0)

    Label(test_frame, text="If the lines intersect each other at a unique point, what is the intersection point?",bg='white',font="Times 14 bold").grid(
        row=11, column=0)


    e.grid(row=12, column=0)

    Submit = Button(test_frame, text="SUBMIT", command=lambda: answer(coords))
    Submit.grid(row=13, column=1)


    next_button = Button(test_frame, text = "Go to next level", command = lambda: event_handler_for_lambda(percentage))
    next_button.grid(row=14, column=1)

    clear_button = Button(test_frame, text="End", command=quit)
    clear_button.grid(row=15, column=1)




############################


def event_handler_for_lambda(per):
    if per < 75:
        gotoframe12()
    else:
        testmode2()

frame12 = Frame(root, padx=10, pady=10,bg='white')
frame13 = Frame(root, padx=10, pady=10,bg='white')
frame14 = Frame(root, padx=10, pady=10,bg='white')
frame15 = Frame(root, padx=10, pady=10,bg='white')
test_frame2 = Frame(root, padx=10,pady=10,bg='white')

def gotoframe12():

    test_frame.destroy()

    global new_graph1

    frame12.grid(padx=20, pady=20)

    Label(frame12, text="Algebraic Equation", bg='white', font="Times 14 bold").grid()
    string2 = '''
    An algebraic equation is an equality involving variables,constants and coefficients.
    The expression on the left of the equality sign is the Left Hand Side(LHS) and
    the expression on the right of the equality sign is the Right Hand Side(RHS).
    The LHS and RHS are equal only for certain values of the variables. These values are the solutions of the equation.
    The solutions may be of the following 3 types:
    •	Unique Solution – Equation has 1 solution
    •	Infinite Solution – Equation has many solutions
    •	No Solution – Equation does not have any solution
    '''
    Label(frame12, text=string2, bg='white', font="Times 12").grid()
    Label(frame12,text="Graphical Method for Solving Equations",bg="white",font="Times 14 bold" ).grid()
    string2_2='''To get the solutions of equations, we can plot a line corresponding to each equation and solve it.
    Here is how we can plot a graph from an equation:
                                                        2x – y +2 = 0
    Substituting x=0                                                                                                          Substituting y=4
    2*0 – y + 2 = 0                                                                                                                2x – 4 + 2 = 0
    y = 2                                                                                                                                 2x – 2 = 0
    (0 , 2)                                                                                                                               2x = 2
                                                                                                                                              x = 1
                                                                                                                                             (1 , 4)
    Therefore a line joining the two points (0,2) and (1,4) should be plotted.
    '''

    Label(frame12, text=string2_2,bg='white',font="Times 12").grid()

    Label(frame12,image=new_graph1).grid()
    Label(frame12,text=" ",bg='white').grid()
    Button(frame12, text="NEXT", command=gotoframe13).grid()


def gotoframe13():
    frame12.destroy()


    global new_graph2

    frame13.grid(padx=20, pady=20)

    Label(frame13, text="To solve a pair of equations", bg='white', font="Times 14 bold").grid()
    string3 = '''We plot the lines corresponding to each equation.
    •	If the two lines plotted are parallel to each other, then there are no solutions.
    •	If the two lines plotted are incident on each other, then there are infinite solutions.
    •	If the two lines plotted intersect each other at a point, then the point of intersection is the unique solution.'''

    Label(frame13, text=string3, bg='white', font="Times 12").grid()

    Label(frame13,text="Example for no solution:", bg='white', font="Times 14 bold").grid()
    string3_2='''Equations:
    x-2y+2=0                                                                                            x-2y-2=0

    x	-2	2                                                                                                   x	2	-2
    y	0	2                                                                                                   y	0	-2
    '''
    string3_3 = "Therefore, the pair of equation has no solution."
    Label(frame13, text=string3_2,bg='white', font="Times 12").grid()

    Label(frame13,image=new_graph2).grid()

    Label(frame13, text=string3_3,bg='white', font="Times 12").grid()
    Label(frame13, text=" ",bg='white').grid()

    Button(frame13, text="NEXT", command=gotoframe14).grid()


def gotoframe14():
    frame13.destroy()

    global new_graph3

    frame14.grid(padx=20, pady=20)


    Label(frame14,text="Example for infinite solution",bg="white",font="Times 14 bold").grid()
    string4 = '''Equations:
    x+y=4                                                                                                        2x+2y=8
    X	0	4                                                                                                               X	2	6
    Y	4	0                                                                                                             Y	2	-2

        '''

    string4_2 = '''A,B have been plotted corresponding to the 1st equation and
    C,D have been plotted corresponding to the 2nd equation.
    Since both pairs of points lie on the same line,thus the lines plotted are
    incident and have infinite solutions.
    '''
    Label(frame14, text=string4,bg='white',font="Times 12").grid()

    Label(frame14,image=new_graph3).grid()
    Label(frame14, text=" ",bg='white').grid()
    Label(frame14, text=string4_2,bg='white',font="Times 12").grid()
    Label(frame14, text=" ",bg='white').grid()
    Button(frame14, text="NEXT", command=gotoframe15).grid()


def gotoframe15():

    frame14.destroy()


    global new_graph4

    frame15.grid(padx=20, pady=20)

    Label(frame15, text="Example for unique solution", bg="white", font="Times 14 bold").grid()
    string5 = '''Equations:
    2x-y+2=0                                                                                                  x-y-1=0


    X	0	1                                                                                                                   x	0	1
    y	2	4                                                                                                                   Y	-1	0
    '''

    string5_2 = '''The point of intersection of the two lines is the  unique solution, which is (-3,-4).'''
    Label(frame15, text=string5,bg='white',font="Times 12").grid()

    Label(frame15, image=new_graph4).grid()
    Label(frame15, text=" ",bg='white').grid()
    Label(frame15, text=string5_2,bg='white',font="Times 12 bold").grid()
    Label(frame15, text=" ",bg='white').grid()
    Button(frame15, text="GO TO TEST MODE").grid()
    clear_button = Button(frame15, text="End", command=quit)
    clear_button.grid()


coords2=[]
r2 = StringVar()
e2 = Entry(test_frame2)


def testmode2():
    test_frame.destroy()

    global x_coeff_1
    global y_coeff_1
    global const_1
    global x_coeff_2
    global y_coeff_2
    global const_2
    global e2
    global r2
    global flag2

    test_frame2.grid(padx=20, pady=20)

    Label(test_frame2, text="            ",bg='white').grid(row=0, column=0)

    Label1 = Label(test_frame2, text="Plot the following linear equations on graph.",bg='white',font="Times 14 bold")
    Label1.grid(row=1, column=0)

    Label(test_frame2, text="            ",bg='white').grid(row=2, column=0)

    first_eq = Label(test_frame2, text="7x - 8y = -12", bg='white', font="Times 14")
    first_eq.grid(row=3, column=0)

    second_eq = Label(test_frame2, text="-4x + 2y = 3", bg='white', font="Times 14")
    second_eq.grid(row=4, column=0)

    Label(test_frame2, text="            ",bg='white').grid(row=5, column=0)

    new_Button = Button(test_frame2, text="Plot on Graph", command=graph2)
    new_Button.grid(row=3, column=1)

    r2.set("infinite solutions")

    Label(test_frame2, text="The given set of equation has:",bg='white',font="Times 14 bold").grid(row=6, column=0)

    Radiobutton(test_frame2, text="Infinite solutions", variable=r2, value="infinite solutions",bg='white',font="Times 12").grid(row=7, column=0)
    Radiobutton(test_frame2, text="No solution", variable=r2, value="no solution",bg='white',font="Times 12").grid(row=8, column=0)
    Radiobutton(test_frame2, text="Unique solution", variable=r2, value="unique solution",bg='white',font="Times 12").grid(row=9, column=0)

    Label(test_frame2, text="                                         ",bg='white').grid(row=10, column=0)

    Label(test_frame2, text="If the lines intersect each other at a unique point, what is the intersection point?",bg='white',font="Times 14 bold").grid(
        row=11, column=0)


    e2.grid(row=12, column=0)

    Submit = Button(test_frame2, text="SUBMIT", command=lambda: answer2(coords2))
    Submit.grid(row=13, column=1)


    clear_button = Button(test_frame2, text="End", command=quit)
    clear_button.grid(row=14, column=1)

root.mainloop()