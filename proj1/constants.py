from proj1.functions import plain_function, styblisnki_tang_function, shifted_and_rotated_weierstrass_function

ACCURACY = 6
# GENS_COUNT_DIR = {"plain": 1,"styblinski":}
VALUE_FUNC_DIR = {"styblinski": styblisnki_tang_function,
                  "shifted_and_rotated_weierstrass_function": shifted_and_rotated_weierstrass_function}

BEST = "best"
ROULETTE = "roulette"
TOURNAMENT = "tournament"

ONE_POINT = "one-point"
TWO_POINT = "two-point"
UNIFORM = "uniform"
DISCRETE = "discrete"

BOUNDARY = "boundary"

# PLAIN_FUNCTION = "plain"
STYBLISNKI_TANG_FUNCTION = "styblinski"
WEIERSTRASS_FUNCTION = "shifted_and_rotated_weierstrass_function"

REAL = "real"
BINARY = "binary"

GAUSS = "gauss"
