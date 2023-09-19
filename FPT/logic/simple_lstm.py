# Import necessary libraries
import torch
import torch.nn as nn
import pandas as pd
import torch.nn.functional as F

# import os
# import sys
# parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(parent_dir)
import torch
import numpy as np
import pandas as pd
import torch.nn as nn
from torch.autograd import Variable
from sklearn.metrics import accuracy_score


# Create a class for the LSTM Model
class LSTMModel(nn.Module):
    # Initialize the model with input, hidden and output dimensions
    def __init__(self, input_dim):
        super(LSTMModel, self).__init__()
        self.input_dim = input_dim
        # Define the LSTM layers
        self.lstm1 = nn.LSTM(self.input_dim, 2)
        self.lstm2 = nn.LSTM(2, 1)
        self.lstm3 = nn.LSTM(8, 1)
        # self.lstm4 = nn.LSTM(100, 20)
        # self.lstm5 = nn.LSTM(20, 8)
        self.drop = nn.Dropout(0.1)
        # Define the fully connected layer
        self.fc = nn.Tanh()

    # Define the forward pass of the model
    def forward(self, x):
        # Pass the input through the LSTM layer
        lstm1_out, _ = self.lstm1(x)
        lstm2_out, _ = self.lstm2(lstm1_out)
        # lstm3_out, _ = self.lstm3(self.drop(lstm2_out))
        # lstm4_out, _ = self.lstm3(self.drop(lstm2_out))
        # lstm5_out, _ = self.lstm4(self.drop(lstm3_out))
        # Pass the output through the fully connected layer
        return self.fc(lstm2_out)

    # Define the predict function
    def predict(self, x):
        # Disable gradient calculation
        with torch.no_grad():
            # Get the output from the forward pass
            output = self.forward(x)
            # Get the predicted value by taking the argmax
            output = torch.atanh(output)
            predicted = torch.argmax(output, dim=1)
        return output


def train_lstm_model(
    model,
    train_data_feature,
    train_data_labels,
    test_data_feature,
    test_data_labels,
    num_epochs=100,
    learning_rate=0.001,
):
    criterion = nn.L1Loss()
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

    epochs = []
    losses = []
    for epoch in range(num_epochs):
        outputs = model(train_data_feature)
        loss = criterion(outputs, train_data_labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if (epoch + 1) % 10 == 0:
            print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item()}")
            epochs.append(epoch + 1)
            losses.append(loss.item())

    return model
