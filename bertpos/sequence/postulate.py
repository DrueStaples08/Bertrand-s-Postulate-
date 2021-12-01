# As long as n > 3 then there will always be a prime number between 
# n and 2n-2

class Bertrand:
    
    def __init__(self):
        pass

    def run(n):
        return [i for i in range(n+1, 2*n-2) if i % 2 != 0]



