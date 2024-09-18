print("Hello, World from main.py!")
def get_coordinates(state):
    coordinates = {
        "Maine":(45.2538,-69.4455),
        "New Hampshire":(43.2081,-71.5382),
        "New York":(40.7128,-74.0060),
        "Massachusetts":(41.5801,-71.3824),
        "Rhode Island":(41.5801,-71.4774),
        "New Jersey":(40.0583,-74.4057),
        "Connecticut":(41.6032,-73.0877),
        "Virginia":(37.4316,-78.6569),
        "Maryland":(39.0458,-76.6413),
        "Delaware":(39.1458,-75.4284),
        "North Carolina":(35.7596,-79.0193),
        "South Carolina":(33.8361,-80.8900),
        "Georgia":(32.1656,-82.9001),
        "Florida":(27.9947,-81.7603),
        "Pennsylvania":(41.2033,-77.1945)
    }
    return coordinates.get(state, "Coordinates not found")
