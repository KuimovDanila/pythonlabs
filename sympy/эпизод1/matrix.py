import sympy as sp

λ, μ, ρ = sp.symbols('λ μ ρ')

matrix = sp.Matrix([
    [0, 0, 0, -1/ρ, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, -1/ρ, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, -1/ρ, 0, 0, 0],
    [-(λ + 2*μ), 0, 0, 0, 0, 0, 0, 0, 0],
    [0, -μ, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, -μ, 0, 0, 0, 0, 0, 0],
    [-λ, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, -λ, 0, 0],
    [-λ, 0, 0, 0, 0, 0, 0, 0, 0]
])

eigenvals = matrix.eigenvals()

for eigenval, multiplicity in eigenvals.items():
    print(f"Собственное значение: {eigenval}, Кратность: {multiplicity}")
