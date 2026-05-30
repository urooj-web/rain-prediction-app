import streamlit as st
import numpy as np

# ─── Page Config ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Rain Prediction App",
    page_icon="🌧️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ─── Custom CSS ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    * { font-family: 'Inter', sans-serif; }
    .stApp {
        background: linear-gradient(160deg, #0f0c29, #302b63, #24243e);
        min-height: 100vh;
    }
    .block-container {
        max-width: 720px;
        padding: 2rem 2rem 3rem 2rem;
        margin: 0 auto;
    }
    .hero {
        text-align: center;
        padding: 2rem 1rem 1rem;
        margin-bottom: 0.5rem;
    }
    .hero h1 {
        font-size: 2.6rem;
        font-weight: 800;
        color: #ffffff !important;
        margin: 0;
        letter-spacing: -0.5px;
        text-shadow: 0 2px 20px rgba(99,179,237,0.4);
    }
    .hero p {
        color: #a0aec0 !important;
        font-size: 1rem;
        margin-top: 0.5rem;
    }
    .section-label {
        color: #90cdf4 !important;
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        margin: 1.5rem 0 0.75rem;
    }
    .stSlider label p {
        color: #e2e8f0 !important;
        font-size: 0.9rem !important;
        font-weight: 600 !important;
    }
    .stButton > button {
        width: 100%;
        padding: 0.9rem;
        background: linear-gradient(135deg, #4299e1, #667eea);
        color: white !important;
        font-size: 1.05rem;
        font-weight: 700;
        border: none;
        border-radius: 14px;
        margin-top: 1.5rem;
        cursor: pointer;
        box-shadow: 0 4px 20px rgba(66,153,225,0.45);
        transition: all 0.2s ease;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 30px rgba(66,153,225,0.55);
        background: linear-gradient(135deg, #3182ce, #5a67d8);
    }
    .result-rain {
        background: linear-gradient(135deg, #2b6cb0, #2c5282);
        border: 1.5px solid #4299e1;
        border-radius: 18px;
        padding: 1.8rem 1.5rem;
        text-align: center;
        margin: 1.2rem 0;
        box-shadow: 0 8px 32px rgba(66,153,225,0.3);
    }
    .result-rain .emoji { font-size: 2.8rem; }
    .result-rain .title {
        font-size: 1.6rem;
        font-weight: 800;
        color: #ffffff;
        margin: 0.4rem 0 0.2rem;
    }
    .result-rain .confidence {
        font-size: 1rem;
        color: #bee3f8;
        font-weight: 500;
    }
    .result-no-rain {
        background: linear-gradient(135deg, #276749, #22543d);
        border: 1.5px solid #48bb78;
        border-radius: 18px;
        padding: 1.8rem 1.5rem;
        text-align: center;
        margin: 1.2rem 0;
        box-shadow: 0 8px 32px rgba(72,187,120,0.3);
    }
    .result-no-rain .emoji { font-size: 2.8rem; }
    .result-no-rain .title {
        font-size: 1.6rem;
        font-weight: 800;
        color: #ffffff;
        margin: 0.4rem 0 0.2rem;
    }
    .result-no-rain .confidence {
        font-size: 1rem;
        color: #c6f6d5;
        font-weight: 500;
    }
    .metric-row {
        display: flex;
        gap: 1rem;
        margin: 1rem 0;
    }
    .metric-box {
        flex: 1;
        background: rgba(255,255,255,0.07);
        border: 1px solid rgba(255,255,255,0.12);
        border-radius: 14px;
        padding: 1rem 1.2rem;
        text-align: center;
    }
    .metric-box .m-label {
        font-size: 0.78rem;
        color: #a0aec0;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.08em;
    }
    .metric-box .m-value {
        font-size: 1.6rem;
        font-weight: 800;
        margin: 0.2rem 0 0;
    }
    .metric-box .m-value.rain { color: #63b3ed; }
    .metric-box .m-value.norain { color: #68d391; }
    .prob-bar-wrap {
        background: rgba(255,255,255,0.08);
        border-radius: 50px;
        height: 10px;
        overflow: hidden;
        margin: 0.5rem 0 1.2rem;
    }
    .prob-bar-fill {
        height: 100%;
        border-radius: 50px;
        background: linear-gradient(90deg, #4299e1, #667eea);
    }
    .factor-card {
        display: flex;
        align-items: center;
        gap: 0.8rem;
        background: rgba(255,255,255,0.06);
        border: 1px solid rgba(255,255,255,0.10);
        border-radius: 12px;
        padding: 0.8rem 1rem;
        margin: 0.4rem 0;
    }
    .factor-card .dot {
        width: 10px; height: 10px;
        border-radius: 50%; flex-shrink: 0;
    }
    .factor-card .dot.high { background: #fc8181; }
    .factor-card .dot.low  { background: #68d391; }
    .factor-card .f-text { font-size: 0.88rem; color: #e2e8f0; line-height: 1.4; }
    .factor-card .f-text strong { color: #ffffff; }
    .rec-box {
        background: rgba(255,255,255,0.06);
        border: 1px solid rgba(255,255,255,0.12);
        border-radius: 12px;
        padding: 0.9rem 1.1rem;
        font-size: 0.92rem;
        color: #e2e8f0;
        margin: 0.8rem 0;
    }
    .rec-box strong { color: #ffffff; }
    hr { border-color: rgba(255,255,255,0.08) !important; }
    .streamlit-expanderHeader { color: #90cdf4 !important; font-weight: 600 !important; }
    table { color: #e2e8f0 !important; }
    th { color: #90cdf4 !important; }
</style>
""", unsafe_allow_html=True)


# ─── Load / Train Model ──────────────────────────────────────────────────────
@st.cache_resource
def load_model():
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.preprocessing import StandardScaler
    from sklearn.pipeline import Pipeline

    np.random.seed(42)
    n = 5000
    humidity    = np.random.uniform(20, 100, n)
    temperature = np.random.uniform(5,  45,  n)
    pressure    = np.random.uniform(990, 1025, n)
    wind_speed  = np.random.uniform(0,  60,  n)
    cloud_cover = np.random.uniform(0,  100, n)
    dew_point   = np.random.uniform(-5, 30,  n)

    X = np.column_stack([humidity, temperature, pressure,
                         wind_speed, cloud_cover, dew_point])
    rain_prob = (
        (humidity / 100) * 0.35 +
        (cloud_cover / 100) * 0.30 +
        ((30 - dew_point) / 35).clip(0, 1) * 0.15 +
        (wind_speed / 60) * 0.10 +
        ((1013 - pressure) / 23).clip(0, 1) * 0.10
    )
    y = (rain_prob + np.random.normal(0, 0.08, n) > 0.45).astype(int)

    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('clf',    RandomForestClassifier(n_estimators=100, max_depth=8,
                                          random_state=42, n_jobs=-1))
    ])
    pipeline.fit(X, y)
    return pipeline


# ─── HERO ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <h1>🌧️ Rain Prediction App</h1>
    <p>Enter current weather conditions to predict rainfall using Machine Learning</p>
</div>
""", unsafe_allow_html=True)

with st.spinner("⚡ Loading model..."):
    model = load_model()

# ─── INPUT SLIDERS ───────────────────────────────────────────────────────────
st.markdown('<p class="section-label">🌡️ Weather Conditions</p>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    humidity    = st.slider("💧 Humidity (%)",      10, 100, 65)
    temperature = st.slider("🌡️ Temperature (°C)",  5,  45,  22)
    pressure    = st.slider("🔵 Pressure (hPa)",    990, 1025, 1010)
with col2:
    wind_speed  = st.slider("💨 Wind Speed (km/h)", 0,  60,  15)
    cloud_cover = st.slider("☁️ Cloud Cover (%)",   0,  100, 50)
    dew_point   = st.slider("🌫️ Dew Point (°C)",   -5, 30,  14)

# ─── PREDICT ─────────────────────────────────────────────────────────────────
if st.button("🔍 Predict Rain", use_container_width=True, type="primary"):
    features    = np.array([[humidity, temperature, pressure,
                              wind_speed, cloud_cover, dew_point]])
    prediction  = model.predict(features)[0]
    probability = model.predict_proba(features)[0]
    rain_pct    = probability[1] * 100
    no_rain_pct = probability[0] * 100

    st.markdown('<p class="section-label">🎯 Prediction Result</p>', unsafe_allow_html=True)

    if prediction == 1:
        st.markdown(f"""
        <div class="result-rain">
            <div class="emoji">🌧️</div>
            <div class="title">RAIN EXPECTED</div>
            <div class="confidence">Confidence: {rain_pct:.1f}%</div>
        </div>""", unsafe_allow_html=True)
        rec = "☂️ Carry an umbrella and plan for wet conditions today."
    else:
        st.markdown(f"""
        <div class="result-no-rain">
            <div class="emoji">☀️</div>
            <div class="title">NO RAIN EXPECTED</div>
            <div class="confidence">Confidence: {no_rain_pct:.1f}%</div>
        </div>""", unsafe_allow_html=True)
        rec = "😎 Great day to go out! Clear skies expected."

    st.markdown(f'<div class="rec-box">💡 <strong>Recommendation:</strong> {rec}</div>',
                unsafe_allow_html=True)

    st.markdown('<p class="section-label">📊 Probability Breakdown</p>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="metric-row">
        <div class="metric-box">
            <div class="m-label">🌧️ Rain Probability</div>
            <div class="m-value rain">{rain_pct:.1f}%</div>
        </div>
        <div class="metric-box">
            <div class="m-label">☀️ No Rain Probability</div>
            <div class="m-value norain">{no_rain_pct:.1f}%</div>
        </div>
    </div>
    <div class="prob-bar-wrap">
        <div class="prob-bar-fill" style="width:{rain_pct:.0f}%;"></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<p class="section-label">🔎 Key Influencing Factors</p>', unsafe_allow_html=True)
    factors = [
        ("💧 Humidity",    humidity,    70,  f"{humidity}% — {'High: increases rain chance' if humidity > 70 else 'Moderate: neutral effect'}"),
        ("☁️ Cloud Cover", cloud_cover, 60,  f"{cloud_cover}% — {'Dense clouds present' if cloud_cover > 60 else 'Mostly clear sky'}"),
        ("🌫️ Dew Point",   dew_point,   18,  f"{dew_point}°C — {'High moisture in air' if dew_point > 18 else 'Low moisture content'}"),
        ("🔵 Pressure",    pressure,    0,   f"{pressure} hPa — {'Low: unstable weather' if pressure < 1005 else 'Normal/stable pressure'}"),
    ]
    for name, val, threshold, desc in factors:
        is_high = val > threshold if "Pressure" not in name else val < 1005
        dot_cls = "high" if is_high else "low"
        st.markdown(f"""
        <div class="factor-card">
            <div class="dot {dot_cls}"></div>
            <div class="f-text"><strong>{name}:</strong> {desc}</div>
        </div>""", unsafe_allow_html=True)

# ─── ABOUT ───────────────────────────────────────────────────────────────────
st.markdown("---")
with st.expander("ℹ️ About this Project"):
    st.markdown("""
| Detail | Info |
|--------|------|
| **Model** | Random Forest Classifier |
| **Features** | Humidity · Temperature · Pressure · Wind Speed · Cloud Cover · Dew Point |
| **Tech Stack** | Python · Scikit-learn · Streamlit · NumPy |
| **Deployed on** | HuggingFace Spaces |
This app demonstrates an end-to-end ML pipeline:
data preprocessing → feature engineering → model training → web deployment.
""")
