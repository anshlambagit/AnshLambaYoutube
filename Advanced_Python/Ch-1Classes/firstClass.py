class llms:

    token_size = 100

    def __init__(self,query):
        self.query = query

    def openai(self):
        print(f"I am openai. You asked {self.query}") 

    def claude(self):
        print("I am claude")

    def llama(self):
        print("I am llama")


if __name__ == "__main__":
    
    obj = llms("Ansh is Ansh")
    print(obj.openai())