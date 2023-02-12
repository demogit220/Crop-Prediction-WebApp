import model
#write code for flask app which uses get.html for getting input and post.html for displaying output and uses predictor.py for prediction
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_input():
    return render_template('get.html')

@app.route('/result', methods=['POST'])
def post_output():
    if request.method == 'POST':
        place = request.form['state'].lower() + '-' + request.form['district'].lower()
        season = request.form['season']
        year = request.form['year']
        rainfall = request.form['rainfall']
        p = request.form['p']
        n = request.form['n']
        k = request.form['k']
        data = {
            #make whole string lowercase and just keep first character as capital
            'state': request.form['state'].lower().capitalize(),
            'district': request.form['district'].lower().capitalize(),
            #capitalize first letter of each word and keep rest as lowercase there may have multiple words in season
            'soil': request.form['season'].title(),
            'place': place,
            'season': season,
            'year': int(year),
            'rainfall': int(rainfall),
            'p': int(p),
            'n': int(n),
            'k': int(k)
        }
        # print(data)
        result = model.predict_crop(0,data)
        # print(result)
        data['crop'] = result[0][0]
        data['temp'] = int(result[1][0][0])
        data['price'] = result[2]
        print(data)

        # print("test")
        # result = ""
        return render_template('result.html', result=data)
    return render_template('get.html')

@app.route('/svm', methods=['GET'])
def get_svm():
    return render_template('svm.html')

@app.route('/svm_result', methods=['POST'])
def post_svm_output():
    if request.method == 'POST':
        place = request.form['state'].lower() + '-' + request.form['district'].lower()
        season = request.form['season']
        year = request.form['year']
        rainfall = request.form['rainfall']
        p = request.form['p']
        n = request.form['n']
        k = request.form['k']
        data = {
            #make whole string lowercase and just keep first character as capital
            'state': request.form['state'].lower().capitalize(),
            'district': request.form['district'].lower().capitalize(),
            #capitalize first letter of each word and keep rest as lowercase there may have multiple words in season
            'soil': request.form['season'].title(),
            'place': place,
            'season': season,
            'year': int(year),
            'rainfall': int(rainfall),
            'p': int(p),
            'n': int(n),
            'k': int(k)
        }
        # print(data)
        result = model.predict_crop(1,data)
        # print(result)
        data['crop'] = result[0][0]
        data['temp'] = int(result[1][0][0])
        data['price'] = result[2]
        print(data)

        # print("test")
        # result = ""
        return render_template('result.html', result=data)
    return render_template('get.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
