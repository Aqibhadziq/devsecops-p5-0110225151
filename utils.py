# utils.py
def format_rupiah(amount):
    """Format angka menjadi format mata uang Rupiah"""
    return f"Rp {amount:,.0f}".replace(",", ".")

def print_header(title):
    """Mencetak header tampilan garis dekoratif"""
    print("=" * 45)
    print(title.center(45))
    print("=" * 45)