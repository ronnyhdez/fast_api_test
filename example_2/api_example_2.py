import uvicorn
from fastapi import FastAPI
import numpy as np
from sklearn.linear_model import LinearRegression

app = FastAPI()

x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
y = np.array([5, 20, 14, 32, 22, 38])
# print(x)

model = LinearRegression()

model.fit(x, y)

# print(f"intercept: {model.intercept_}")
# print(f"slope: {model.coef_}")


@app.get("/get-new-value/{new_value}")
def get_new_value(new_value: float):
    value_to_predict = np.array([new_value]).reshape((-1, 1))
    y_pred = model.predict(value_to_predict)
    return y_pred[0]


# a = get_new_value(7)
# print(a)
# print(f"predicted response:\n{y_pred}")

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
