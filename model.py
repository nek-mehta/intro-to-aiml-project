import csv
import os

WEIGHTS_FILE = "model_weights.txt"

def employees_to_points(employee_percent):
    if employee_percent < 75:
        return 0
    elif employee_percent < 80:
        return 1
    elif employee_percent < 85:
        return 2
    elif employee_percent < 90:
        return 3
    elif employee_percent < 95:
        return 4
    else:
        return 5

def load_dataset(csv_path):
    """
    Loads restaurant_marks.csv and returns:
    X = [[cleanliness_avg, rmaterial_avg, employee_points, taste_score], ...]
    y = [final_score, final_score, ...]
    """

    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    X = []
    y = []

    with open(csv_path, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        required_cols = [
            "cleanliness_avg",
            "rmaterial_avg",
            "employee_percent",
            "taste_score",
            "final_score"
        ]

        for col in required_cols:
            if col not in reader.fieldnames:
                raise ValueError(f"Missing column '{col}' in CSV file.")

        for row in reader:
            a = float(row["cleanliness_avg"])  # out of 10
            q = float(row["rmaterial_avg"])         # out of 10
            emp_percent = float(row["employee_percent"])  # out of 100%
            emp_points = employees_to_points(emp_percent)
            p = float(row["taste_score"])    # out of 20
            fs = float(row["final_score"])     # raw final score

            X.append([a, q, emp_points, p])
            y.append(fs)

    return X, y

def train_from_csv(csv_path):
    """
    Trains a simple linear regression model on the CSV dataset using pure Python.
    Saves weights to a file.
    Returns mean absolute error and weights.
    """
    X, y = load_dataset(csv_path)

    # Add bias term to X
    X_bias = [[1] + features for features in X]

    # Calculate weights using normal equation without numpy
    # w = (X^T X)^-1 X^T y
    # Implement matrix operations manually

    # Helper functions for matrix operations
    def transpose(matrix):
        return list(map(list, zip(*matrix)))

    def matmul(A, B):
        result = []
        for i in range(len(A)):
            row = []
            for j in range(len(B[0])):
                s = 0
                for k in range(len(B)):
                    s += A[i][k] * B[k][j]
                row.append(s)
            result.append(row)
        return result

    def matinv(matrix):
        n = len(matrix)
        AM = [row[:] for row in matrix]
        I = [[float(i == j) for i in range(n)] for j in range(n)]

        for fd in range(n):
            if AM[fd][fd] == 0:
                for i in range(fd+1, n):
                    if AM[i][fd] != 0:
                        AM[fd], AM[i] = AM[i], AM[fd]
                        I[fd], I[i] = I[i], I[fd]
                        break
                else:
                    raise ValueError("Matrix is singular and cannot be inverted")
            fdScaler = 1.0 / AM[fd][fd]
            for j in range(n):
                AM[fd][j] *= fdScaler
                I[fd][j] *= fdScaler
            for i in range(n):
                if i == fd:
                    continue
                crScaler = AM[i][fd]
                for j in range(n):
                    AM[i][j] -= crScaler * AM[fd][j]
                    I[i][j] -= crScaler * I[fd][j]
        return I

    XT = transpose(X_bias)
    XTX = matmul(XT, X_bias)
    XTX_inv = matinv(XTX)
    XTy = matmul(XT, [[val] for val in y])
    w_matrix = matmul(XTX_inv, XTy)
    w = [row[0] for row in w_matrix]

    with open(WEIGHTS_FILE, "w") as f:
        f.write(" ".join(map(str, w)))

    preds = []
    for features in X_bias:
        pred = sum(w[i]*features[i] for i in range(len(w)))
        preds.append(pred)
    mae = sum(abs(preds[i] - y[i]) for i in range(len(y))) / len(y)

    return mae, w

def predict_single(cleanliness_avg, rmaterial_avg, employee_percent, taste_score):
    """
    Predicts final score out of 45 using saved weights and input features.

    Input:
    - cleanliness_avg (out of 10)
    - rmaterial_avg (out of 10)
    - employee_percent (out of 100%)
    - taste_score (out of 20)

    Employee percent is converted to points internally.
    The predicted final score is scaled to be out of 45.
    """
    if not os.path.exists(WEIGHTS_FILE):
        raise FileNotFoundError(f"Model weights file '{WEIGHTS_FILE}' not found. Train the model first.")

    with open(WEIGHTS_FILE, "r") as f:
        w = list(map(float, f.read().strip().split()))

    emp_points = employees_to_points(employee_percent)

    x = [1, cleanliness_avg, rmaterial_avg, emp_points, taste_score]
    pred_raw = sum(w[i]*x[i] for i in range(len(w)))

    max_cleanliness = 10
    max_rmaterial = 10
    max_employee = 5
    max_taste = 20

    max_raw = w[0] + w[1]*max_cleanliness + w[2]*max_rmaterial + w[3]*max_employee + w[4]*max_taste
    if max_raw != 0:
        pred_scaled = (pred_raw / max_raw) * 45
    else:
        pred_scaled = pred_raw

    return pred_scaled 