class BudgetManager: 
 def init(self): 
  self.income = 0.0 
  self.expenses = {}

 def add_income(self, amount):
    self.income += amount
    print(f"Income updated: ${self.income}")
    
 def add_expense(self, category, amount):
    if category in self.expenses:
        self.expenses[category] += amount
    else:
        self.expenses[category] = amount
    print(f"Added expense: {category} - ${amount}")
    
 def show_summary(self):
    total_expenses = sum(self.expenses.values())
    savings = self.income - total_expenses
    print("\n--- Budget Summary ---")
    print(f"Total Income: ${self.income}")
    print("Expenses:")
    for category, amount in self.expenses.items():
        print(f" {category}: ${amount}")
    print(f"Total Expenses: ${total_expenses}")
    print(f"Savings: ${savings}")

Example usage

budget = BudgetManager() 
budget.add_income(3000) 
budget.add_expense("Rent", 1200) 
budget.add_expense("Groceries", 300) 
budget.add_expense("Entertainment", 150) 
budget.show_summary()
