import torch
import numpy as np
import joblib
from model import AttendancePredictor

scaler = joblib.load('scaler.pkl')

example = np.array([[0, 3, 5, 20, 1, 4]])
example_scaled = scaler.transform(example)
example_tensor = torch.FloatTensor(example_scaled)


input_size = 6
model = AttendancePredictor(input_size)
model.load_state_dict(torch.load('model.pth'))
model.eval()

with torch.no_grad():
    predicted_attendance = model(example_tensor).item()
    print(f"Предсказанный процент посещаемости: {predicted_attendance:.2f}%")
