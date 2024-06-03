from tkinter import *
from googletrans import Translator,LANGUAGES
from tkinter import ttk
import pyttsx3
windows=Tk()        #create a window
windows.geometry('600x500')
windows.title('Language Translater ')
windows.config(bg='#5EB1FE')


#user define function

def translate():
    t1=Translator()
    result=t1.translate(text=Input_text.get(1.0,END),src=ip_lang.get(),dest=op_lang.get())
    #print(result)
    Output_text.delete(1.0,END)
    if result.pronunciation==None:
        Output_text.insert(END,result.text+'.\n')

    else:
        Output_text.insert(END,result.text+'.\n')
        Output_text.insert(END,result.pronunciation)

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# declare components position 
# Labels
Label(windows,text='Language Translator',font='Times_new_roman 15 bold',bg='#C0C0C0').place(x=175,y=25)#pack()
Label(windows,text='Input language',font='Times_new_roman 15 bold',bg='#C0C0C0').place(x=60,y=100)
Label(windows,text='Output Language',font='Times_new_roman 15 bold',bg='#C0C0C0').place(x=350,y=100)

lang_list=list(LANGUAGES.values())
print(lang_list)

# Input Language Drop List
ip_lang=ttk.Combobox(windows,values=lang_list,height=12,width=15)
ip_lang.place(x=80,y=70)

# Input text box decleration, position
Input_text=Text(windows,font='Times_new_roman 10',height=12,wrap=WORD,padx=15,pady=15,width=30)
Input_text.place(x=30,y=150)

# Output Language rop List
op_lang=ttk.Combobox(windows,values=lang_list,height=12,width=15)
op_lang.place(x=370,y=70)

# Output text box decleration, position
Output_text=Text(windows,font='Times_new_roman 10',height=12,wrap=WORD,padx=15,pady=15,width=30)
Output_text.place(x=325,y=150)

# Translate Button Declared
Button(windows,text='Translate',font='Times_new_roman 15 bold',width='15',command=translate).place(x=175,y=400)



# Loud Button Declared
Button(windows,text='Loud',font='Times_new_roman 15 bold',width='5',command=lambda: speak(Output_text.get("1.0",END))).place(x=250,y=450)

windows.mainloop()  #looping for continues running till box closed
