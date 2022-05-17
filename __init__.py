import requests
import sys

def main(url):
    r = requests.get(url)
    print(r.text)

    print(sys.executable)
    print(sys.version)
    print(sys.version_info)

    import tensorflow as tf
    print(tf.__version__)