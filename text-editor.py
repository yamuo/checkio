import copy

class Text:
    
    def __init__(self):
        self.text = ""
        self.font = ""
        
    def write(self,text_str):
        self.text += text_str
    
    def set_font(self,font_str):
        self.font = font_str
    
    def show(self) :
        if self.font:
            return "[{}]{}[{}]".format(self.font,self.text,self.font)
        else:
            return self.text
    
    def restore(self,text_ins):
        self.text = text_ins.text
        self.font = text_ins.font
        
class SavedText:
    
    def __init__(self):
        self.version = []
        
    def save_text(self,text):
        self.version.append(copy.deepcopy(text))
        
    def get_version(self,code):
        return(self.version[code])
        
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    text = Text()
    saver = SavedText()
    
    text.write("At the very beginning ")
    saver.save_text(text)
    text.set_font("Arial")
    saver.save_text(text)
    text.write("there was nothing.")
    
    assert text.show() == "[Arial]At the very beginning there was nothing.[Arial]"
    
    text.restore(saver.get_version(0))
    assert text.show() == "At the very beginning "

    print("Coding complete? Let's try tests!")