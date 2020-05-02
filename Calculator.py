from tkinter import *
import sympy

# 生成主界面
window = Tk()
window.title('微积分计算器--- By Ren Thomas')
window.geometry('640x640')
window.geometry('640x640+450+90')
window.iconbitmap('ironman.ico')
window.wm_resizable(False,False)

# 上方图片
canvas = Canvas(window, bg='white', height=200, width=640)
image_file = PhotoImage(file='bg.png')
image = canvas.create_image(0,0, anchor='nw', image=image_file)
canvas.pack()

# 定义函数变量
x = sympy.Symbol('x')
y = sympy.Symbol('y')

def solve_equation(f1, f2):
    return sympy.solve([f1, f2], [x, y])

def solve_limit(f, x, num):
    return sympy.limit(f, x, num)

def solve_derivative(f, x):
    return sympy.diff(f, x)

def solve_partial_derivative(f, x, y):
    x1 = sympy.diff(f, x)
    y1 = sympy.diff(f, y)
    answer_pder.insert('insert', "对x求偏导："+"\n")
    answer_pder.insert('insert', x1)
    answer_pder.insert('insert', "\n"+"\n")
    answer_pder.insert('insert', "对y求偏导："+"\n")
    answer_pder.insert('insert', y1)
    answer_pder.insert('insert', "\n"+"\n")

def solve_d_integral(f, x, down_um, up_num,):
    return sympy.integrate(f,(x, down_um, up_num))

def solve_b_d_integral(f, x):
    return sympy.integrate(f, x)

def hit():
    button_fun.place(x=20, y=220)
    button_lim.place(x=20, y=280)
    button_der.place(x=20, y=340)
    button_par.place(x=20, y=400)
    button_itg.place(x=20, y=460)
    button_bitg.place(x=20, y=520)


# 方程组
var1 = StringVar
var2 = StringVar
answer_fun = Text(window, height=12, width=42, font=12)
one = Entry(window, width=25, borderwidth=3, font=15)
two = Entry(window, width=25, borderwidth=3, font=12)
one_label = Label(window, text='方程1：', font=12)
two_label = Label(window, text='方程2：', font=12)
ans_label = Label(window, text='Answer', font=12)

def func():
    answer_fun.place(x=200, y=315)
    ans_label.place(x=200, y=285)
    one.place(x=270, y=220)
    two.place(x=270, y=255)
    one_label.place(x=200, y=218)
    two_label.place(x=200, y=253)
    play_f.place(x=548, y=236)
    del_f.place(x=510, y=585)

def play_func():
    var1 = one.get()
    var2 = two.get()
    ans_fun = solve_equation(var1, var2)
    answer_fun.intsert('insert', "方程组的解为："+"\n")
    answer_fun.intsert('insert', ans_fun)
    answer_fun.intsert('insert', "\n")

def del_func():
    answer_fun.place_forget()
    ans_label.place_forget()
    one.place_forget()
    two.place_forget()
    one_label.place_forget()
    two_label.place_forget()
    play_f.place_forget()
    del_f.place_forget()



# 求极限
lim1 = StringVar
lim2 = StringVar
limf = Entry(window, width=25, borderwidth=3, font=12)
lims = Entry(window, width=25, borderwidth=3, font=12)
limf_label = Label(window, text="函数", font=12)
lims_label = Label(window, text="趋向值：", font=12)
answer_lim = Text(window, height=12, width=42, font=12)

def lim():
    limf.place(x=275,y=220)
    lims.place(x=275,y=255)
    limf_label.place(x=200,y=218)
    lims_label.place(x=200,y=253)
    play_l.place(x=548,y=236)
    answer_lim.place(x=200,y=315)
    ans_label.place(x=200,y=285)
    del_l.place(x=510,y=585)


def play_lim():
    lim1 = limf.get()
    lim2 = lims.get()
    if lim2 == "oo":
        lim2 = "oo"
    else:
        lim2 = int(lim2)
    ans_lim = solve_limit(lim1, x, lim2)
    answer_lim.insert('insert', "函数的极限为：" + "\n")
    answer_lim.insert('insert', ans_lim)
    answer_lim.insert('insert', "\n")


def del_lim():
    limf.place_forget()
    lims.place_forget()
    limf_label.place_forget()
    lims_label.place_forget()
    answer_lim.place_forget()
    del_l.place_forget()
    play_l.place_forget()
    ans_label.place_forget()


# 求导数
d = StringVar
d_num = Entry(window, width=25, borderwidth=3, font=12)
d_num_label = Label(window, text="函数", font=12)
answer_der = Text(window,height=12, width=42, font=12)

def der():
    d_num.place(x=260, y=225)
    d_num_label.place(x=200, y=225)
    answer_der.place(x=200, y=315)
    ans_label.place(x=200, y=285)
    del_der.place(x=510, y=585)
    play_d.place(x=548, y=220)

def play_der():
    d = d_num.get()
    ans_d = solve_derivative(d, x)
    answer_der.insert('insert', "函数的导数为：" + "\n")
    answer_der.insert('insert', ans_d)
    answer_der.insert('insert', "\n")


def del_der():
    d_num.place_forget()
    d_num_label.place_forget()
    answer_der.place_forget()
    del_der.place_forget()
    play_d.place_forget()
    ans_label.place_forget()



# 求偏导
pder = StringVar
pd_num = Entry(window, width=25, borderwidth=3, font=12)
answer_pder = Text(window,height=12, width=42, font=12)

def pder():
    pd_num.place(x=260, y=255)
    d_num_label.place(x=200, y=225)
    answer_pder.place(x=200, y=315)
    ans_label.place(x=200, y=285)
    del_p.place(x=510, y=585)
    play_p.place(x=548, y=220)

def play_pder():
    p = pder.get()
    solve_derivative(p, x, y)

def del_pder():
    del_p.place_forget()
    ans_label.place_forget()
    answer_pder.place_forget()
    pd_num.place_forget()
    d_num_label.place_forget()
    play_p.place_forget()



# 定积分
ding1 = StringVar
ding2 = StringVar
ding3 = StringVar
ding_fun = Entry(window, width=25, borderwidth=3, font=12)
ding_up = Entry(window, width=6, borderwidth=3, font=12)
ding_down = Entry(window, width=6, borderwidth=3, font=12)
ding_label = Label(window, text="函数：", font=12)
ding_up_label = Label(window, text="上限", font=12)
ding_down_label = Label(window, text="下限", font=12)
answer_ding = Text(window, width=42, height=12, font=12)

def inte():
    ding_fun.place(x=260,y=210)
    ding_up.place(x=260,y=250)
    ding_down.place(x=450,y=250)
    answer_ding.place(x=200,y=315)
    ans_label.place(x=200, y=285)
    ding_label.place(x=200,y=210)
    ding_up_label.place(x=200,y=250)
    ding_down_label.place(x=380,y=250)
    del_i.place(x=510, y=585)
    play_i.place(x=548, y=223)


def play_inte():
    ding1 = ding_fun.get()
    ding2 = int(ding_up.get())
    ding3 = int(ding_down.get())
    ans_ding = solve_derivative(ding1, ding3, ding2)
    answer_ding.insert('insert', "定积分的结果为：" + "\n")
    answer_ding.insert('insert', ans_ding)
    answer_ding.insert('insert', "\n")

def del_inte():
    del_i.place_forget()
    play_i.place_forget()
    ans_label.place_forget()
    ding_fun.place_forget()
    ding_label.place_forget()
    ding_up.place_forget()
    ding_down.place_forget()
    answer_ding.place_forget()
    ding_up_label.place_forget()
    ding_down_label.place_forget()



# 不定积分
bud = StringVar
b = Entry(window, width=25, borderwidth=3, font=12)
b_label = Label(window, text="函数", font=12)
answer_b = Text(window, height=12, width=42, font=12)

def buding():
    b.place(x=260, y=225)
    b_label.place(x=200, y=225)
    answer_b.place(x=200, y=315)
    ans_label.place(x=200, y=285)
    del_b.place(x=510, y=585)
    play_b.place(x=548, y=220)

def play_buding():
    bud = b.get()
    ans_b = solve_derivative(bud, x)
    answer_b.insert('insert', "不定积分的结果为：" + "\n")
    answer_b.insert('insert', ans_b)
    answer_b.insert('insert', "\n")

def del_buding():
    del_b.place_forget()
    play_b.place_forget()
    ans_label.place_forget()
    b.place_forget()
    b_label.place_forget()
    answer_b.place_forget()



del_f = Button(window, text="点我换方法", font=12, command=del_func)
del_l = Button(window, text="点我换方法", font=12, command=del_lim)
del_der = Button(window, text="点我换方法", font=12, command=del_der)
del_p = Button(window, text="点我换方法", font=12, command=del_pder)
del_i = Button(window, text="点我换方法", font=12, command=del_inte)
del_b = Button(window, text="点我换方法", font=12, command=del_buding)

play_f = Button(window, text="点我计算", bd=1, font=("Microsoft YaHei", 12), activebackground='Light green', command=play_func)
play_l = Button(window, text="点我计算", bd=1, font=("Microsoft YaHei", 12), activebackground='Light green', command=play_lim)
play_d = Button(window, text="点我计算", bd=1, font=("Microsoft YaHei", 12), activebackground='Light green', command=play_der)
play_p = Button(window, text="点我计算", bd=1, font=("Microsoft YaHei", 12), activebackground='Light green', command=play_pder)
play_i = Button(window, text="点我计算", bd=1, font=("Microsoft YaHei", 12), activebackground='Light green', command=play_inte)
play_b = Button(window, text="点我计算", bd=1, font=("Microsoft YaHei", 12), activebackground='Light green', command=play_buding)


button_fun = Button(window, text="解方程", font=("Microsoft YaHei", 12), activebackground='Light green',
                       bg="#fc9d9a", command=func)
button_lim = Button(window, text="求极限", font=("Microsoft YaHei", 12), activebackground='Light green',
                       bg="#fc9d9a", command=lim)
button_der = Button(window, text="求导数", font=("Microsoft YaHei", 12), activebackground='Light green',
                       bg="#fc9d9a", command=der)
button_par = Button(window, text="求偏导", font=("Microsoft YaHei", 12), activebackground='Light green',
                       bg="#fc9d9a", command=pder)
button_itg = Button(window, text="求定积分", font=("Microsoft YaHei", 12), activebackground='Light green',
                       bg="#fc9d9a", command=inte)
button_bitg = Button(window, text="求不定积分", font=("Microsoft YaHei", 12), activebackground='Light green',
                        bg="#fc9d9a", command=buding)
hit()
window.mainloop()
