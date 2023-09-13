from flask import Flask
# 导入需要的库
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


# 创建Flask应用程序
app = Flask(__name__)

# 创建示例数据
data = [{'id': 1, 'name': 'Alice', 'age': 25},
        {'id': 2, 'name': 'Bob', 'age': 30},
        {'id': 3, 'name': 'Charlie', 'age': 35}]


# 创建获取所有数据的接口
@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data)


# 创建获取单个数据的接口
@app.route('/data/<int:id>', methods=['GET'])
def get_single_data(id):
    for d in data:
        if d['id'] == id:
            return jsonify(d)
    return jsonify({'message': 'Data not found'})


# 创建添加数据的接口
@app.route('/data', methods=['POST'])
def add_data():
    new_data = request.get_json()
    data.append(new_data)
    return jsonify({'message': 'Data added successfully'})


# 创建更新数据的接口
@app.route('/data/<int:id>', methods=['PUT'])
def update_data(id):
    for d in data:
        if d['id'] == id:
            d['name'] = request.json.get('name')
            d['age'] = request.json.get('age')
            return jsonify({'message': 'Data updated successfully'})
    return jsonify({'message': 'Data not found'})


# 创建删除数据的接口
@app.route('/data/<int:id>', methods=['DELETE'])
def delete_data(id):
    for d in data:
        if d['id'] == id:
            data.remove(d)
            return jsonify({'message': 'Data deleted successfully'})
    return jsonify({'message': 'Data not found'})


# 运行Flask应用程序
if __name__ == '__main__':
    app.run(debug=True)
