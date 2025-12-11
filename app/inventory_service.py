import threading
lock = threading.Lock()

from .database import Session
from .models import Product

def update_stock(product_id, qty):
    with lock:
        session = Session()
        product = session.query(Product).filter(Product.id == product_id).first()
        product.stock -= qty
        session.commit()
