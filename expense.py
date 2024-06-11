class Expense:

   def __init__(self, name, category, amount) -> None:
        """defines expense class for tracker with name category and amount"""
        self.name = name
        self.category = category
        self.amount = amount

   def __repr__(self): #returns a string of the expense output instead of expense object mumbo jumbo
      return f"<Expense: {self.name}, {self.category}, ${self.amount:.2f}>"