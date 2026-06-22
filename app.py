from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import pandas as pd
import joblib

app = Flask(__name__)

# Modeli yükle
with open("knn_model.pkl", "rb") as file:
    model = joblib.load(file)

# Soruların modelde beklenen sırası
FEATURES = (
    [f"EXT{i}" for i in range(1, 11)] +
    [f"EST{i}" for i in range(1, 11)] +
    [f"AGR{i}" for i in range(1, 11)] +
    [f"CSN{i}" for i in range(1, 11)] +
    [f"OPN{i}" for i in range(1, 11)]
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tahmin", methods=["POST"])
def tahmin():
    data = request.get_json()

    try:
        # 50 sorunun hepsini sırayla al
        values = [int(data[name]) for name in FEATURES]

        # Modeli eğitirken kullanılan 100 özellik (50 soru cevabı + 50 süre bilgisi) yapısına uymak için
        # 50 adet varsayılan süre değeri (örn: 1000 ms) ekliyoruz.
        values_100 = values + [1000] * 50

        # Model için numpy array oluştur
        input_data = np.array([values_100])

        # Modeli çalıştır
        prediction = model.predict(input_data)

        # Eğer model 5 ayrı sonuç döndürüyorsa
        pred_array = np.array(prediction).flatten()

        if len(pred_array) >= 5:
            result = {
                "EXT": round(float(pred_array[0]), 2),
                "EST": round(float(pred_array[1]), 2),
                "AGR": round(float(pred_array[2]), 2),
                "CSN": round(float(pred_array[3]), 2),
                "OPN": round(float(pred_array[4]), 2)
            }
        else:
            # Model tek sınıf/cluster sonucu döndürüyorsa
            # En azından formdan trait ortalamalarını hesaplayıp gösteriyoruz
            result = {
                "EXT": round(np.mean([data[f"EXT{i}"] for i in range(1, 11)]), 2),
                "EST": round(np.mean([data[f"EST{i}"] for i in range(1, 11)]), 2),
                "AGR": round(np.mean([data[f"AGR{i}"] for i in range(1, 11)]), 2),
                "CSN": round(np.mean([data[f"CSN{i}"] for i in range(1, 11)]), 2),
                "OPN": round(np.mean([data[f"OPN{i}"] for i in range(1, 11)]), 2),
                "model_sonucu": str(pred_array[0])
            }

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)