import tkinter 
import json 
class Register(tkinter.Tk):
    """ Register constructor 
    this is a child class of tkinter """
    def __init__(self):
        super().__init__()
        """ register attributes """
        self.title("Register app")
        self.geometry("800x600+620+200")
        self.resizable(width = False, height = False)

        # setting the background image on the window
        self.background_image = tkinter.PhotoImage(file = "new.png")
        self.background_label = tkinter.Label(self, image = self.background_image)
        self.background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

        # username
        self.username = tkinter.Text(height = 3, width = 47, font = ("times, 12"))
        self.username.insert("1.0", "Username")
        self.username.place(x = 247, y = 193)        
        # password
        self.password = tkinter.Text(height = 3, width = 47, font = ("times, 12"))
        self.password.insert("1.0", "Password")
        self.password.place(x = 247, y = 279)

        # email
        self.email = tkinter.Text(height = 3, width = 47, font = ("times, 12"))
        self.email.insert("1.0", "Email")
        self.email.place(x = 247, y = 365)

        # register_button
        self.register_button = tkinter.Button(text = "Register", command = self.save_data)
        self.register_button.place(x = 360, y = 493)

        # error_label
        self.error_message = ""


    def save_data(self):
        the_username = self.username.get("1.0", tkinter.END)
        the_username = the_username[0:-1]
        the_password =  self.password.get("1.0", tkinter.END)
        the_password = the_password[0:-1]
        the_email = self.email.get("1.0", tkinter.END)
        the_email = the_email[0:-1]

        if (len(the_username) != 0 and len(the_password) != 0 and len(the_email) != 0):
            if ("@" in the_email):
                pass 
            else:
                self.error_email_label = tkinter.Label(text = "Invalid Email address", bg = "#485065", fg = "orange",
                                                        font = ("times, 12"))
                self.error_email_label.place(x = 330, y = 550)
        else:
            self.error_filed_label = tkinter.Label(text = "please make sure you fill all the fields", bg  = "#485065",
                                                    fg = "orange", font = ("times, 12"))
            self.error_filed_label.place(x = 280, y = 550)


register = Register()

# run loop

register.mainloop()
        
