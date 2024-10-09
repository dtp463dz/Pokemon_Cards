# Đây là chuyển data thành API dựa trên Flask

from flask import Flask, jsonify
import csv

def read_csv(file_path):
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        data = [row for row in csv_reader]
    return data

data = read_csv('pokemon_data_22.csv')

app = Flask(__name__)

# Hàm API trả về dữ liệu từ CSV
@app.route('/api/data', methods=['GET'])
def get_data():
    data = read_csv('pokemon_data_22.csv')
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
