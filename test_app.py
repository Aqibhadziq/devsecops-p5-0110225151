# test_app.py
import unittest
from tracker import FinanceTracker
from utils import format_rupiah

class TestTabungIN(unittest.TestCase):

    def setUp(self):
        self.tracker = FinanceTracker()

    def test_add_income_and_expense(self):
        self.assertTrue(self.tracker.add_income(100000, "Uang Saku"))
        self.assertTrue(self.tracker.add_expense(30000, "Makan"))

    def test_get_summary(self):
        self.tracker.add_income(500000, "Gaji")
        self.tracker.add_expense(200000, "Belanja")
        summary = self.tracker.get_summary()
        
        self.assertEqual(summary["total_income"], 500000)
        self.assertEqual(summary["total_expense"], 200000)
        self.assertEqual(summary["balance"], 300000)

    def test_format_rupiah(self):
        self.assertEqual(format_rupiah(50000), "Rp 50.000")

if __name__ == "__main__":
    unittest.main()