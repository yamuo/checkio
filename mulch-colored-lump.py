class Lamp:
    colors = ["Green","Red","Blue","Yellow"]
    color = 3
    ret_color = colors[1]

    def light(self):
        try:
            self.color += 1
            self.ret_color = self.colors[self.color]
        except:
            self.color = 0
            self.ret_color = self.colors[self.color]
        
        return self.ret_color
