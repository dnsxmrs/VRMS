def format_vehicle_data(vehicle):
    return f"{vehicle.make} {vehicle.model} ({vehicle.year}) - {vehicle.availability}"

def format_user_data(user):
    return f"{user.username} - {user.email} ({user.contact_info})"
