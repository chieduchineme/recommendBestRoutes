import requests
import pandas as pd
import urllib.parse as urlparse

# Function to get details of all routes and recommend the best one
def get_all_routes_and_recommend_best(startLocation, endLocation, API_KEY):
    # Base URL
    base_url = "https://api.tomtom.com/routing/1/calculateRoute/"

    # Request parameters
    max_alternatives = 3  # Number of alternative routes to request
    request_params = (
        urlparse.quote(startLocation) + ":" + urlparse.quote(endLocation) +
        f"/json?maxAlternatives={max_alternatives}&routeType=fastest&traffic=true&travelMode=car"
    )

    # Construct request URL
    request_url = base_url + request_params + "&key=" + API_KEY

    # Get data from TomTom API
    response = requests.get(request_url)
    json_result = response.json()

    # Extract all route summaries
    routes = json_result['routes']
    route_data = []

    for idx, route in enumerate(routes):
        summary = route['summary']
        travel_time_in_seconds = summary['travelTimeInSeconds']
        traffic_delay_in_seconds = summary['trafficDelayInSeconds']
        no_traffic_time_in_seconds = travel_time_in_seconds - traffic_delay_in_seconds
        distance_in_meters = summary['lengthInMeters']
        arrival_time = summary['arrivalTime']
        departure_time = summary['departureTime']

        # Collecting details for each route
        route_data.append({
            "Route Index": idx + 1,
            "Travel Time (min)": travel_time_in_seconds // 60,
            "Traffic Delay (min)": traffic_delay_in_seconds // 60,
            "No Traffic Time (min)": no_traffic_time_in_seconds // 60,
            "Distance (km)": distance_in_meters / 1000,
            "Departure Time": departure_time,
            "Arrival Time": arrival_time
        })

    # Convert to DataFrame for easier display
    df = pd.DataFrame(route_data)

    # Display details of all routes
    print("Details of All Routes:")
    print(df)

    # Determine the best route based on shortest travel time and minimal traffic delay
    best_route = df.loc[df['Traffic Delay (min)'] <= df['Traffic Delay (min)'].quantile(0.25)].sort_values('Travel Time (min)').iloc[0]

    # Recommend route
    recommended_route_index = best_route['Route Index']
    recommendation_message = (
        f"\nRecommended Route: Route {recommended_route_index} is the best option.\n"
        f"It takes approximately {best_route['Travel Time (min)']} minutes.\n"
        f"This route has a traffic delay of about {best_route['Traffic Delay (min)']} minutes, "
        f"which is better than other routes with higher traffic delays.\n"
        "This route is recommended because it offers the fastest travel time while minimizing the impact of traffic."
    )

    # Return all routes' details and the recommendation message
    return df, recommendation_message

# Example usage:
startLocation = "37.77493,-122.419415"  # San Francisco
endLocation = "34.052234,-118.243685"  # Los Angeles
API_KEY = 'a2cvZL5Hn6VUHWOBOJYMKnqD3122VWnY'  # Replace with your actual API Key

all_routes_df, recommendation_message = get_all_routes_and_recommend_best(startLocation, endLocation, API_KEY)

# Print all routes' details
print(all_routes_df[2])

# Print the recommendation message
print(recommendation_message)
