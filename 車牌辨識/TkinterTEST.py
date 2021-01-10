import tkinter as tk # 使用Tkinter前需要先导入
# 第1步，实例化object，建立窗口

window = tk.Tk() # 第2步，给窗口的可视化起名字
window.title('My Window') # 第3步，设定窗口的大小(长 * 宽)
window.geometry('500x300') # 这里的乘是小x
# 第4步，在图形界面上设定标签

var = tk.StringVar()    # 将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上

l = tk.Label(window, textvariable=var , bg='green', font=('Arial', 12), width=30, height=2)
# 说明： bg为背景，font为字体，width为长，height为高
# 这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高

# 第5步，放置标签
l.pack() # Label内容content区域放置位置，自动调节尺寸
# 放置lable的方法有：1）l.pack(); 2)l.place();
on_hit = False
def runMain():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me')

    else:
        on_hit = False
        var.set('')

b = tk.Button(window, text="run", font=('Arial',12), width=10, height=1, command=runMain)
b.pack()
# 第6步，主窗口循环显示
window.mainloop()
