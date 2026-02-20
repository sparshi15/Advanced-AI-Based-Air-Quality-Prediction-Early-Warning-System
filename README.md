# Advanced-AI-Based-Air-Quality-Prediction-Early-Warning-System
<!DOCTYPE html>
<html>
<head>
    
</head>
<body style="font-family: Arial, sans-serif; line-height:1.6;">

<h1 align="center">🌍 Delhi AQI Intelligence Platform</h1>

<p align="center">
AI-Powered Air Quality Forecasting & Health Advisory System<br>
Using Machine Learning, Deep Learning, RAG & Real-Time APIs
</p>

<hr>

<h2>📌 Project Overview</h2>
<p>
This project is an advanced AI-based environmental intelligence system designed for Delhi.
It collects real-time air quality and weather data, predicts AQI levels for the next 1–2 days using Deep Learning,
classifies pollution risk using Machine Learning, and generates dynamic health advisories using RAG and Generative AI.
</p>

<hr>

<h2>🚀 Key Features</h2>
<ul>
<li>Real-time AQI & Weather Data Integration</li>
<li>Time-Series Forecasting using LSTM (TensorFlow)</li>
<li>Risk Classification using Scikit-learn</li>
<li>Hospital Load Prediction Model</li>
<li>RAG-based Dynamic Health Advisory Generation</li>
<li>Station-wise Delhi Prediction</li>
<li>Interactive React Dashboard</li>
<li>Hybrid Database (PostgreSQL + MongoDB)</li>
</ul>

<hr>

<h2>🧠 System Architecture</h2>

<pre>
OpenWeather + OpenAQ APIs
            ↓
      PostgreSQL Database
            ↓
   Feature Engineering Layer
            ↓
   LSTM Forecast Model
            ↓
   Risk Classification Model
            ↓
   RAG Knowledge Retrieval
            ↓
   Generative AI Advisory
            ↓
   React Dashboard + Alerts
</pre>

<hr>

<h2>🗄️ Database Design</h2>

<h3>PostgreSQL Tables</h3>
<ul>
<li><b>stations</b> – Delhi monitoring stations</li>
<li><b>aqi_data</b> – Historical & real-time pollution data</li>
<li><b>predictions</b> – ML forecast results</li>
<li><b>alerts</b> – Triggered severe alerts</li>
</ul>

<h3>MongoDB Collections</h3>
<ul>
<li><b>advisories</b> – Generated AI health advisories</li>
<li><b>logs</b> – API and model logs</li>
</ul>

<hr>

<h2>⚙️ Tech Stack</h2>

<table border="1" cellpadding="8">
<tr>
<th>Layer</th>
<th>Technology</th>
</tr>
<tr>
<td>Frontend</td>
<td>React.js</td>
</tr>
<tr>
<td>Backend</td>
<td>FastAPI</td>
</tr>
<tr>
<td>Database</td>
<td>PostgreSQL + MongoDB</td>
</tr>
<tr>
<td>Machine Learning</td>
<td>Scikit-learn</td>
</tr>
<tr>
<td>Deep Learning</td>
<td>TensorFlow (LSTM)</td>
</tr>
<tr>
<td>APIs</td>
<td>OpenWeather + OpenAQ</td>
</tr>
<tr>
<td>RAG</td>
<td>FAISS + LLM</td>
</tr>
</table>

<hr>

<h2>📊 ML Models Used</h2>

<h3>1️⃣ LSTM Model</h3>
<p>
Predicts AQI for the next 1–2 days using historical time-series data.
</p>

<h3>2️⃣ Risk Classification Model</h3>
<p>
Classifies AQI into Good, Moderate, Unhealthy, Very Poor, Severe categories.
</p>

<h3>3️⃣ Hospital Load Prediction</h3>
<p>
Estimates increase in respiratory patient admissions based on AQI.
</p>

<hr>

<h2>📂 Project Structure</h2>

<pre>
backend/
frontend-react/
frontend-streamlit/
database/
rag/
docker-compose.yml
README.md
</pre>

<hr>

<h2>📦 Installation</h2>

<h3>1️⃣ Clone Repository</h3>

<pre>
git clone https://github.com/your-username/delhi-aqi-intelligence-platform.git
cd delhi-aqi-intelligence-platform
</pre>

<h3>2️⃣ Backend Setup</h3>

<pre>
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
</pre>

<h3>3️⃣ Frontend Setup</h3>

<pre>
cd frontend-react
npm install
npm start
</pre>

<hr>

<h2>🐳 Run with Docker</h2>

<pre>
docker-compose up --build
</pre>

<hr>

<h2>📈 Example Output</h2>

<pre>
Predicted AQI Tomorrow: 395
Risk Level: Severe
Hospital Surge Risk: +18%
Advisory Generated: Yes
</pre>

<hr>
<hr>

<h2>📊 Dataset Information</h2>

<h3>🔹 What is a Dataset?</h3>
<p>
A dataset is a structured collection of environmental data used to train and evaluate
machine learning models. In this project, the dataset contains historical air pollution
and weather parameters used for AQI forecasting.
</p>

<h4>Example Dataset Structure:</h4>

<table border="1" cellpadding="8">
<tr>
<th>Date</th>
<th>PM2.5</th>
<th>PM10</th>
<th>NO₂</th>
<th>SO₂</th>
<th>CO</th>
<th>Temperature</th>
<th>Humidity</th>
<th>AQI</th>
</tr>
<tr>
<td>2023-01-01</td>
<td>120</td>
<td>200</td>
<td>40</td>
<td>15</td>
<td>0.8</td>
<td>29</td>
<td>60</td>
<td>250</td>
</tr>
</table>

<hr>

<h3>🔹 Historical Dataset (Model Training)</h3>

<p>
The machine learning and deep learning models are trained using historical air quality data.
</p>

<ul>
<li><b>Kaggle – Air Pollution & Delhi AQI Dataset</b></li>
<li><b>Central Pollution Control Board (CPCB) – Government Data</b></li>
<li><b>OpenAQ – Historical Pollution Data</b></li>
</ul>

<p>
These datasets provide multi-year station-wise AQI and pollutant data,
which are used to train the LSTM time-series forecasting model.
</p>

<hr>

<h3>🔹 Real-Time Data (Live Prediction)</h3>

<p>
For real-time forecasting and dashboard updates, live data is fetched using APIs:
</p>

<ul>
<li><b>OpenWeather API</b> – Temperature, humidity, wind speed, AQI components</li>
<li><b>OpenAQ API</b> – Real-time pollution measurements</li>
</ul>

<p>
The system collects live environmental data every hour, stores it in PostgreSQL,
and uses it as input for prediction and risk classification.
</p>

<hr>

<h3>🔹 How Dataset is Used in the System</h3>

<pre>
Historical Dataset (Kaggle / CPCB)
            ↓
     Train LSTM Model
            ↓
Real-Time API Data
            ↓
     AQI Forecast Prediction
            ↓
     Risk Classification
            ↓
     RAG-Based Advisory Generation
</pre>

<hr>

<h3>🔹 Why This Dataset Strategy is Strong</h3>

<ul>
<li>Combines historical multi-year training data</li>
<li>Integrates real-time API updates</li>
<li>Supports time-series deep learning forecasting</li>
<li>Enables dynamic health advisory generation</li>
<li>Ensures government-backed validation sources</li>
</ul>

<hr>

<h2>🎓 Academic Value</h2>

<ul>
<li>Time-Series Forecasting</li>
<li>Hybrid Database Architecture</li>
<li>Real-Time Data Integration</li>
<li>Full-Stack AI Deployment</li>
<li>RAG-based Generative AI Integration</li>
</ul>

<hr>

<h2>🌟 Future Enhancements</h2>

<ul>
<li>Mobile App Version</li>
<li>SMS Alert System</li>
<li>Satellite Data Integration</li>
<li>Multi-City Expansion</li>
<li>Reinforcement Learning for Adaptive Prediction</li>
</ul>

<hr>

<h2 align="center">Developed for Advanced AI/ML Research & Final Year Project</h2>

</body>
</html>
