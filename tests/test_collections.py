""" import time
from collections import deque

def timed_exec(label, function, *parameters):
    ts = time.time()
    function(*parameters)
    print(label, str((time.time() - ts)*1000))

def run_list(list):    
    timed_exec("Lista preenchida em:", fill_right, list)
    timed_exec("Lista apagada em:", empty_right, list)
    timed_exec("Lista preenchida do comeco:", fill_left, list)
    timed_exec("Tostring em:", tostring, list)
    timed_exec("Tostring_Index em:", tostring_Index, list)
    timed_exec("TostringJoin em:", tostringJoin, list)
    timed_exec("Media em:", media, list)
    timed_exec("Media_Index em:", media_Index, list)
    timed_exec("Lista apagada do comeco em:", empty_left, list)

def fill_right(list):
    for i in range(0, 100000):
        list.append(i)

def fill_left(list):
    for i in range(0, 100000):
        list.insert(0, i)

def empty_right(list):
    if type(list) == deque:
        while(list):
            list.pop()
    else:
        for i in reversed(range(0, len(list))):
            list.pop(i)

def empty_left(list):
    if type(list) == deque:
        for i in range(0, len(list)):
            list.popleft()
    else:
        for i in range(0, len(list)):
            list.pop(0)

def tostring_Index(list):
    string = ""
    for i in range(0, len(list)):
        string += str(list[i])

def tostring(list):
    string = ""
    for item in list:
        string += str(item)

def tostringJoin(list):
    string = "".join([str(x) for x in list])

def media(list):
    total = 0
    for i in list:
        total += i
    return round(total/len(list))

def media_Index(list):
    total = 0
    for i in range(0, len(list)):
        total += list[i]
    return round(total/len(list))

def test_list():
    print("---------- Testando lista comum ----------")
    run_list([])
def test_deque():
    print("---------- Testando deque ----------")
    run_list(deque())
 """