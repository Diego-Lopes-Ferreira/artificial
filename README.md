# Diego's artifical intelligence lab?

This repo is made out of a lot of diferent things, such as python scripts to
see the camera, electron apps and more...

## Runing the Electron App:
Make sure you have [NodeJS](https://nodejs.org/en/) installed

```sh
$ npm install  // install dependencies
$ npm start    // start development server
```

## Running the python scripts:
Make sure you have [python](https://www.python.org) installed

### The socket server and client:
Open two diferent shells and run this commands (first server, then client)
```sh
$ python socket/server.py
$ python socket/client.py
```


### The openvc scripts:
First, you need to install opencv:
```sh
$ pip install opencv-python
```
Then run the scripts
```sh
$ python opencv/camera.py
```

