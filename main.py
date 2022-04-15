from time import strftime
import requests
from datetime import datetime

# Using Pixela app to track study hours
# https://pixe.la/

# Create User

USERNAME = 'diego1504'
TOKEN = 'g8594yg8gh568hg6850gj8605hg80j6589h'
ID = 'graph1504'

pixela_endpoint = 'https://pixe.la/v1/users'
user_param = {
    'token': USERNAME,  # you can create your token, username here
    'username': TOKEN,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_param)
# print(response.text)

# Create Graph

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    'id': ID,
    'name': "Study Hours",
    'unit': 'Hrs',
    'type': 'float',
    'color': 'shibafu'
}

headers = {
    'X-USER-TOKEN': TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)  # here you can create you graph for you need to control(hours, days) to be more productive
# print(response.text)

# Insert pixel

today = datetime.now()
formatted_time = today.strftime('%Y%m%d')
# if you want create a variable to insert in quantity
hour_study = input('How many hours did you study today?\n')

add_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}"
pixel_config = {
    'date': formatted_time,
    'quantity': hour_study,
}

# here you send your results and make a control of it.
response = requests.post(url=add_pixel_endpoint,
                         json=pixel_config, headers=headers)
print(response.text)

# Update Pixel

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{formatted_time}"
pixel_param = {'quantity': '5'}

# response = requests.put(url=update_pixel_endpoint,json=pixel_param, headers=headers)
# print(response.text)

# Delete Pixel

delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{formatted_time}"

# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.text)
