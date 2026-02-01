#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Demo script untuk menunjukkan cara penggunaan Symbolab
Script ini mensimulasikan input user untuk demonstrasi
"""

import sys
from io import StringIO

# Simulasi beberapa contoh penggunaan
demo_sessions = [
    {
        "title": "DEMO 1: ALJABAR - Faktorisasi",
        "inputs": [
            "1",      # Menu Aljabar
            "2",      # Faktorisasi
            "x^2 - 4",  # Ekspresi
            "",       # Continue
            "0"       # Exit
        ]
    },
    {
        "title": "DEMO 2: TURUNAN",
        "inputs": [
            "3",      # Menu Turunan
            "x^3 + 2*x^2 + x",  # Fungsi
            "x",      # Variabel
            "1",      # Orde 1
            "",       # Continue
            "0"       # Exit
        ]
    },
    {
        "title": "DEMO 3: INTEGRAL TAK TENTU",
        "inputs": [
            "4",      # Menu Integral
            "1",      # Tak tentu
            "x^2 + 2*x",  # Fungsi
            "x",      # Variabel
            "",       # Continue
            "0"       # Exit
        ]
    },
    {
        "title": "DEMO 4: LIMIT",
        "inputs": [
            "5",      # Menu Limit
            "sin(x)/x",  # Fungsi
            "x",      # Variabel
            "0",      # Menuju 0
            "",       # Kedua sisi
            "",       # Continue
            "0"       # Exit
        ]
    },
    {
        "title": "DEMO 5: TRIGONOMETRI",
        "inputs": [
            "2",      # Menu Trigonometri
            "1",      # Sederhanakan
            "sin(x)^2 + cos(x)^2",  # Ekspresi
            "",       # Continue
            "0"       # Exit
        ]
    }
]

def run_demo(title, inputs):
    """Jalankan satu sesi demo"""
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70)
    
    # Simpan stdin asli
    old_stdin = sys.stdin
    
    # Buat input stream dari list
    input_stream = StringIO('\n'.join(inputs))
    sys.stdin = input_stream
    
    # Import dan jalankan Symbolab
    from symbolab import Symbolab
    app = Symbolab()
    
    try:
        app.run()
    except (EOFError, KeyboardInterrupt):
        pass
    finally:
        # Kembalikan stdin
        sys.stdin = old_stdin
    
    print()

if __name__ == "__main__":
    print("\n" + "="*70)
    print("  SYMBOLAB - DEMONSTRASI PENGGUNAAN")
    print("="*70)
    print("\nBerikut adalah beberapa contoh penggunaan Symbolab:")
    print("Program akan menampilkan output dari berbagai operasi matematika.\n")
    input("Tekan Enter untuk memulai demonstrasi...")
    
    for demo in demo_sessions:
        run_demo(demo["title"], demo["inputs"])
        print("\n" + "-"*70)
        input("Tekan Enter untuk lanjut ke demo berikutnya...")
    
    print("\n" + "="*70)
    print("  DEMONSTRASI SELESAI")
    print("="*70)
    print("\nUntuk menggunakan Symbolab secara interaktif, jalankan:")
    print("  python symbolab.py")
    print("\nSelamat belajar matematika! 🎓\n")
