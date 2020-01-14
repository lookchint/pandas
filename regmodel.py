from sklearn import linear_model
import statsmodels.api as sm
from sklearn.externals import joblib
def modelreg(X,Y):
    regr = linear_model.LinearRegression()
    regr.fit(X, Y)
    joblib.dump(regr,'reg_model')
    modelreg=joblib.load('reg_model')
    return modelreg
