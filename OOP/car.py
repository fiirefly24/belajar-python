class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
        
    def drive(self):
        return print(f"Get in! Start our {self.model}")
    
    def stop(self):
        print("Step the brake!")