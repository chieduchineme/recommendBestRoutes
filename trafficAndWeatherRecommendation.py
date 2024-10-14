import json

data = {
    "day1": [
        {"time": "06:00", "route": "Route A", "timeRequired": 20, "weather": "Good", "traffic": "Yes"},
        {"time": "06:00", "route": "Route B", "timeRequired": 25, "weather": "Poor", "traffic": "No"},
        {"time": "06:00", "route": "Route C", "timeRequired": 22, "weather": "Good", "traffic": "Yes"},
        {"time": "06:10", "route": "Route A", "timeRequired": 22, "weather": "Good", "traffic": "No"},
        {"time": "06:10", "route": "Route B", "timeRequired": 23, "weather": "Poor", "traffic": "Yes"},
        {"time": "06:10", "route": "Route C", "timeRequired": 20, "weather": "Good", "traffic": "No"},
        {"time": "06:20", "route": "Route A", "timeRequired": 25, "weather": "Poor", "traffic": "Yes"},
        {"time": "06:20", "route": "Route B", "timeRequired": 28, "weather": "Poor", "traffic": "Yes"},
        {"time": "06:20", "route": "Route C", "timeRequired": 22, "weather": "Good", "traffic": "Yes"},
        {"time": "06:30", "route": "Route A", "timeRequired": 30, "weather": "Poor", "traffic": "Yes"},
        {"time": "06:30", "route": "Route B", "timeRequired": 32, "weather": "Poor", "traffic": "Yes"},
        {"time": "06:30", "route": "Route C", "timeRequired": 24, "weather": "Good", "traffic": "No"}
    ],
    "day2": [
        {"time": "06:00", "route": "Route A", "timeRequired": 30, "weather": "Poor", "traffic": "No"},
        {"time": "06:00", "route": "Route B", "timeRequired": 28, "weather": "Good", "traffic": "Yes"},
        {"time": "06:00", "route": "Route C", "timeRequired": 26, "weather": "Good", "traffic": "Yes"},
        {"time": "06:10", "route": "Route A", "timeRequired": 32, "weather": "Poor", "traffic": "Yes"},
        {"time": "06:10", "route": "Route B", "timeRequired": 29, "weather": "Good", "traffic": "Yes"},
        {"time": "06:10", "route": "Route C", "timeRequired": 28, "weather": "Poor", "traffic": "No"},
        {"time": "06:20", "route": "Route A", "timeRequired": 35, "weather": "Poor", "traffic": "Yes"},
        {"time": "06:20", "route": "Route B", "timeRequired": 32, "weather": "Good", "traffic": "Yes"},
        {"time": "06:20", "route": "Route C", "timeRequired": 30, "weather": "Poor", "traffic": "Yes"},
        {"time": "06:30", "route": "Route A", "timeRequired": 40, "weather": "Poor", "traffic": "Yes"},
        {"time": "06:30", "route": "Route B", "timeRequired": 35, "weather": "Good", "traffic": "Yes"},
        {"time": "06:30", "route": "Route C", "timeRequired": 33, "weather": "Poor", "traffic": "Yes"}
    ],
    "day3": [
        {"time": "06:00", "route": "Route A", "timeRequired": 18, "weather": "Good", "traffic": "No"},
        {"time": "06:00", "route": "Route B", "timeRequired": 21, "weather": "Good", "traffic": "Yes"},
        {"time": "06:00", "route": "Route C", "timeRequired": 25, "weather": "Poor", "traffic": "No"},
        {"time": "06:10", "route": "Route A", "timeRequired": 20, "weather": "Good", "traffic": "No"},
        {"time": "06:10", "route": "Route B", "timeRequired": 23, "weather": "Poor", "traffic": "Yes"},
        {"time": "06:10", "route": "Route C", "timeRequired": 26, "weather": "Good", "traffic": "Yes"},
        {"time": "06:20", "route": "Route A", "timeRequired": 22, "weather": "Good", "traffic": "No"},
        {"time": "06:20", "route": "Route B", "timeRequired": 25, "weather": "Good", "traffic": "Yes"},
        {"time": "06:20", "route": "Route C", "timeRequired": 28, "weather": "Poor", "traffic": "No"},
        {"time": "06:30", "route": "Route A", "timeRequired": 24, "weather": "Good", "traffic": "No"},
        {"time": "06:30", "route": "Route B", "timeRequired": 28, "weather": "Good", "traffic": "Yes"},
        {"time": "06:30", "route": "Route C", "timeRequired": 30, "weather": "Poor", "traffic": "Yes"}
    ]
}

def get_best_route(routes):
    # Filter routes with good weather
    good_weather_routes = [route for route in routes if route["weather"] == "Good"]

    # Find the route with the minimum time among the good weather routes
    if good_weather_routes:
        return min(good_weather_routes, key=lambda x: x["timeRequired"])
    return None

prev_best_route = None

def print_best_route(day_data, time):
    global prev_best_route
    current_routes = [entry for entry in day_data if entry["time"] == time]

    best_route = get_best_route(current_routes)

    if best_route:
        print(f"At {time}, the best route is {best_route['route']} taking {best_route['timeRequired']} minutes.")

        if prev_best_route:
            if best_route["route"] != prev_best_route["route"]:
                print(f"The previous best route was {prev_best_route['route']} but it is no longer the best because of {('weather' if prev_best_route['weather'] != best_route['weather'] else 'traffic')}.")
            else:
                print(f"The previous best route {prev_best_route['route']} is still the best.")
        prev_best_route = best_route
    else:
        print(f"At {time}, there is no route with good weather.")

# Iterate through each day and print best routes at different times
for day, day_data in data.items():
    print(f"\n--- {day} ---")
    print_best_route(day_data, "06:00")
    print_best_route(day_data, "06:10")
    print_best_route(day_data, "06:20")
    print_best_route(day_data, "06:30")