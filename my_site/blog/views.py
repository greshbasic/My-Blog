from datetime import date

from django.shortcuts import render

all_posts = [
    {
        "slug": "the-strawhats",
        "image": "strawhats.png",
        "author": "Gresh",
        "date": date(2024, 6, 12),
        "title": "The Strawhats",
        "excerpt": "Learn what each Strawhat Pirate's dream is and what their roles are in the crew.",
        "content": """
                    The Strawhat Pirates consist of the captain Monkey D. Luffy, the combatant Roronoa Zoro, 
                    the navigator Nami, the sniper Usopp, the cook Sanji, the doctor Tony Tony Chopper, the archaeologist Nico Robin,
                    the shipwright Franky, the musician Brook, and the helmsman Jinbe. Each strawhat has their own unique abilities and dreams. 
                    Luffy wants to become the Pirate King, Zoro wants to become the greatest swordsman, Nami wants to draw a map of the world, 
                    Usopp wants to become a brave warrior of the sea, Sanji wants to find the All Blue, Chopper wants to become the greatest doctor,
                    Robin wants to uncover the true history of the world, Franky wants to build a ship that can circumnavigate the world, 
                    Brook wants to reunite with his friend Laboon, and Jinbe wants to unite the fishmen and humans. The crew all share the ambition of
                    making Luffy the Pirate King and are willing to do anything to achieve that goal. 
                   """
    },
    {
        "slug": "gears",
        "image": "gear2.png",
        "author": "Gresh",
        "date": date(2024, 6, 12),
        "title": "Luffy's Gears",
        "excerpt": "What are Luffy's gears and what do they do?",
        "content": """
                    Luffy's gears are special techniques Luffy uses to increase his power and speed. Gear Second,
                    involves Luffy pumping his blood faster to increase his speed and power. Gear Third, involves
                    Luffy blowing air into his bones to increase his size and strength. Gear Fourth, involves Luffy
                    inflating his muscles and imbuing them with massive amounts of haki to significantly increase his power and speed. 
                    Lastly, Gear Fifth, involves Luffy awakening his devil fruit, the Hito Hito no Mi, Model: Nika, which increases his
                    physical abilities and haki, allows him to turn his surroundings into rubber, and lets him use his imagination to
                    fight in any way he wants. Gear 2nd and 3rd were showcased in the Enies Lobby arc, Gear 4th was showcased in the Dressrosa Arc
                    and Gear 5th was showcased in the Wano Arc.
                   """
    },
    {
        "slug": "haki",
        "image": "haki.png",
        "author": "Gresh",
        "date": date(2024, 6, 12),
        "title": "Haki Explained",
        "excerpt": "What are the different types of Haki?",
        "content": """
                    Haki is the second power system in the One Piece world. Haki is divided into three types:
                    Observation Haki, Armament Haki, and Conqueror's Haki. Observation Haki allows the user to sense the presence, strength, and emotions of others.
                    Armament Haki allows the user to create an invisible armor around themselves, increasing their offensive and defensive capabilities.
                    Conqueror's Haki allows the user to exert their willpower over others, causing them to faint or be intimidated. 
                    Haki is a form of spiritual energy that flows through all living things. Armament and observation haki can be trained and developed 
                    through rigorous training and experience, but Conqueror's Haki is a rare ability that you are born with.
                    
                    There are also advanced forms of each haki type. Advanced Observation Haki allows the user to see into the future. 
                    Advanced Armament Haki allows the user to emit their haki into something else, destroying it from the inside.
                    Advanced Conqueror's Haki allows the user to coat themselves with an invisible armor, just like Armament Haki, but it is significantly stronger,
                    being considered not only the strongest form of Haki, but the strongest ability in the One Piece world.
                   """
    },
]


# Create your views here.
def starting_page(request):
    sorted_posts = sorted(all_posts, key=lambda post: post["date"], reverse=True)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })

def post_detail(request, slug):        
    identified_post = next(post for post in all_posts if post["slug"] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })
