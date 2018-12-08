class Collector:
    #variables
    size = 128
    amount = 500
    name = "unlabeled_matrices"
    density = 0.2
    path = " "
    fetch = true


    def init(self, amount, name, size, density, path, fetch):
        self.size = size
        self.amount = amount
        self.name = name
        self.density = density
        self.path = path
        self.fetch = fetch

    def fetch(self):
        #fetches matrices from suite sparse
        #if the variable fetch is true it fetches as much matrices as possible
        # until the given amount is reached

    def generate(self):
        #generates artificial matrices