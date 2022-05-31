import requests

# Задача 1
class Superhero:
    def __init__(self, name, url):
        self.name = name
        self.url = url

    def hero_intelligence(self):
        response = requests.get(self.url)
        data = response.json()
        list = data["results"]
        intelligence = int(list[0]["powerstats"]["intelligence"])
        return intelligence

if __name__ == '__main__':
    Hulk = Superhero("Hulk" , "https://superheroapi.com/api/2619421814940190/search/Hulk")
    Hulk.hero_intelligence()
    Captain_America = Superhero("Captain_America" , "https://superheroapi.com/api/2619421814940190/search/Captain_America")
    Captain_America.hero_intelligence()
    Thanos = Superhero("Thanos" , "https://superheroapi.com/api/2619421814940190/search/Thanos")
    Thanos.hero_intelligence()

    best_indicator = max(Hulk.hero_intelligence(), Captain_America.hero_intelligence(), Thanos.hero_intelligence())
    if best_indicator == Hulk.hero_intelligence():
        print("Самый умный Hulk")
    if best_indicator == Captain_America.hero_intelligence():
        print("Самый умный Captain_America")
    if best_indicator == Thanos.hero_intelligence():
        print("Самый умный Thanos")
