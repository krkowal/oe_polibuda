from typing import List
import benchmark_functions as bf
import opfunu


def plain_function(values: List[float]):
    return values[0] ** 2 + 5


def styblisnki_tang_function(values: List[float]):
    func = bf.StyblinskiTang(n_dimensions=len(values))
    return func(point=values)


def shifted_and_rotated_weierstrass_function(values: List[float]):
    funcs = opfunu.get_functions_by_classname("F62014")
    func = funcs[0](ndim=len(values))
    func.dim_supported = list(range(2, 101))
    # print(func)
    # point = [25, -34.6]
    return func.evaluate(values)
