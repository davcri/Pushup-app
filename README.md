# Pushup app
![Pushup-app Main Window screenshot](http://imgur.com/ngrWVMJ.jpg "Pushup-app MainWindow screenshot")

**Note**:This application is only a proof of concept made to test the Python language
for a desktop application. There is no UI/UX design involved
in this project. 

This app stores your progresses in physicals exercises, like
pushups, on a local database.


* __Target Platform__ : PC, actually Pushup-app has been tested only on Linux,
  but it should be portable.
* __State__: Not in development
* __License__ : [GPL
  v3.0](https://github.com/davcri/Pushup-app/blob/master/LICENSE.txt)

# Run the application
First check your requirements ! If all libraries are installed on your system
then :

1. Download the [source
   code](https://github.com/davcri/Push-up-app/archive/master.zip).
2. Extract the archive.
3. Open the terminal and run
```python main.py```

# Requirements
- __Python__ _2.7.8_ : Installed by default on most Linux distros
- __PySide__ _1.2.1_: For _apt-based_ Linux distros, open your terminal and run

```sudo apt-get install python-pyside```

 Otherwise look at the official documentation:
 https://pypi.python.org/pypi/PySide#installation

- __Matplotlib__ _1.3.1_: http://matplotlib.org/

# Development
I'm developing this application on __Linux__ (Mint 17) with :

- __Programming language__ : Python 2.7.6
- __Database__ : Sqlite3
- __GUI__ : Pyside 1.2.1 (Qt 4.8)
- __Graph__ : Matplotlib (1.3.1)
