# Help resources
# https://www.devdungeon.com/content/run-python-wsgi-web-app-waitress
# https://opensource.com/article/23/3/build-raspberry-pi-dashboard-appsmith#:~:text=Build%20a%20Raspberry%20Pi%20monitoring%20dashboard%20in%20under,to%20the%20internet%20...%205%205.%20Repetition%20
# https://www.geeksforgeeks.org/how-to-get-current-cpu-and-ram-usage-in-python/
# http://icanhazip.com/
# https://answers.opencv.org/question/196218/python-opencv-how-to-read-avi-file/
# location: C:\Users\user\Desktop\Project_DataAnalytics\Scripts
#----------------------------------------------------------------------------
# Created By  : Nandkishor Motiram Dhawale
# Created Date: 20241130
# Last Modification Date: 20241130
# version ='1.0'
# ---------------------------------------------------------------------------

"""Module documentation goes here
   This is an API like programm to get CPU data post it on a locally hosted web browser
"""

from flask import Flask
from flask_restful import Resource, Api
import psutil
app = Flask(__name__)
api = Api(app)

class CPUData(Resource):
    def get(self):
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        system_info_data = {
            'cpu_percent': psutil.cpu_percent(1),
            'cpu_count': psutil.cpu_count(),
            'cpu_freq': psutil.cpu_freq(),
            'cpu_mem_total': memory.total,
            'cpu_mem_avail': memory.available,
            'cpu_mem_used': memory.used,
            'cpu_mem_free': memory.free,
            'disk_usage_total': disk.total,
            'disk_usage_used': disk.used,
            'disk_usage_free': disk.free,
            'disk_usage_percent': disk.percent}
            #'sensor_temperatures': psutil.sensors_temperatures(fahrenheit=False)}
            #'sensor_temperatures': psutil.sensors_temperature()["cpu_thermal"][0].current,
            #'sensor fan' : psutil.sensors_fans()}
        return system_info_data
            
api.add_resource(CPUData, '/get-stats')

if __name__ == '__main__':
    app.run(debug=True)