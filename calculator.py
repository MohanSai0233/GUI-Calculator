from tkinter import *

cal = Tk()
cal.title("Calculator")
cal.geometry("425x362")
cal.resizable(False, False)
cal.configure(bg="#291717")
cal.iconphoto(False, PhotoImage(file="C:/Users/DELL/OneDrive/Documents/Desktop/vs_code/PYTHON/calculator_icon.png"))
 

def clear():
    display_box.delete(0, END)
    
def ClearALL():
    global first_number,math
    clear()
    first_number = ''
    math = ''
    return  
    
    
#clicked number insering function


def btn_clck(number):
    current_number=display_box.get()
    clear()
    display_box.insert(0, current_number + number)
    
first_number = 0
math = ''

def calculation(math_type):
    global first_number,math
    math = math_type
    first_number = display_box.get()
    clear()
    
def equal():
    global first_number, math
    try:
        
        second_number = display_box.get()
        clear()
        if second_number == '' or math == '':
            clear()
            display_box.insert(0, "Error: Invalid inputs")
        else:
            
            if  '.' not in first_number and '.' not in second_number:
                if math == 'add':
                    display_box.insert(0, str(int(first_number) + int(second_number)))
                elif math == 'sub':
                    display_box.insert(0, str(int(first_number) - int(second_number)))
                elif math == 'mul':
                    display_box.insert(0, str(int(first_number) * int(second_number)))
                elif math == 'div':
                    display_box.insert(0, str(int(first_number) / int(second_number)))
            else:   #'.' in first_number or '.' in second_number:
                if math == 'add':
                    display_box.insert(0, str(float(first_number) + float(second_number)))
                elif math == 'sub':
                   display_box.insert(0, str(float(first_number) - float(second_number)))
                elif math == 'mul':
                    display_box.insert(0, str(float(first_number) * float(second_number)))
                elif math == 'div':
                    display_box.insert(0, str(float(first_number) / float(second_number)))
                    
                    
        #display_box.insert(0, str(result))

    except ZeroDivisionError:
        clear()
        display_box.insert(0, "Error: Division by zero")
    except ValueError:
        clear()
        display_box.insert(0, "Error: Invalid value")
    except Exception as e:
        clear()
        display_box.insert(0, f"Error: {str(e)}") 
        

#Creating widgets
display_box = Entry(cal, width=31, font=('Arial',18), justify='right') # DIsplay box for input


btn_0= Button(cal, text='0',font=('Arial',14,'bold'),bg="#FFFFFF", padx=36, pady=10, command = lambda: btn_clck('0'))
btn_pont= Button(cal, text='.',font=('Arial',14,'bold'),bg="#FFFFFF", padx=38, pady=10, command = lambda: btn_clck('.'))
btn_1= Button(cal, text='1',font=('Arial',14,'bold'),bg="#FFFFFF", padx=36, pady=10, command = lambda: btn_clck('1'))
btn_2= Button(cal, text='2',font=('Arial',14,'bold'),bg="#FFFFFF", padx=36, pady=10, command = lambda: btn_clck('2'))
btn_3= Button(cal, text='3',font=('Arial',14,'bold'),bg="#FFFFFF", padx=36, pady=10, command = lambda: btn_clck('3'))

btn_4= Button(cal, text='4',font=('Arial',14,'bold'),bg="#FFFFFF", padx=36, pady=10, command = lambda: btn_clck('4'))
btn_5= Button(cal, text='5',font=('Arial',14,'bold'),bg="#FFFFFF", padx=36, pady=10, command = lambda: btn_clck('5'))
btn_6= Button(cal, text='6',font=('Arial',14,'bold'),bg="#FFFFFF", padx=36, pady=10, command = lambda: btn_clck('6'))

btn_7= Button(cal, text='7',font=('Arial',14,'bold'),bg="#FFFFFF", padx=36, pady=10, command = lambda: btn_clck('7'))
btn_8= Button(cal, text='8',font=('Arial',14,'bold'),bg="#FFFFFF", padx=36, pady=10, command = lambda: btn_clck('8'))
btn_9= Button(cal, text='9',font=('Arial',14,'bold'),bg="#FFFFFF", padx=36, pady=10, command = lambda: btn_clck('9'))
btn_add= Button(cal, text='+',font=('Arial',14,'bold'),bg="#FFFFFF", padx=37, pady=10, command = lambda: calculation('add'))
btn_sub= Button(cal, text='-',font=('Arial',14,'bold'),bg="#FFFFFF", padx=38, pady=10, command = lambda: calculation('sub'))
btn_mul= Button(cal, text='*',font=('Arial',14,'bold'),bg="#FFFFFF", padx=38, pady=10, command = lambda: calculation('mul'))
btn_div= Button(cal, text='/',font=('Arial',14,'bold'),bg="#FFFFFF", padx=38, pady=10, command = lambda: calculation('div'))
btn_eql= Button(cal, text='=',font=('Arial',14,'bold'),bg="#FFFFFF", padx=38, pady=40, command = equal)
btn_clc= Button(cal, text='clear',font=('Arial',17,'bold'), bg="#FFFFFF", padx=63, pady=10, command = clear)
btn_clc_all= Button(cal, text='CA',font=('Arial',16,'bold'), bg="#FFFFFF", padx=27, pady=10, command = ClearALL)


#Displaying widgets
display_box.grid(row=0, column=0,columnspan=4, padx=10, pady=10)
btn_0.grid(row=4, column=0, padx=2, pady=2)
btn_1.grid(row=3, column=0, padx=2, pady=2)
btn_2.grid(row=3, column=1, padx=2, pady=2)
btn_3.grid(row=3, column=2, padx=2, pady=2)

btn_4.grid(row=2, column=0, padx=2, pady=2)
btn_5.grid(row=2, column=1, padx=2, pady=2)
btn_6.grid(row=2, column=2, padx=2, pady=2)

btn_7.grid(row=1, column=0, padx=2, pady=2)
btn_8.grid(row=1, column=1, padx=2, pady=2)
btn_9.grid(row=1, column=2, padx=2, pady=2)

btn_add.grid(row=1, column=3, padx=2, pady=2)
btn_sub.grid(row=2, column=3, padx=2, pady=2)
btn_mul.grid(row=3, column=3, padx=2, pady=2)
btn_div.grid(row=4, column=2, padx=2, pady=2)
btn_eql.grid(row=4, column=3, rowspan=2, padx=4, pady=2)
btn_clc.grid(row=5, column=1, columnspan=2, padx=2, pady=2)



btn_clc_all.grid(row=5, column=0, padx=2, pady=2)


btn_pont.grid(row=4, column=1, padx=2, pady=2)



cal.mainloop()