
from tqdm import tqdm

def count_matches(a_start, b_start):

    a_mul_factor = 16807
    b_mul_factor = 48271
    mul_modulus = 2147483647

    a_val = a_start
    b_val = b_start

    matches = 0

    for _ in tqdm(range(40_000_000)):

        a_val *= a_mul_factor
        a_val %= mul_modulus

        b_val *= b_mul_factor
        b_val %= mul_modulus

        if (a_val & 0xffff) == (b_val & 0xffff):
            matches += 1

    return matches

if __name__ == "__main__":
    A_START = 703
    B_START = 516
    print(count_matches(A_START, B_START))