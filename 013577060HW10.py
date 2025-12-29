import numpy as np
import time
from scipy import linalg
from scipy.linalg import blas

# 產生兩個大小為 200 × 200 的隨機矩陣
np.random.seed(42)  # 設定隨機種子以便結果可重現
A = np.random.rand(200, 200)
B = np.random.rand(200, 200)
print()
print(f"矩陣 A 大小: {A.shape}")
print(f"矩陣 B 大小: {B.shape}")
print()

# 自行實作矩陣乘法（不使用 NumPy 的 dot、@、matmul）
def manual_matrix_multiply(A, B):

    m, n = A.shape
    n2, p = B.shape
    
    if n != n2:
        raise ValueError("矩陣維度不匹配")
    
    # 初始化結果矩陣
    C = np.zeros((m, p))
    
    # 三層迴圈計算矩陣乘法
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i, j] += A[i, k] * B[k, j]
    
    return C

# 測量自行實作版本的執行時間
start_time = time.perf_counter()
C_manual = manual_matrix_multiply(A, B)
end_time = time.perf_counter()
manual_time = end_time - start_time
print()

#  使用 scipy.linalg.blas.dgemm（最fast）
start_time = time.perf_counter()
C_scipy_blas = blas.dgemm(alpha=1.0, a=A, b=B)
end_time = time.perf_counter()
scipy_blas_time = end_time - start_time

#  使用 scipy.linalg 的一般矩陣乘法
start_time = time.perf_counter()
C_scipy = A @ B  # SciPy 實際上會使用優化的 BLAS 庫
end_time = time.perf_counter()
scipy_time = end_time - start_time
print()

print("執行時間比較")
print(f"自行實作版本的執行時間:        {manual_time:.6f} 秒")
print(f"SciPy BLAS 加速版本的執行時間:  {scipy_blas_time:.6f} 秒")
print(f"NumPy/SciPy 標準版本的執行時間: {scipy_time:.6f} 秒")
print()
print(f"加速比 (手動 / BLAS):           {manual_time / scipy_blas_time:.2f}x")
print(f"加速比 (手動 / 標準):           {manual_time / scipy_time:.2f}x")
print()

print()
print()
print()
is_close_blas = np.allclose(C_manual, C_scipy_blas)
is_close_standard = np.allclose(C_manual, C_scipy)

print(f"手動實作 vs SciPy BLAS:   {is_close_blas} " if is_close_blas else f"手動實作 vs SciPy BLAS:   {is_close_blas} ✗")
print(f"手動實作 vs NumPy 標準:   {is_close_standard}" if is_close_standard else f"手動實作 vs NumPy 標準:   {is_close_standard} ✗")
print()

# 最大誤差
max_diff_blas = np.max(np.abs(C_manual - C_scipy_blas))
max_diff_standard = np.max(np.abs(C_manual - C_scipy))
print(f"最大誤差 (vs BLAS):    {max_diff_blas:.2e}")
print(f"最大誤差 (vs 標準):    {max_diff_standard:.2e}")
print()