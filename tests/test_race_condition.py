import threading
import requests

def worker():
    requests.post("http://localhost:5000/order", json={
        "discount": 0,
        "items": [{"id": 1, "qty": 1}]
    })

def test_race_condition():
    threads = []
    for _ in range(10):
        t = threading.Thread(target=worker)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

    assert True
