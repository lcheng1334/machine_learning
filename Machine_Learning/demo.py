import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# 读取数据
path = "D:\code\skill\Machine_Learning\melb_data.csv"
data = pd.read_csv(path)


# 清洗数据
all_data = data.dropna(axis=0)

# 确定预测值
y = all_data.Price

# 确定特征值
features = melbourne_features = ["Rooms", "Bathroom", "Landsize", "Lattitude", "Longtitude"]
X =all_data[features]

# 划分数据集
train_X, train_y, val_X, val_y = train_test_split(X, y, random_state=0)

# 定义函数进行训练
def get_mae(max_node, train_X, train_y, val_X, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_node, random_state=0)
    model.fit(train_X, train_y)
    predicted = model.predict(val_X)
    mae = mean_absolute_error(val_y, predicted)
    return mae

