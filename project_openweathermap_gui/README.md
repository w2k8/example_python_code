# This is an example code for python

This python code creates a window with python tkinter.
it uses a public api form openweathermap to get some data.
This data is a json structure.
In the code there is a small example how to extract some data from json.

![Example](https://raw.githubusercontent.com/w2k8/example_python_code/main/project_openweathermap_gui/images/demo_openweathermap_gui1.png)

![Example](https://raw.githubusercontent.com/w2k8/example_python_code/main/project_openweathermap_gui/images/demo_openweathermap_gui2.png)

Included a basic form of logging.

```
DEBUG 2023-09-07T14:09:44.304 - Starting new HTTPS connection (1): openweathermap.org:443
DEBUG 2023-09-07T14:09:44.479 - https://openweathermap.org:443 "GET /data/2.5/weather?appid=439d4b804bc8187953eb36d2a8c26a02 HTTP/1.1" 200 None
INFO 2023-09-07T14:09:44.480 - Het weer voor Amsterdam vandaag: 26.65 ℃ en clear sky
DEBUG 2023-09-07T14:17:23.402 - Starting new HTTPS connection (1): openweathermap.org:443
DEBUG 2023-09-07T14:17:23.498 - https://openweathermap.org:443 "GET /data/2.5/weather?appid=b1b15e88fa797225412429c1c50c122a1 HTTP/1.1" 401 None
DEBUG 2023-09-07T14:54:59.079 - Starting new HTTPS connection (1): openweathermap.org:443
DEBUG 2023-09-07T14:54:59.243 - https://openweathermap.org:443 "GET /data/2.5/weather?appid=439d4b804bc8187953eb36d2a8c26a02 HTTP/1.1" 200 None
INFO 2023-09-07T14:54:59.244 - Het weer voor Amsterdam vandaag: 28.54 ℃ en clear sky
```
