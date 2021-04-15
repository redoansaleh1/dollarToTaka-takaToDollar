from tkinter import *;


def main():
    global root;
    root = Tk();
    root.title("dollar to taka and taka to dollar");
    root.config(bg='#fFFffF');
    root.geometry("685x400"); 
    
    
    global amountOfDollarOrTaka; 
    amountOfDollarOrTaka = Entry(root, width=6);
    amountOfDollarOrTaka.place(x=10, y=10);
    
    
    global userWantToConvertDollarToTakaOrTakaToDollar;
    userWantToConvertDollarToTakaOrTakaToDollar = IntVar();
    userWantToConvertDollarToTakaOrTakaToDollar.set(1);
    
    
    userWantToConvertDollarToTakaRadioButton = Radiobutton(root, variable=userWantToConvertDollarToTakaOrTakaToDollar, value=1, text='Dollar To Taka', bg='#fFFffF', activebackground='#fFFffF');
    userWantToConvertDollarToTakaRadioButton.place(x=280,y=10);
    
    
    userWantToConvertTakaToDollarRadioButton = Radiobutton(root, variable=userWantToConvertDollarToTakaOrTakaToDollar, value=2, text='Taka To Dollar', bg='#fFFffF', activebackground='#fFFffF');
    userWantToConvertTakaToDollarRadioButton.place(x=280,y=80);
    
    
    getAmountOfTakaButton = Button(root, text='Get amount of taka or dollar', command=getAmountOfTaka, bg='#fFFffF', highlightcolor='#fFFffF', activebackground='#fFFffF');
    getAmountOfTakaButton.place(x=10, y=180);
    
    
    global amountOfTakaOrDollarLabel;
    amountOfTakaOrDollarLabel = Label(root, bg='#fFFffF');
    
    
    root.mainloop();

    
def getAmountOfTaka():
    try:
        if userWantToConvertDollarToTakaOrTakaToDollar.get() == 1:
            taka = float(amountOfDollarOrTaka.get())*84.74;
            amountOfTakaOrDollarLabel['text'] = '%0.2f'%taka;
            amountOfTakaOrDollarLabel.place(x=10, y=80);    
        else:
            dollar = float(amountOfDollarOrTaka.get())/84.74;
            amountOfTakaOrDollarLabel['text'] = '%0.2f'%dollar;
            amountOfTakaOrDollarLabel.place(x=10, y=80);    
    except Exception as e:    
        amountOfTakaOrDollarLabel['text'] = 'Invalid input!';
        amountOfTakaOrDollarLabel.place(x=10, y=80);   
        print(e) 

        
if __name__ == '__main__':
    main();     