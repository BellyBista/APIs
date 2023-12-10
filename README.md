# Restaurant Finder using Foursquare and Google Maps APIs

## Overview

This Python script, `findARestaurant.py`, leverages both the Foursquare and Google Maps APIs to find and display information about nearby restaurants based on specified meal types and locations. It also retrieves a 300x300 picture of the first restaurant found using the Foursquare fsq ID.

## Prerequisites

1. **Foursquare API Credentials:** Obtain your Foursquare API credentials (client ID, client secret, version, and API key) and save them in a `secrets.json` file in the script's parent directory. The `secrets.json` file should have the following structure:

    ```json
    {
        "foursquare_client_id": "YOUR_CLIENT_ID",
        "foursquare_client_secret": "YOUR_CLIENT_SECRET",
        "foursquare_version": "API_VERSION",
        "foursquare_api_key": "YOUR_API_KEY"
    }
    ```

2. **Google Maps API Key:** Obtain your Google Maps API key and save it in the `secrets.json` file alongside the Foursquare credentials:

    ```json
    {
        "google_api_key": "YOUR_GOOGLE_API_KEY"
    }
    ```

3. **Python Libraries:**
   - The script uses the `geocode` module for obtaining latitude and longitude coordinates based on location names.
   - Ensure that the required Python libraries are installed. You can install them using the following command:

    ```bash
    pip install httplib2 requests
    ```

## Usage

1. Run the script:

    ```bash
    python findARestaurant.py
    ```

2. The script is configured with example calls to `find_a_restaurant()` for different meal types and locations. Modify or expand these calls based on your preferences.

3. The script prints information about each restaurant found, including the name, address, and an image URL.

## Script Structure

- **`findARestaurant` Function:**
    - Uses the `geocode` module to obtain latitude and longitude coordinates for a given location using the Google Maps API.
    - Sends a request to the Foursquare API to find nearby restaurants based on meal type, latitude, and longitude.
    - Retrieves details about the first restaurant found, including name, address, and Foursquare fsq ID.
    - Sends another request to get a 300x300 image of the restaurant using the Foursquare fsq ID.
    - Prints restaurant information and returns a dictionary containing the name, address, and image URL.

- **Error Handling:**
    - The script includes exception handling to catch and print any errors that may occur during the execution.

## Notes

- Ensure that your Foursquare API and Google Maps API credentials are valid and have the necessary permissions.
- The script includes default image URLs in case no images are available for a restaurant.