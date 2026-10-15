# app.py
from tracker import FinanceTracker
from utils import format_rupiah, print_header

def main():
    print_header("APLIKASI TABUNGIN - CATATAN KEUANGAN PRIBADI")
    
    tracker = FinanceTracker()
    
    # Tambah Pemasukan & Pengeluaran
    tracker.add_income(5000000, "Gaji Bulanan")
    tracker.add_expense(150000, "Beli Makan Siang")
    tracker.add_expense(50000, "Bensin")
    
    # Tampilkan Ringkasan Keuangan
    summary = tracker.get_summary()
    print(f"Total Pendapatan : {format_rupiah(summary['total_income'])}")
    print(f"Total Pengeluaran: {format_rupiah(summary['total_expense'])}")
    print(f"Sisa Tabungan    : {format_rupiah(summary['balance'])}")

if __name__ == "__main__":
    main()