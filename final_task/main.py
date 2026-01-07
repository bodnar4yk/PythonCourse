import json 
import pandas as pd
from matplotlib import pyplot as plt

class Expense:
    def __init__(self,description,amount,category):
        self.description=description
        self.amount=amount
        self.category=category

    def to_dict(self):
        return{"description":self.description,
               "amount":self.amount,
               "category":self.category
               }
    @classmethod
    def from_dict(cls,data:dict):
        return cls(description=data.get("description"),
                   amount=data.get("amount"),
                   category=data.get("category"))

class BudgetPlaner:
    JSON_FILE_NAME="BudgetPlaner.json"
    def __init__(self,start_income=0.0) -> None:
        self.income=start_income
        self.expences=[]
        self.load_data()

    def add_income(self,amount):
        self.income+=amount
        print(f"imcome_plus= {amount}")

    def add_expense(self,description,amount,category):
        new_expences=Expense(description,amount,category)
        self.expences.append(new_expences)

    def view_budget(self):
        total_expence=sum([expences.amount for expences in self.expences])
        balance=self.income-total_expence
        print("\n current budget:")
        print(f"\n General income: {self.income}")
        print(f"\n expence: {total_expence}")
        print(f"\n balance: {balance}\n")

    def save_data (self):
        data={
            "income": self.income,
            "expences": [expences.to_dict() for expences in self.expences]
        }
        with open(self.JSON_FILE_NAME,'w') as f:
            json.dump(data,f)
        print("save_data")

    def load_data(self):
        try:
            with open(self.JSON_FILE_NAME,'r') as f:
                data=json.load(f)
                self.income=data['income']
                self.expences=[Expense.from_dict(exp) for exp in data["expences"]]
                print("Upload data")
        except FileNotFoundError:
            print("Not exist file for load")
    
    def show_expense_analysis(self):
        """Show expense analysis using pie chart."""
        if not self.expences:
            print("Жодної витрати ще не створено.")
            return

        df = pd.DataFrame([exp.to_dict() for exp in self.expences])
        expences_by_category = df.groupby('category')['amount'].sum()

        # Plotting pie chart for expense categories
        plt.figure(figsize=(10, 6))
        expences_by_category.plot(kind='pie', autopct='%1.1f%%', startangle=140)
        plt.title('Витрати за категоріями')
        plt.ylabel('')  
        plt.show()

def main():
    planner=BudgetPlaner()

    while True:
        print(f"1. add expences")
        print(f"2. add income")
        print(f"3. show balance")
        print(f"4. Show analisis for group")
        print(f"5. exit")        
        user_input=input("Select act: ")
        if user_input=='1':
            category=input("type of category: \n ")
            try:
                amount=float(input('input sum\n'))
            except ValueError:
                print("Not correct type for amount")
                continue
            description=input("Input description expence\n")
            planner.add_expense(description,amount,category)
        elif user_input=='2':
            amount=float(input("sum income: \n"))
            planner.add_income(amount)
        elif user_input=='3':
            planner.view_budget()
        elif user_input=='4':
            planner.show_expense_analysis()
        elif user_input=='5':
            break

        planner.save_data()

if __name__=="__main__":
    main()

