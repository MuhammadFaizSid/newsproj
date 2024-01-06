# News Headline Console Based Application

# 1 step: fetch the current news.

# (API) | newsapi 

# requests | api call 

# modules? 

# in-built - datetime
# external - later

# import datetime

# print(datetime.datetime.now())

# requests | api pr requests bhejne ke lye use hota hay
import requests


def take_initial_user_input():
    while True:
        try:
            user_input = int(input("""
                For Business press 1,
                For Sports press 2,
                For technology press 3,
                For health press 4
                For custom query press 5
                Press 0 for exit
                
                Please enter you input: """))
            if user_input < 6:
                return user_input
    
        except:
            print("Enter the valid integer")

def take_decs_user_input(list_max_index):
    while True:
        try:
            user_input = int(input("Enter the number of the article of which you want to read its description"))
# 101 > 5 | 5
            if user_input > list_max_index:
                print("integer is max")

            else:
                return user_input
        
        except:
            print("enter the valid integer")

while True:

    user_category_input = take_initial_user_input()

    if user_category_input == 1:
        category = "business"

    elif user_category_input == 2:
        category = "sports"

    elif user_category_input == 3:
        category = "technology"

    elif user_category_input == 4:
        category = "health"

    elif user_category_input == 0:
        break

    elif user_category_input == 5:
        while True:

            user_query = input("Enter your query")
            if len(user_query) != 0:
                break

            else:
                print("Enter something in the query")
    
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey=4e5f0bd79a534d53b39908bdcfcd06ca&q={user_query}"


    if user_category_input != 5:
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey=4e5f0bd79a534d53b39908bdcfcd06ca&category={category}"

    request = requests.get(url)

    parsed_data = request.json()
    all_articles = parsed_data['articles']
    total_results = parsed_data['totalResults']

    if total_results == 0:
        print("no news found")

    else:
        articles = all_articles[:5]

        for e, article in enumerate(articles, 1):
            print(e, article['title'], "\n")

        decs_of_article = take_decs_user_input(total_results)
        print(articles[decs_of_article-1]['description'])

print("Thank you for using our app")