import pickle
from fr.model.manager import get_model_path
from sklearn.linear_model import LinearRegression
def lr_api(length):
    path = get_model_path()
    with open(file=path, mode='rb') as f:
        lr = pickle.load(f)
    prediction = lr.predict([[length]])
    return prediction[0]