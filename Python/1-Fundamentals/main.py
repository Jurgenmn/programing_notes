import random

big_cities_cold = ["Seattle, WA", "New York City, NY", "Boston, MA",
              "Chicago, IL", "Baltimore, MA", "Philadelphia, PA", "Detroit, MI"]
big_cities_warm = ["Los Angeles, CA", "Phoenix, AZ", "Austin, TX", "San Antonio, TX", "San Diego, CA", "Dallas, TX",
              "San Jose, CA", "Atlanta, GA", "Miami, FL", "Las Vegas, NV"]

moderate_cities_cold = ["Madison, WI", "Denver, CO", "Albany, NY", "Cleveland, OH", "Tampa, FL", "Hudson, NY", "Asheville, NC"]
moderate_cities_warm = ["New Orleans, LA", "Austin, TX", "Nashville, TN", "Honolulu, HI", "Charleston, SC",
                   "Albuquerque, NM", "Tampa, FL", "St. Petersburg, FL", "Arlington, TX", "Tulsa, OK"]

liberal_near_ocean = ["Los Angeles, CA", "New York City, NY", "Hudson, NY", "San Diego, CA", "Honolulu, HA"]
liberal_not_near_ocean = ["Austin, TX", "Seattle, WA", "New Orleans, LA", "Asheville, NC", "Hudson, NY", "Detroit, MI", "Chicago, IL", "Baltimore, MA", "Philadelphia, PA"]
conservative_near_ocean = ["San Antonio, TX", "Tampa, FL", "Anchorage, AK", "Miami, FL"]
conservative = ["San Antonio, TX", "Tampa, FL", "Anchorage, AK", "Miami, FL", "Omaha, NB", "Las Vegas, NV", "Arlington, TX", "Tulsa, OK", "Phoenix, AZ", "San Antonio, TX", "Dallas, TX"]


question = []

game_on = True
while game_on:
    question_a = int(input(
        "Question: Do you want to live in 1. A Big City, 2. Small City or Town. Please answer with the number of the question. "))
    question_b = int(input(
        "Question: Do you want to live 1. Somewhere with seasons, 2. Somewhere that stays warm year round "))
    question_c = int(input("Question: Do you prefer 1. A liberal area, 2. A conservative area"))
    question_d = int(input("Do you want to live 1. Near a beach, 2. Doesn't matter"))
    if question_a == 1 and question_b == 1:
        question.append(big_cities_cold)
    elif question_a == 1 and question_b == 2:
        question.append(big_cities_warm)
    elif question_a == 2 and question_b == 1:
        question.append(moderate_cities_cold)
    elif question_a == 2 and question_b == 2:
        question.append(moderate_cities_warm)
    if question_c == 1 and question_d == 1:
        question.append(liberal_near_ocean)
    elif question_c == 1 and question_d == 2:
        question.append(liberal_not_near_ocean)
    elif question_c == 2 and question_d == 1:
        question.append(conservative_near_ocean)
    elif question_c == 2 and question_d == 2:
        question.append(conservative)
    else:
        print("That is not a valid option. Try again.")
    game_on = False



final_place = max(question)
if len(final_place) > 1:
    selection = random_item_from_list = random.choice(final_place)

print("You should live in " + selection)
