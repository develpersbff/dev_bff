from api_module import api_call


article_sample = "Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. Jupiter is one of the brightest objects visible to the naked eye in the night sky, and has been known to ancient civilizations since before recorded history. It is named after the Roman god Jupiter.[19] When viewed from Earth, Jupiter can be bright enough for its reflected light to cast visible shadows,[20] and is on average the third-brightest natural object in the night sky after the Moon and Venus."


def welcome():
    print("""
    *********************************
    Welcome to dev_BFF! 
    Input a search term to 
    retrieve summarized articles
    *********************************
    """)

def user_input():
    question = input("> ")
    # web scrape function here
    # web scrape output is article_text


    api_call(article_text)




if __name__ == '__main__':
    welcome()
    api_call(article_sample)
