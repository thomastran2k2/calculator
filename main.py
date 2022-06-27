import tkinter as  tk

LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"
SMALL_FONT_SIZE = ("Arial", 16)
BIG_FONT_SIZE = ("Arial", 40, "bold ")
class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("Calculator")
        self.current_expression = "0"
        self.total_expression = "0"
        self.display_frame = self.create_display_frame()
        self.total_label, self.label = self.create_display_labels()

        self.buttons_frame = self.create_buttons_frame()

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text = self.total_expression, anchor=tk.E, bg = LIGHT_GRAY, fg= LABEL_COLOR, padx = 24, font = SMALL_FONT_SIZE)
        total_label.pack(expand =True, fill = "both")
        label = tk.Label(self.display_frame, text = self.current_expression, anchor = tk.E, bg =LIGHT_GRAY, fg = LABEL_COLOR, padx = 24, font = BIG_FONT_SIZE)
        label.pack(expand = True, fill = "both")

        return total_label, label



    def create_display_frame(self):
        frame = tk.Frame(self.window, height = 221, bg = LIGHT_GRAY)
        frame.pack(expand = True, fill = "both")
        return frame
    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand = True, fill = "both")
        return frame
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()


