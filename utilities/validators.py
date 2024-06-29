def validate_vehicle_data(make, model, year, availability):
    if not make or not model or not year or not availability:
        return False
    return True

def validate_user_data(username, email, contact_info):
    if not username or not email or not contact_info:
        return False
    return True
