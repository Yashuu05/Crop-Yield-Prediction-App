# 🌾 Crop Yield Prediction – Machine Learning + Streamlit Web App

- This project predicts crop yield on the basis of `crop`, `states`, `area`, `fertilizer` and so on.
- It uses a Machine Learning regression model trained on crop data and an interactive Streamlit web app where users can input parameters and instantly get predicted yield values.
- Focuses on Model training using `sklearn`, Feature Engineering / EDA using `pandas`, `seaborn`, `matplotlib` and web app development using `streamlit`. 

---

# Features

- Trained ML regression model with R2 Score of **0.96**.
- Train both Linear Regression and XGB Reegressor. Select best among two.
- Preprocessing + data splitting + evaluation
- Feature importance analysis & visualization
- Interactive Streamlit UI
- Clean and simple design for easy user experience
- Model saved using joblib / pickle for real-time prediction


---

# Tech Stack
- Python 3.13
- Scikit-learn –> ML model
- Pandas –> Data processing
- Matplotlib and Seaborn –> Visualization
- Streamlit –> Web app
- Joblib / Pickle –> Model serialization

--- 

# Project Structure
```
├── dataset/
│   ├── Crop_yield.csv          # dataset used for training
├── model/
│   ├── xgb_model.pkl           # saved model
├── APP/
│   ├── myapp.py                # Streamlit web app
├── notebooks/
│   ├── Crop_yield.ipynb  # model training 
├── README.md
├── requirements.txt

```
---

# Streamlit Web App

Streamlit App workflow: 
- Loads saved model from directory.
- Select or enter input fields (Crop, Rainfall, State, Season, Fertilizer, etc.)
- Review your input data in tabular format to make sure all inputs are correct.
- Click `Predict` button to get predicted crop yield.
- That's it.

---

# Future Improvements

- Add multiple model comparison
- Deploy on cloud (Streamlit Cloud / Render / Heroku)
- Add SHAP explainability
- Add database for storing predictions
- Create a dashboard for farmers/admin panel

---

# Resoruces

- Streanlit: https://docs.streamlit.io/
- Scikit learn: https://scikit-learn.org/stable/supervised_learning.html
- Dataset: https://www.kaggle.com/datasets/saincoder404/crop-yield-data-india 
