import numpy as np
import cpuinfo

print("Cold start...")


def lambda_handler(event, context):

    # get and print processor
    info = cpuinfo.get_cpu_info()['brand']
    print(f"processor: {info}")

    cal = [13815.637, 14917.344, 14425.993, 12699.687]
    SC = np.zeros(4)
    for i in range(4):
        SC[i] = cal[i]

    # matrices operations
    ROWS = 6
    COLS = 6
    to_inv = [[9.9842829544323, 4.585886329998, 1.110212314147, 3.595374092222, 0.292904474147, 0],
              [8.9842829544323, 5.585886329998, 2.110212314147, 4.595374092222, 1.292904474147, 0],
              [7.9842829544323, 6.585886329998, 3.110212314147, 1.595374092222, 2.292904474147, 0],
              [6.9842829544323, 7.585886329998, 1.110212314147, 2.595374092222, 3.292904474147, 0],
              [5.9842829544323, 8.585886329998, 2.110212314147, 3.595374092222, 4.292904474147, 0],
              [4.9842829544323, 9.585886329998, 3.110212314147, 4.595374092222, 5.292904474147, 0]]

    TO_INV = np.zeros((ROWS, COLS))
    for i in range(ROWS):
        for j in range(COLS):
            TO_INV[i, j] = to_inv[i][j]

    for k in range(100):

        # do normalization
        # mean of the sum of root of the sum of squares per cell
        norm_factor = (
                np.sum(np.sqrt(np.sum(np.square(TO_INV), axis=0))) / ROWS
        )
        if norm_factor > 0:
            TO_INV /= (norm_factor *0.5)

        # inversion
        try:
            INV = np.linalg.inv(TO_INV)
        except np.linalg.LinAlgError:
            INV = np.linalg.pinv(TO_INV)

    mult_by = [[2194.105, 0, 0, 0, 0, 0],
               [2194.105, 0, 0, 0, 0, 0],
               [2194.105, 0, 0, 0, 0, 0],
               [2194.105, 0, 0, 0, 0, 0],
               [2194.105, 0, 0, 0, 0, 0],
               [2194.105, 0, 0, 0, 0, 0]]
    MULT = np.zeros((ROWS, COLS))
    for i in range(ROWS):
        for j in range(COLS):
            MULT[i, j] = mult_by[i][j]

    C = np.matmul(INV, MULT)
    res = C[0, 0]

    return {
        "multiplied": res,
        "processor": info
    }


if __name__ == "__main__":
    result = lambda_handler(None, None)
    print(result)
