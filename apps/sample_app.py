import sys
sys.path.append('/home/youngsuklee/jacob/abc')

from flask import Flask, render_template, request
from weather.weather_api_call import my_func

app = Flask(__name__)

@app.route('/')
def home():
    weather_data = my_func(3)  # Assuming my_func takes a parameter and returns weather data
    return render_template('index.html', weather=weather_data)

@app.route('/save', methods=['POST'])
def save():
    data = request.form['data']
    with open('saved_data.txt', 'a') as file:
        file.write(data + '\n')
    return 'Data saved successfully!'

if __name__ == "__main__":
    app.run(debug=True)