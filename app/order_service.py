from flask import Blueprint, request, jsonify
from .database import Session
from .models import Order, OrderItem, Product
from .inventory_service import update_stock
from .discount_service import apply_discount

bp = Blueprint("order", __name__)

@bp.post("/order")
def create_order():
    data = request.json
    session = Session()

    order = Order(discount=data["discount"])
    session.add(order)
    session.commit()

    total = 0
    for item in data["items"]:
        product = session.query(Product).filter(Product.id == item["id"]).first()
        total += product.stock * item["qty"]

        order_item = OrderItem(order_id=order.id, product_id=product.id, qty=item["qty"])
        session.add(order_item)

        update_stock(product.id, item["qty"])

    final_amount = apply_discount(total, order.discount)
    session.commit()

    return jsonify({"order_id": order.id, "final_amount": final_amount})
