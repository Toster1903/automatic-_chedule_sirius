import torch
import torch.nn as nn
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

class AttendancePredictor(nn.Module):
    def __init__(self, input_size):
        super(AttendancePredictor, self).__init__()
        self.layers = nn.Sequential(
            nn.Linear(input_size, 128),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 1)
        )


    def forward(self, x):
        return self.layers(x)

def prepare_data():

    df = pd.read_csv('study_data.csv')

    df['день'] = df['день'].map({
        'Понедельник': 0, 'Вторник': 1, 'Среда': 2,
        'Четверг': 3, 'Пятница': 4, 'Суббота': 5
    })
    

    df['осадки'] = df['осадки'].astype(int)
    

    features = ['день', 'группа', 'сложность', 'температура', 'осадки', 'количество пар']
    X = df[features].values
    y = df['процент посещаемости'].values

    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    X_train = torch.FloatTensor(X_train)
    y_train = torch.FloatTensor(y_train).reshape(-1, 1)
    X_test = torch.FloatTensor(X_test)
    y_test = torch.FloatTensor(y_test).reshape(-1, 1)
    
    return X_train, X_test, y_train, y_test, scaler

def train_model(model, X_train, y_train, epochs=150, learning_rate=0.001):
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001, weight_decay=1e-5)

    
    for epoch in range(epochs):
        model.train()
        optimizer.zero_grad()

        outputs = model(X_train)
        loss = criterion(outputs, y_train)
        

        loss.backward()
        optimizer.step()
        
        if (epoch + 1) % 10 == 0:
            print(f'Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}')

def evaluate_model(model, X_test, y_test):
    model.eval()
    with torch.no_grad():
        predictions = model(X_test)
        mse = nn.MSELoss()(predictions, y_test)
        print(f'Test MSE: {mse.item():.4f}')
        
        # Calculate mean absolute error
        mae = torch.mean(torch.abs(predictions - y_test))
        print(f'Test MAE: {mae.item():.4f}')

def main():
    X_train, X_test, y_train, y_test, scaler = prepare_data()

    input_size = X_train.shape[1]
    model = AttendancePredictor(input_size)
    train_model(model, X_train, y_train)
    evaluate_model(model, X_test, y_test)


    torch.save(model.state_dict(), 'model.pth')
    import joblib
    joblib.dump(scaler, 'scaler.pkl')



if __name__ == "__main__":
    main()
