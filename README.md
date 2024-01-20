# qdvis (Quick Data Visualizer)
This is a tool to easily visualize the logs when long time processing is required by simply starting up a local server.

<img width="1680" alt="スクリーンショット 2024-01-20 14 41 22" src="https://github.com/ta-ke-inf/qdvis/assets/115391575/5bda04b5-da97-449e-b3c0-508cd9749ffd">

## Installation
```
pip install qdvis
```
## Usage
1. Exmaple of code. Let the log be added to the writer object anywhere in the code (e.g., loop).
```python
from qdvis.writer import LogWriter

writer = LogWriter()

num_epochs = 10
for epoch in range(num_epochs):
    for inputs, targets in data_loader:
        outputs = model(inputs)
        loss = criterion(outputs, targets)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    
    print(f"Epoch {epoch+1}/{num_epochs}, Loss: {loss.item()}")

    writer.add_scalar(x_value=epoch, y_value=loss.item())
```
2. You can start a terminal and launch a local server for visualization with the `qdvis` command.
```
qdvis --logpath ./logs/log.json --port 8000
```
- --logpath:  path for log file.
- --port: port of local server.


## Methods
gpu utilization can be added to the log
```
add_scaler(x_value, y_value)
```
Parameters
- x_value(float): x scaler value of 2D chart.
- y_value(float): y scaler value of 2D chart.




2D chart can be added to the log
```
add_gpu_status()
```