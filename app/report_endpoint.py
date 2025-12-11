from flask import Blueprint, jsonify

bp = Blueprint("debug", __name__)

@bp.get("/debug/report")
def debug_report():
    return jsonify({
        "race_condition": "Fixed using threading.Lock",
        "memory_leak": "Fixed by clearing cache",
        "n+1_query": "Fixed using eager loading",
        "discount_logic": "Corrected percentage formula",
        "code_quality": "Improved structure and modules"
    })
