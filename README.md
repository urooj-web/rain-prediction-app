# 🌧️ Rain Prediction App

An interactive machine learning web application that predicts whether it will rain based on real-time weather conditions.

🔗 **[Live Demo on HuggingFace Spaces](https://huggingface.co/spaces/UroojFatima123/rain-prediction-app)**


---

## 🚀 Features

- 🌡️ **6 Weather Inputs** — Humidity, Temperature, Pressure, Wind Speed, Cloud Cover, Dew Point
- 🤖 **ML Prediction** — Random Forest Classifier with real-time inference
- 📊 **Probability Breakdown** — Visual rain vs no-rain probability bar
- 🔎 **Factor Analysis** — Key weather factors influencing the prediction
- 💡 **Smart Recommendations** — Actionable advice based on prediction
- 🎨 **Modern Dark UI** — Clean, responsive interface built with Streamlit

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Language** | Python 3.10+ |
| **ML Model** | Random Forest Classifier |
| **Data Processing** | NumPy, Scikit-learn |
| **Web Framework** | Streamlit |
| **Deployment** | HuggingFace Spaces |
| **Version Control** | Git & GitHub |

---

## 🧠 ML Pipeline

```
Weather Data → Preprocessing → Feature Engineering → Model Training → Prediction → Web App
```

**Features used for prediction:**
- 💧 Humidity (%)
- 🌡️ Temperature (°C)
- 🔵 Atmospheric Pressure (hPa)
- 💨 Wind Speed (km/h)
- ☁️ Cloud Cover (%)
- 🌫️ Dew Point (°C)

---

## 📁 Project Structure

```
rain-prediction-app/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## 🔍 How It Works

1. User adjusts **weather sliders** to set current conditions
2. App feeds values into a trained **Random Forest Classifier**
3. Model returns **rain / no-rain prediction** with confidence score
4. App displays **probability breakdown** and **key influencing factors**
5. A **recommendation** is shown based on the result

---

## 📊 Model Details

- **Algorithm:** Random Forest Classifier
- **Training:** Synthetic weather dataset (5,000 samples)
- **Pipeline:** StandardScaler → RandomForestClassifier
- **Parameters:** 100 estimators, max depth 8

---

## 🌐 Deployment

This app is deployed on **HuggingFace Spaces** using the Streamlit SDK.

👉 **Try it live:** [huggingface.co/spaces/UroojFatima123/rain-prediction-app](https://huggingface.co/spaces/UroojFatima123/rain-prediction-app)

---


