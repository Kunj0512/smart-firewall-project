import joblib

MODEL_PATH = 'models/decision_tree.pkl'

def recommend_rule(port):
    """
    Return a simple ALLOW/BLOCK decision for a given port.
    """
    clf = joblib.load(MODEL_PATH)
    prediction = clf.predict([[port]])
    return "ALLOW" if prediction[0] == 1 else "BLOCK"


def generate_rule(port):
    """
    Generate a structured firewall rule for the given port.

    This keeps things simple and generic but provides a JSON‑ready rule
    object that can be downloaded from the UI.
    """
    port = int(port)
    action = recommend_rule(port)

    rule = {
        "source": "any",
        "destination": "any",
        "protocol": "tcp",
        "port": port,
        "action": action,
        "description": "Auto‑generated rule from Smart Firewall Recommender"
    }
    return rule
