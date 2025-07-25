from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib
import mlflow
import mlflow.sklearn
from data_loader import fetch_data

df  = fetch_data()
if df.empty:
    raise Exception("No data found in MongoDB!")
 
x = df.drop(columns=["monthly_charge", "customer_id"])
y = df["monthly_charge"]
#print(x)
#print(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

model = LinearRegression()
model.fit(x_train, y_train)

score = model.score(x_test, y_test)

joblib.dump(model, "model.pkl")

with mlflow.start_run():
    mlflow.sklearn.log_model(model, "linear_model")
    mlflow.log_metric("r2_score", score)

print(f"Linear Regression model saved.  R² Score: {score:.2f}")