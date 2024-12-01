class Employee:
    def __init__(self, name, job):
        self.name = name
        self.job = job
        
    def get_info(self):
        return f"{self.name} = {self.job}"
    
    @staticmethod
    def isValid_job(job):
        validJob = ["Manager", "Cashier", "Cook", "Janitor"]
        return job in validJob
    

Employee.isValid_job("Manager") # Static Method

employ1 = Employee("Crab", 59)  # Instance method
employ2 = Employee("Pat", 23)   # Instance method