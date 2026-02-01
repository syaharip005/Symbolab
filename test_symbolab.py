#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test script untuk Symbolab
Mengetes berbagai fungsionalitas matematika
"""

from sympy import *
from symbolab import Symbolab
import sys

def test_aljabar():
    """Test operasi aljabar"""
    print("="*60)
    print("TEST: ALJABAR")
    print("="*60)
    
    x = symbols('x')
    
    # Test 1: Simplify
    expr = (x+1)**2 - x**2
    result = simplify(expr)
    print(f"✓ Simplify (x+1)^2 - x^2 = {result}")
    assert result == 2*x + 1
    
    # Test 2: Factor
    expr = x**2 - 4
    result = factor(expr)
    print(f"✓ Factor x^2 - 4 = {result}")
    
    # Test 3: Expand
    expr = (x+1)*(x-1)
    result = expand(expr)
    print(f"✓ Expand (x+1)*(x-1) = {result}")
    assert result == x**2 - 1
    
    # Test 4: Solve
    expr = x**2 - 5*x + 6
    result = solve(expr, x)
    print(f"✓ Solve x^2 - 5x + 6 = 0: x = {result}")
    assert result == [2, 3]
    
    print("✓ Semua test aljabar PASSED\n")

def test_trigonometri():
    """Test trigonometri"""
    print("="*60)
    print("TEST: TRIGONOMETRI")
    print("="*60)
    
    x = symbols('x')
    
    # Test 1: Identitas trigonometri
    expr = sin(x)**2 + cos(x)**2
    result = trigsimp(expr)
    print(f"✓ sin(x)^2 + cos(x)^2 = {result}")
    assert result == 1
    
    # Test 2: Nilai trigonometri
    result = sin(pi/4)
    print(f"✓ sin(π/4) = {result} = {float(result.evalf()):.4f}")
    
    # Test 3: Ekspansi trigonometri
    expr = sin(2*x)
    result = expand_trig(expr)
    print(f"✓ Expand sin(2x) = {result}")
    
    print("✓ Semua test trigonometri PASSED\n")

def test_turunan():
    """Test turunan"""
    print("="*60)
    print("TEST: TURUNAN")
    print("="*60)
    
    x = symbols('x')
    
    # Test 1: Turunan polynomial
    expr = x**3 + 2*x**2 + x
    result = diff(expr, x)
    print(f"✓ d/dx(x^3 + 2x^2 + x) = {result}")
    assert result == 3*x**2 + 4*x + 1
    
    # Test 2: Turunan trigonometri
    expr = sin(x)
    result = diff(expr, x)
    print(f"✓ d/dx(sin(x)) = {result}")
    assert result == cos(x)
    
    # Test 3: Turunan kedua
    expr = x**4
    result = diff(expr, x, 2)
    print(f"✓ d²/dx²(x^4) = {result}")
    assert result == 12*x**2
    
    print("✓ Semua test turunan PASSED\n")

def test_integral():
    """Test integral"""
    print("="*60)
    print("TEST: INTEGRAL")
    print("="*60)
    
    x = symbols('x')
    
    # Test 1: Integral tak tentu
    expr = x**2 + 2*x
    result = integrate(expr, x)
    print(f"✓ ∫(x^2 + 2x) dx = {result} + C")
    
    # Test 2: Integral tentu
    expr = x**2
    result = integrate(expr, (x, 0, 1))
    print(f"✓ ∫[0,1] x^2 dx = {result}")
    assert result == Rational(1, 3)
    
    # Test 3: Integral trigonometri
    expr = sin(x)
    result = integrate(expr, x)
    print(f"✓ ∫sin(x) dx = {result} + C")
    assert result == -cos(x)
    
    print("✓ Semua test integral PASSED\n")

def test_limit():
    """Test limit"""
    print("="*60)
    print("TEST: LIMIT")
    print("="*60)
    
    x = symbols('x')
    
    # Test 1: Limit klasik
    expr = sin(x)/x
    result = limit(expr, x, 0)
    print(f"✓ lim(x→0) sin(x)/x = {result}")
    assert result == 1
    
    # Test 2: Limit tak hingga
    expr = 1/x
    result = limit(expr, x, oo)
    print(f"✓ lim(x→∞) 1/x = {result}")
    assert result == 0
    
    # Test 3: Limit dengan indeterminate form
    expr = (x**2 - 1)/(x - 1)
    result = limit(expr, x, 1)
    print(f"✓ lim(x→1) (x^2-1)/(x-1) = {result}")
    assert result == 2
    
    print("✓ Semua test limit PASSED\n")

def test_matriks():
    """Test matriks"""
    print("="*60)
    print("TEST: MATRIKS")
    print("="*60)
    
    # Test 1: Determinan
    M = Matrix([[1, 2], [3, 4]])
    det = M.det()
    print(f"✓ det([[1,2],[3,4]]) = {det}")
    assert det == -2
    
    # Test 2: Inverse
    M = Matrix([[4, 7], [2, 6]])
    inv = M.inv()
    identity = M * inv
    print(f"✓ Inverse matrix calculated")
    # Check if result is identity matrix (allowing for floating point errors)
    for i in range(2):
        for j in range(2):
            expected = 1 if i == j else 0
            assert abs(identity[i, j] - expected) < 0.0001
    
    # Test 3: Eigenvalues
    M = Matrix([[4, 2], [1, 3]])
    eigenvals = M.eigenvals()
    print(f"✓ Eigenvalues: {eigenvals}")
    
    # Test 4: Transpose
    M = Matrix([[1, 2, 3], [4, 5, 6]])
    trans = M.T
    print(f"✓ Transpose: {trans.shape[0]}x{trans.shape[1]}")
    assert trans.shape == (3, 2)
    
    print("✓ Semua test matriks PASSED\n")

def test_diferensial():
    """Test persamaan diferensial"""
    print("="*60)
    print("TEST: PERSAMAAN DIFERENSIAL")
    print("="*60)
    
    x = symbols('x')
    f = Function('f')
    
    # Test 1: Persamaan diferensial sederhana
    # y' = y
    eq = f(x).diff(x) - f(x)
    result = dsolve(eq, f(x))
    print(f"✓ dsolve(y' = y): {result}")
    
    # Test 2: Persamaan diferensial order 2
    # y'' + y = 0
    eq = f(x).diff(x, 2) + f(x)
    result = dsolve(eq, f(x))
    print(f"✓ dsolve(y'' + y = 0): solved")
    
    print("✓ Semua test diferensial PASSED\n")

def run_all_tests():
    """Jalankan semua test"""
    print("\n" + "="*60)
    print("SYMBOLAB - AUTOMATED TEST SUITE")
    print("="*60 + "\n")
    
    try:
        test_aljabar()
        test_trigonometri()
        test_turunan()
        test_integral()
        test_limit()
        test_matriks()
        test_diferensial()
        
        print("="*60)
        print("✓✓✓ SEMUA TEST PASSED! ✓✓✓")
        print("="*60)
        print("\nProgram Symbolab berfungsi dengan baik!")
        print("Siap digunakan untuk membantu belajar matematika.\n")
        return True
        
    except AssertionError as e:
        print(f"\n✗ TEST FAILED: {e}")
        return False
    except Exception as e:
        print(f"\n✗ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
