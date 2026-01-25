import requests as r

cal_poly_coords = [35.3010369667717, -120.65987863175936]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}

api_str = "https://api.weather.gov/points/" + str(cal_poly_coords[0]) + "," + str(cal_poly_coords[1])

response = r.get(api_str, headers=headers)

print(response.status_code)

print(response.json())