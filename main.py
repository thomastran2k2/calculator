import tkinter as  tk

LIGHT_GRAY = "#F5F5F5"
class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("Calculator")
        self.buttons_frame = self.create_buttons_frame()
        self.display_frame = self.create_display_frame()
    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text = self.total_expression, anchor=tk.E)

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


