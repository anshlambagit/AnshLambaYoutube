from firstClass import llms

class chatbot(llms):

    def __init__(self, model,query):
        self.model = model 
        llms.__init__(self,query)

    def showme(self):
        print("I am calling {self.model}.")
        llms.openai()

obj_inherit = chatbot("openai","Hey, I am Ansh Lamba")
print(obj_inherit.openai())
