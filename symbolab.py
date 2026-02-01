#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Symbolab - AI Math Solver untuk Mahasiswa dan Pelajar Indonesia
Mendukung: Aljabar, Trigonometri, Kalkulus, Integral, Turunan, Limit, Matriks, dan Persamaan Diferensial
"""

import sys
from sympy import *
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application
import re

# Konfigurasi SymPy untuk output yang lebih baik
init_printing(use_unicode=True)

class Symbolab:
    def __init__(self):
        self.x, self.y, self.z, self.t = symbols('x y z t')
        self.history = []
        
    def tampilkan_menu(self):
        """Menampilkan menu utama"""
        print("\n" + "="*60)
        print("    SYMBOLAB - AI MATH SOLVER UNTUK INDONESIA")
        print("="*60)
        print("\nPilih jenis operasi matematika:")
        print("1. Aljabar (persamaan, penyederhanaan, faktorisasi)")
        print("2. Trigonometri (sin, cos, tan, simplifikasi)")
        print("3. Turunan/Derivative (dy/dx)")
        print("4. Integral (∫)")
        print("5. Limit (lim)")
        print("6. Matriks (determinan, inverse, eigenvalue)")
        print("7. Persamaan Diferensial")
        print("8. Lihat Riwayat")
        print("9. Bantuan")
        print("0. Keluar")
        print("="*60)
        
    def parse_expression(self, expr_str):
        """Parse string menjadi ekspresi SymPy"""
        try:
            # Ganti ^ dengan ** untuk pangkat
            expr_str = expr_str.replace('^', '**')
            
            transformations = standard_transformations + (implicit_multiplication_application,)
            expr = parse_expr(expr_str, transformations=transformations, 
                            local_dict={'x': self.x, 'y': self.y, 'z': self.z, 't': self.t})
            return expr
        except Exception as e:
            print(f"Error parsing ekspresi: {e}")
            return None
    
    def aljabar(self):
        """Operasi aljabar"""
        print("\n--- ALJABAR ---")
        print("1. Sederhanakan ekspresi")
        print("2. Faktorisasi")
        print("3. Expand/Ekspansi")
        print("4. Selesaikan persamaan")
        
        pilihan = input("\nPilih operasi (1-4): ").strip()
        
        if pilihan == '1':
            expr_str = input("Masukkan ekspresi (contoh: (x+1)^2 - x^2): ")
            expr = self.parse_expression(expr_str)
            if expr:
                result = simplify(expr)
                print(f"\nHasil: {result}")
                self.history.append(f"Simplify: {expr} = {result}")
                
        elif pilihan == '2':
            expr_str = input("Masukkan ekspresi (contoh: x^2 - 4): ")
            expr = self.parse_expression(expr_str)
            if expr:
                result = factor(expr)
                print(f"\nHasil faktorisasi: {result}")
                self.history.append(f"Factor: {expr} = {result}")
                
        elif pilihan == '3':
            expr_str = input("Masukkan ekspresi (contoh: (x+1)*(x-1)): ")
            expr = self.parse_expression(expr_str)
            if expr:
                result = expand(expr)
                print(f"\nHasil ekspansi: {result}")
                self.history.append(f"Expand: {expr} = {result}")
                
        elif pilihan == '4':
            expr_str = input("Masukkan persamaan (contoh: x^2 - 4 = 0, cukup tulis x^2 - 4): ")
            expr = self.parse_expression(expr_str)
            if expr:
                var = input("Selesaikan untuk variabel (default: x): ").strip() or 'x'
                var_symbol = symbols(var)
                try:
                    result = solve(expr, var_symbol)
                    print(f"\nSolusi: {var} = {result}")
                    self.history.append(f"Solve {expr} = 0: {var} = {result}")
                except Exception as e:
                    print(f"Error: {e}")
    
    def trigonometri(self):
        """Operasi trigonometri"""
        print("\n--- TRIGONOMETRI ---")
        print("1. Sederhanakan ekspresi trigonometri")
        print("2. Hitung nilai trigonometri")
        print("3. Ubah ke bentuk lain")
        
        pilihan = input("\nPilih operasi (1-3): ").strip()
        
        if pilihan == '1':
            expr_str = input("Masukkan ekspresi (contoh: sin(x)^2 + cos(x)^2): ")
            expr = self.parse_expression(expr_str)
            if expr:
                result = trigsimp(expr)
                print(f"\nHasil: {result}")
                self.history.append(f"Trigsimp: {expr} = {result}")
                
        elif pilihan == '2':
            func = input("Fungsi (sin/cos/tan): ").strip().lower()
            nilai = input("Nilai (contoh: pi/4, 30*pi/180): ")
            try:
                angle = self.parse_expression(nilai)
                if func == 'sin':
                    result = sin(angle)
                elif func == 'cos':
                    result = cos(angle)
                elif func == 'tan':
                    result = tan(angle)
                else:
                    print("Fungsi tidak dikenal")
                    return
                print(f"\n{func}({angle}) = {result} = {float(result.evalf())}")
                self.history.append(f"{func}({angle}) = {result}")
            except Exception as e:
                print(f"Error: {e}")
                
        elif pilihan == '3':
            expr_str = input("Masukkan ekspresi: ")
            expr = self.parse_expression(expr_str)
            if expr:
                result = expand_trig(expr)
                print(f"\nHasil ekspansi: {result}")
                self.history.append(f"Expand trig: {expr} = {result}")
    
    def turunan(self):
        """Menghitung turunan/derivative"""
        print("\n--- TURUNAN/DERIVATIVE ---")
        expr_str = input("Masukkan fungsi (contoh: x^3 + 2*x^2 + x): ")
        expr = self.parse_expression(expr_str)
        
        if expr:
            var = input("Turunan terhadap variabel (default: x): ").strip() or 'x'
            var_symbol = symbols(var)
            
            order = input("Orde turunan (1 untuk turunan pertama, 2 untuk kedua, dst): ").strip() or '1'
            try:
                order = int(order)
                result = diff(expr, var_symbol, order)
                
                if order == 1:
                    print(f"\ndy/d{var} = {result}")
                else:
                    print(f"\nd^{order}y/d{var}^{order} = {result}")
                    
                self.history.append(f"d^{order}/d{var}^{order}({expr}) = {result}")
            except Exception as e:
                print(f"Error: {e}")
    
    def integral(self):
        """Menghitung integral"""
        print("\n--- INTEGRAL ---")
        print("1. Integral tak tentu")
        print("2. Integral tentu")
        
        pilihan = input("\nPilih jenis (1-2): ").strip()
        
        expr_str = input("Masukkan fungsi (contoh: x^2 + 2*x): ")
        expr = self.parse_expression(expr_str)
        
        if expr:
            var = input("Integralkan terhadap variabel (default: x): ").strip() or 'x'
            var_symbol = symbols(var)
            
            try:
                if pilihan == '1':
                    result = integrate(expr, var_symbol)
                    print(f"\n∫({expr}) d{var} = {result} + C")
                    self.history.append(f"∫({expr}) d{var} = {result} + C")
                    
                elif pilihan == '2':
                    batas_bawah = input("Batas bawah: ")
                    batas_atas = input("Batas atas: ")
                    
                    bb = self.parse_expression(batas_bawah)
                    ba = self.parse_expression(batas_atas)
                    
                    result = integrate(expr, (var_symbol, bb, ba))
                    print(f"\n∫[{bb} to {ba}] ({expr}) d{var} = {result}")
                    print(f"Nilai numerik: {float(result.evalf())}")
                    self.history.append(f"∫[{bb},{ba}] ({expr}) d{var} = {result}")
                    
            except Exception as e:
                print(f"Error: {e}")
    
    def limit_func(self):
        """Menghitung limit"""
        print("\n--- LIMIT ---")
        expr_str = input("Masukkan fungsi (contoh: sin(x)/x): ")
        expr = self.parse_expression(expr_str)
        
        if expr:
            var = input("Variabel (default: x): ").strip() or 'x'
            var_symbol = symbols(var)
            
            point = input("Limit menuju (contoh: 0, oo untuk infinity): ")
            if point.lower() == 'oo' or point.lower() == 'infinity':
                point_val = oo
            else:
                point_val = self.parse_expression(point)
            
            direction = input("Arah (+ untuk kanan, - untuk kiri, enter untuk kedua sisi): ").strip()
            
            try:
                if direction == '+':
                    result = limit(expr, var_symbol, point_val, '+')
                elif direction == '-':
                    result = limit(expr, var_symbol, point_val, '-')
                else:
                    result = limit(expr, var_symbol, point_val)
                
                print(f"\nlim ({var} → {point_val}) {expr} = {result}")
                self.history.append(f"lim ({var} → {point_val}) {expr} = {result}")
                
            except Exception as e:
                print(f"Error: {e}")
    
    def matriks(self):
        """Operasi matriks"""
        print("\n--- MATRIKS ---")
        print("1. Determinan")
        print("2. Inverse")
        print("3. Eigenvalue dan Eigenvector")
        print("4. Transpose")
        print("5. Perkalian matriks")
        
        pilihan = input("\nPilih operasi (1-5): ").strip()
        
        if pilihan in ['1', '2', '3', '4']:
            print("\nMasukkan elemen matriks baris per baris")
            print("Contoh untuk matriks 2x2: ")
            print("  Baris 1: 1, 2")
            print("  Baris 2: 3, 4")
            
            try:
                rows = int(input("\nJumlah baris: "))
                cols = int(input("Jumlah kolom: "))
                
                matrix_data = []
                for i in range(rows):
                    row_str = input(f"Baris {i+1} (pisahkan dengan koma): ")
                    row = [parse_expr(x.strip()) for x in row_str.split(',')]
                    matrix_data.append(row)
                
                M = Matrix(matrix_data)
                print(f"\nMatriks Anda:\n{M}")
                
                if pilihan == '1':
                    det = M.det()
                    print(f"\nDeterminan = {det}")
                    self.history.append(f"det(M) = {det}")
                    
                elif pilihan == '2':
                    inv = M.inv()
                    print(f"\nInverse:\n{inv}")
                    self.history.append(f"M^(-1) calculated")
                    
                elif pilihan == '3':
                    eigenvals = M.eigenvals()
                    eigenvects = M.eigenvects()
                    print(f"\nEigenvalues: {eigenvals}")
                    print(f"\nEigenvectors:")
                    for val, mult, vects in eigenvects:
                        print(f"  λ = {val}, multiplicity = {mult}")
                        for v in vects:
                            print(f"    v = {v}")
                    self.history.append(f"Eigenvalues: {eigenvals}")
                    
                elif pilihan == '4':
                    trans = M.T
                    print(f"\nTranspose:\n{trans}")
                    self.history.append(f"M^T calculated")
                    
            except Exception as e:
                print(f"Error: {e}")
                
        elif pilihan == '5':
            print("\nPerkalian Matriks A × B")
            try:
                # Matriks A
                rows_a = int(input("\nMatriks A - Jumlah baris: "))
                cols_a = int(input("Matriks A - Jumlah kolom: "))
                
                matrix_a = []
                for i in range(rows_a):
                    row_str = input(f"A Baris {i+1}: ")
                    row = [parse_expr(x.strip()) for x in row_str.split(',')]
                    matrix_a.append(row)
                
                # Matriks B
                rows_b = int(input("\nMatriks B - Jumlah baris: "))
                cols_b = int(input("Matriks B - Jumlah kolom: "))
                
                matrix_b = []
                for i in range(rows_b):
                    row_str = input(f"B Baris {i+1}: ")
                    row = [parse_expr(x.strip()) for x in row_str.split(',')]
                    matrix_b.append(row)
                
                A = Matrix(matrix_a)
                B = Matrix(matrix_b)
                
                result = A * B
                print(f"\nA × B =\n{result}")
                self.history.append(f"Matrix multiplication performed")
                
            except Exception as e:
                print(f"Error: {e}")
    
    def persamaan_diferensial(self):
        """Menyelesaikan persamaan diferensial"""
        print("\n--- PERSAMAAN DIFERENSIAL ---")
        print("Contoh input: Eq(f(x).diff(x), f(x))")
        print("Untuk y' = y, masukkan: f(x).diff(x) - f(x)")
        
        expr_str = input("\nMasukkan persamaan diferensial: ")
        
        try:
            f = Function('f')
            local_dict = {'x': self.x, 'y': self.y, 't': self.t, 'f': f, 'Derivative': Derivative}
            
            # Parse menggunakan sympify
            eq = sympify(expr_str, locals=local_dict)
            
            # Coba selesaikan
            result = dsolve(eq, f(self.x))
            print(f"\nSolusi: {result}")
            self.history.append(f"dsolve: {result}")
            
        except Exception as e:
            print(f"Error: {e}")
            print("\nTips: Gunakan f(x) untuk fungsi, f(x).diff(x) untuk turunan")
    
    def lihat_riwayat(self):
        """Menampilkan riwayat perhitungan"""
        print("\n--- RIWAYAT PERHITUNGAN ---")
        if not self.history:
            print("Belum ada perhitungan")
        else:
            for i, item in enumerate(self.history, 1):
                print(f"{i}. {item}")
    
    def bantuan(self):
        """Menampilkan bantuan"""
        print("\n" + "="*60)
        print("                    BANTUAN SYMBOLAB")
        print("="*60)
        print("\nCONTOH PENGGUNAAN:")
        print("\n1. ALJABAR:")
        print("   - Sederhanakan: (x+1)^2 - x^2")
        print("   - Faktorisasi: x^2 - 4")
        print("   - Selesaikan: x^2 - 5*x + 6")
        print("\n2. TRIGONOMETRI:")
        print("   - sin(x)^2 + cos(x)^2")
        print("   - tan(pi/4)")
        print("\n3. TURUNAN:")
        print("   - x^3 + 2*x^2 + x")
        print("   - sin(x)*cos(x)")
        print("\n4. INTEGRAL:")
        print("   - x^2 + 2*x")
        print("   - sin(x)")
        print("\n5. LIMIT:")
        print("   - sin(x)/x menuju 0")
        print("   - (x^2 - 1)/(x - 1) menuju 1")
        print("\n6. MATRIKS:")
        print("   - Masukkan elemen per baris")
        print("   - Contoh 2x2: 1,2 lalu 3,4")
        print("\n7. DIFERENSIAL:")
        print("   - f(x).diff(x) - f(x)  (untuk y' = y)")
        print("\nCATATAN:")
        print("   - Gunakan * untuk perkalian: 2*x bukan 2x")
        print("   - Gunakan ^ atau ** untuk pangkat: x^2 atau x**2")
        print("   - Gunakan pi untuk π")
        print("   - Gunakan oo untuk infinity (∞)")
        print("="*60)
    
    def run(self):
        """Jalankan program utama"""
        print("\nSelamat datang di SYMBOLAB!")
        print("Program pembantu matematika untuk pelajar Indonesia")
        
        while True:
            try:
                self.tampilkan_menu()
                pilihan = input("\nPilih menu (0-9): ").strip()
                
                if pilihan == '0':
                    print("\nTerima kasih telah menggunakan Symbolab!")
                    print("Semangat belajar matematika! 🎓")
                    break
                elif pilihan == '1':
                    self.aljabar()
                elif pilihan == '2':
                    self.trigonometri()
                elif pilihan == '3':
                    self.turunan()
                elif pilihan == '4':
                    self.integral()
                elif pilihan == '5':
                    self.limit_func()
                elif pilihan == '6':
                    self.matriks()
                elif pilihan == '7':
                    self.persamaan_diferensial()
                elif pilihan == '8':
                    self.lihat_riwayat()
                elif pilihan == '9':
                    self.bantuan()
                else:
                    print("\nPilihan tidak valid!")
                    
                input("\nTekan Enter untuk melanjutkan...")
                
            except KeyboardInterrupt:
                print("\n\nProgram dihentikan oleh user.")
                break
            except Exception as e:
                print(f"\nTerjadi error: {e}")
                input("\nTekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    app = Symbolab()
    app.run()
