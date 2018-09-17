import time

VOWELS = "aeiouAEIOU"

class Chat:
    def __init__(self):
        self.dialogue = ""
        self.human = None
        self.robot = None
    
    def connect_human(self,human_ins):
        self.human = human_ins
    
    def connect_robot(self,robot_ins):
        self.robot = robot_ins
        

        
    def show_human_dialogue(self):
        self.human_dialogue = sorted(self.human.h_list + self.robot.r_list)
        ret = ""
        
        for i,v in enumerate(self.human_dialogue):
            ret += "{0} said: {1}\n".format(v[1],v[2])
        
        return ret[:-1]
        
    def show_robot_dialogue(self):
        self.robot_dialogue = sorted(self.human.h_list + self.robot.r_list)
        ret = ""
        
        for i,v in enumerate(self.robot_dialogue):
            ret += "{0} said: {1}\n".format(v[1],self.change_robot(v[2]))
        
        return ret[:-1]
        
    def change_robot(self,text):
        ret = ""
        
        for i in text:
            if VOWELS.find(i) != -1:
                ret += "0"
            else:
                ret += "1"
                
        return ret

class Human:
    
    def __init__(self, text):
        self.h_list = []
        self.name = ""
        self.name = text
    
    def send(self,message):
        self.h_list.append([time.time(),self.name,message])    
        
class Robot:
    
    def __init__(self, text):
        self.r_list = []
        self.name = ""
        self.name = text
    
    def send(self,message):
        self.r_list.append([time.time(),self.name,message])


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    chat = Chat()
    karl = Human("Karl")
    bot = Robot("R2D2")
    chat.connect_human(karl)
    chat.connect_robot(bot)
    karl.send("Hi! What's new?")
    bot.send("Hello, human. Could we speak later about it?")
    print(chat.show_human_dialogue())
    print(chat.show_robot_dialogue())


    
    """
        assert chat.show_human_dialogue() == "Karl said: Hi! What's new?
R2D2 said: Hello, human. Could we speak later about it?"
    assert chat.show_robot_dialogue() == "Karl said: 101111011111011
R2D2 said: 10110111010111100111101110011101011010011011"

    print("Coding complete? Let's try tests!")
"""