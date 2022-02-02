# Learning Hash table techniques
import ctypes
def hash_function(key):
    return key % 100

def hash_table(size):
    slots = ctypes.py_object * size
    array = slots()

