"""
Welcome to The Boredless Tourist, an online application giving you the power to find the parts of the city that fit the pace of your life. 
We at The Boredless Tourist run a recommendation engine using Python. We first evaluate what a person’s interests are and then give them recommendations in their area to venues, restaurants, and historical destinations that we think they’ll be engaged by. 
Let’s get started!
"""

#creating a list of destinations
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "Sao Paulo, Brazil", "Cairo, Egypt"]

#defining a test traveler
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]
#index 1 for name, 2 for destination, 3 for hobbies
#included nested list

#indexing locations
def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

#testing function
#print(get_destination_index("Los Angeles, USA"))
#print(get_destination_index("Paris, France"))
#print(get_destination_index("Hyderabad, India"))

#function for user's location (very public)
def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index
#is it literally the same function but for a customer?

#mic test mic test
test_destination_index = get_traveler_location(test_traveler)
#print(test_destination_index)

#list of attractions
attractions = []

for destination in destinations:
  attractions.append([])

#alternative# 
#attractions = [[] for destination in destinations]

#printing out attractions
#print(attractions)

def add_attraction(destination, attraction):
  try:
   destination_index = get_destination_index(destination)
   attractions_for_destination = attractions[destination_index].append(attraction)
  except ValueError:
    return

add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
#print(attractions)
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

#this function is to help travelers find attractions
def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []
  for attraction in attractions_in_city:
    possible_attraction = attraction
    attraction_tags = attraction[1]
    for interest in interests:
      if interest in attraction_tags:
        attractions_with_interest.append(possible_attraction[0])
  return attractions_with_interest

#testing out whatever the hell that was
la_arts = find_attractions("Los Angeles, USA", ['art'])
#print(la_arts)

#the interface finally 
def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)
  interests_string = "Hi " + traveler[0] + ", we think you'll like these places around " + traveler_destination + ": " 
  for attraction in traveler_attractions:
    interests_string += attraction
    interests_string += ", "
  return interests_string

#the test drive
smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)