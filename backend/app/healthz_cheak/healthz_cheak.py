from flask_healthz import HealthError

def printok():
    print("Everything is fine")

def liveness():
    try:
        printok()
    except Exception:
        raise HealthError("Can't connect")

def readiness():
    try:
        printok()
    except Exception:
        raise HealthError("Can't connect")