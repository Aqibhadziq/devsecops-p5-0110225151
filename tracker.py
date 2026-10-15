# tracker.py
class FinanceTracker:
    def __init__(self):
        self.transactions = []

    def add_income(self, amount, description):
        """Menambah data pendapatan"""
        if amount <= 0:
            return False
        self.transactions.append({"type": "income", "amount": amount, "desc": description})
        return True

    def add_expense(self, amount, description):
        """Menambah data pengeluaran"""
        if amount <= 0:
            return False
        self.transactions.append({"type": "expense", "amount": amount, "desc": description})
        return True

    def get_summary(self):
        """Menghitung total pendapatan, pengeluaran, dan sisa saldo"""
        total_income = sum(t["amount"] for t in self.transactions if t["type"] == "income")
        total_expense = sum(t["amount"] for t in self.transactions if t["type"] == "expense")
        return {
            "total_income": total_income,
            "total_expense": total_expense,
            "balance": total_income - total_expense
        }