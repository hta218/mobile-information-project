from flask import *
import mlab
from mongoengine import *
import datetime

app = Flask(__name__)

mlab.connect()

class Data(Document):
    time = DateTimeField()
    location = StringField()
    temperature = FloatField()
    weather = StringField()
    wind_speed = FloatField()
    humidity = IntField()
    rainfall = FloatField()
    sunrise_time = StringField()
    sunset_time = StringField()

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("login.html")
    elif request.method == 'POST':
        print(request.form['username'])
        if request.form["username"] == "admin" and request.form["password"] == "admin":
            return redirect('/admin')


@app.route("/admin")
def admin():
    data_list = Data.objects()
    return render_template('admin.html', data_list=data_list)


@app.route('/add-data', methods=["GET","POST"])
def adddata():
    if request.method == "GET":
        return render_template('add-data.html')
    elif request.method =="POST":
        form = request.form

        time = form['time']
        location = form['location']
        temperature = form['temperature']
        weather = form['weather']
        wind_speed = form['wind_speed']
        humidity = form['humidity']
        rainfall = form['rainfall']
        sunrise_time = form['sunrise_time']
        sunset_time = form['sunset_time']

        data = Data(
            time = time,
            location = location,
            temperature = temperature,
            weather = weather,
            wind_speed = wind_speed,
            humidity = humidity,
            rainfall = rainfall,
            sunrise_time = sunrise_time,
            sunset_time = sunset_time,
        )

        data.save()
        data_list = Data.objects()
        return render_template('admin.html', data_list=data_list)


@app.route('/delete-data/<data_id>')
def deletedata(data_id):
    data = Data.objects().with_id(data_id)
    if data is None:
        print("Not found")
    else:
        data.delete()

    return redirect('/admin')


@app.route('/update-data/<data_id>', methods = ['GET','POST'])
def updatedata(data_id):
    data_list = Data.objects()
    data = Data.objects().with_id(data_id)

    if request.method == "GET":
        return render_template('update-data.html', data=data)
    elif request.method == "POST":
        form = request.form

        time = form['time']
        location = form['location']
        temperature = form['temperature']
        weather = form['weather']
        wind_speed = form['wind_speed']
        humidity = form['humidity']
        rainfall = form['rainfall']
        sunrise_time = form['sunrise_time']
        sunset_time = form['sunset_time']

        data.update(
            set__time = time,
            set__location = location,
            set__temperature = temperature,
            set__weather = weather,
            set__wind_speed = wind_speed,
            set__humidity = humidity,
            set__rainfall = rainfall,
            set__sunrise_time = sunrise_time,
            set__sunset_time = sunset_time
        )

    return redirect('/admin')

if __name__ == '__main__':
  app.run(debug=True)
