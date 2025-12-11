from app.discount_service import apply_discount

def test_discount():
    assert apply_discount(100, 10) == 90
    assert apply_discount(200, 0) == 200
    assert apply_discount(500, 50) == 250
    assert apply_discount(1000, 25) == 750
