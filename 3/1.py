def linear_coefficients(p1, p2):
    B = (p1[1] * p2[0] - p1[0] * p2[1]) / (p2[0] - p1[0])
    K = (p2[1] - p1[1]) / (p2[0] - p1[0])
    return (K, B)

print(linear_coefficients((1, 2), (2, 3)))
#(1.0, 1.0)

print(linear_coefficients((0, 0), (1, 5)))
#(5.0, 0.0)

print(linear_coefficients((0, 2), (2, 2)))
#(0.0, 2.0)

print(linear_coefficients((-2, -2), (-1, -2)))
#(0.0, -2.0)

print(linear_coefficients((1, -1), (-1, 1)))
#(-1.0, 0.0)

print(linear_coefficients((2, 2), (3, 3)))
#(1.0, 0.0)