from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import joblib
import pandas as pd
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Load trained model
model = joblib.load("SolarRadiationPrediction.pkl")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict", response_class=HTMLResponse)
def predict(request: Request,
            temperature: float = Form(...),
            pressure: float = Form(...),
            humidity: float = Form(...),
            speed: float = Form(...),
            wind_direction: float = Form(...)):
    
    # Prepare data for prediction
    input_data = pd.DataFrame({
        'Temperature': [temperature],
        'Pressure': [pressure],
        'Humidity': [humidity],
        'Speed': [speed],
        'WindDirection(Degrees)': [wind_direction]
    })
    
    prediction = model.predict(input_data)[0]
    
    return templates.TemplateResponse("index.html", {
        "request": request,
        "result": round(prediction, 2)
    })

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
