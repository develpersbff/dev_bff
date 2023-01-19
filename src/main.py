from api_module import api_call
from web_scraping_module import web_scraper, web_scraper_second

article_sample = "Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. Jupiter is one of the brightest objects visible to the naked eye in the night sky, and has been known to ancient civilizations since before recorded history. It is named after the Roman god Jupiter.[19] When viewed from Earth, Jupiter can be bright enough for its reflected light to cast visible shadows,[20] and is on average the third-brightest natural object in the night sky after the Moon and Venus."


def welcome():
    print('''
    
██████╗░███████╗██╗░░░██╗░░░░░░██████╗░███████╗███████╗
██╔══██╗██╔════╝██║░░░██║░░░░░░██╔══██╗██╔════╝██╔════╝
██║░░██║█████╗░░╚██╗░██╔╝░░░░░░██████╦╝█████╗░░█████╗░░
██║░░██║██╔══╝░░░╚████╔╝░░░░░░░██╔══██╗██╔══╝░░██╔══╝░░
██████╔╝███████╗░░╚██╔╝░░█████╗██████╦╝██║░░░░░██║░░░░░
╚═════╝░╚══════╝░░░╚═╝░░░╚════╝╚═════╝░╚═╝░░░░░╚═╝░░░░░
    ''')
    print("""
    *********************************
    Welcome to Dev_BFF!       
    Your best friend in learning! 
    Input a search term to 
    retrieve summarized articles.
    *Results take a few seconds to load*
    Have fun!
    *********************************
    """)


def what_next():
    print("""
    What would you like to do next? 
    "n" for a different article, 
    "l" to get a link to the article, 
    "q" to quit,
    """)
    user_input2 = str(input('>> '))
    if user_input2.lower() == "n":
        api_call(web_scraper_second(user_input))
        print("thank you for using dev_BFF, see you next time!")
        return
    if user_input2.lower() == "l":
        url = web_scraper(user_input)
        print(f"{url}\n")
        print("thank you for using dev_BFF, see you next time!")
        return
    if user_input2.lower() == "q":
        print("thank you for using dev_BFF, see you next time!")
        return


if __name__ == '__main__':
    welcome()
    user_input = str(input('>> '))
    api_call(web_scraper(user_input))
    what_next()
