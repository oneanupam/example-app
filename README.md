# Example App
This repository contains Example App written in python programming language using flask framework of web development.

## Prerequisites
Below prerequisites must be fulfilled for successful execution of code.

### Software Requirement
Resources in this repository are meant for use with Python 3.x (check the version using `python3 --version`) and pip3 (check the version using `pip3 --version`). If you don't have the compatible version, download it from official python repository.

- [python3](https://www.python.org/downloads/) >= 3.10.14
- [pip3](https://pypi.org/project/pip/) >= 23.0.1

### Bootstrap Virtual Environment
It is a best practice to create a virtual environment for your application to avoid any conflict in dependencies between multiple applications. Hence, it is recommended to create a virtual environment (using python's default package "venv" or of your choice) and install all the dependencies. Follow below according to your operating system.

```bash
# Linux OS:
python3 -m venv example-app-venv
source example-app-venv/bin/activate
pip install -r requirements.txt

# Windows OS:
python -m venv example-app-venv
example-app-venv\Scripts\activate
pip install -r requirements.txt
```

> [!NOTE]
> Activation makes the virtual environment the default Python interpreter for the duration of a shell session. Because, This will prepend that directory to your PATH, so that running python will invoke the virtual environment’s Python interpreter. As an indication of virtual environment activation, current shell prompt will prepend the name of the virtual environment you are currently using.
>
> To deactivate the environment, simply type `deactivate` and you will return to your normal shell.
>
> Within the virtual environment, you can use the command `pip` instead of `pip3` and `python` instead of `python3`.

## Run and Test the App on Local Machine
Flask has the built-in Werkzeug server. To start the default dev web server of the app, execute the below command -

```bash
# To start the default dev web server of the app
python python/run.py
```

To start the production grade wsgi gunicorn server, execute the below command -

```bash
gunicorn main:app
gunicorn --bind :9090 --workers 1 --threads 8 main:app

# Where:
# gunicorn -> Runs the Gunicorn WSGI server
# --bind :9090 -> Bind to all network interfaces (0.0.0.0) on port 9090
# --workers -> 1	Start 1 worker process
# --threads -> 8	Each worker can run 8 threads concurrently
# main:app -> main is the Python file name (i.e., main.py), and app is the Flask app object inside it
```

To check the webapp, open a browser and hit the below URL -

``` bash
http://<IP>:Port
http://127.0.0.1:4999/
```

## Run and Test the App on Docker
1. Clone the repository and switch inside the directory.
2. Build the docker image using one of below command:

```bash
docker build -t eapp:latest .
docker build -t eapp:latest -f Dockerfile.dev .
```

3. To run the docker container from built image in the background with port mapping, use one of below command:

```bash
# To explicitly specify the what port to map in the form, <host_port>:<container_port>
    # with --rm flag, Docker will automatically remove the container after the container exits.
docker run -d -p 5000:4999 --name eapp-container eapp:latest

# To map the exposed port (via EXPOSE) to random ports on the host machine
docker run -d -P --name eapp-container eapp:latest
```

4. To test the app on host machine, open the browser or use curl command:
```bash
    curl http://localhost:5000
```

> [!NOTE]
> ( . ) tells about the build context. The build context is the current directory (.), which should contain your application code and the Dockerfile. Pass the Dockerfile, if its name is not exactly Dockerfile.
>
> Port mapping is used to access the services running inside a Docker container. In the above case, we can now access the application using port 5000 on the host machine.

## References
- https://www.warp.dev/terminus/docker-logs-tail
- https://www.warp.dev/terminus/docker-expose-port
- https://www.warp.dev/terminus/docker-exec-container
- https://www.warp.dev/terminus/docker-start-container
