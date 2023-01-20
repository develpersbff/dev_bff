from api_module import api_call
from web_scraping_module import web_scraper, web_scraper_second
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()


def audio_results(text_result):
    engine.say("Do you want me to read your results? Please type in (yes or no)")
    engine.runAndWait()
    response = input("\n\nDo you want me to read your results? Please type in (yes/no): ")
    if response == "yes":
        engine.say(text_result)
        engine.runAndWait()

    else:
        print("No Worries!")


def audio_assistant():

    def on_start():
        print()

    def on_word(name):
        print()

    def on_end(name):
        print(name)

    engine.connect('started-utterance', on_start)
    engine.connect('started-word', on_word)
    engine.connect('finished-utterance', on_end)

    engine.say("Do you want to use an audio assistant? Please type in (yes or no): ")
    engine.runAndWait()

    response = input("Do you want to use an audio assistant? Please type in (yes/no): ")
    if response == "yes":
        print("Audio assistant activated.")
        engine.say("Audio assistant activated. Welcome to Dev_BFF! Your best friend in learning. Dev BFF is an online tool to help developers summarize long articles. Want to know how to get started?")
        print('Welcome to Dev_BFF! Your best friend in learning. Dev BFF is an online tool to help developers summarize long articles! Want to know how to get started?')
        engine.runAndWait()
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Say Something!')
            audio = r.listen(source)
            print('Done!')
            engine.say(" To get started... Input a search term to retrieve summarized articles. Have fun!")

        text = r.recognize_google(audio)
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
            *Be patient, results take a few seconds to load*
            Have fun!
            *********************************
            """)
        engine.runAndWait()
        link = web_scraper("query")
        user_input = api_call(link)
        audio_results(user_input)

    else:
        print("Audio assistant not activated.")
        print('Welcome to Dev_BFF! Your best friend in learning. Dev BFF is an online tool to help developers summarize long articles')


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


def what_next(cont_input):
    print("""
    What would you like to do next? 
    "n" for a different article, 
    "l" to get a link to the article, 
    "q" to quit,
    """)
    user_input2 = str(input('>> '))
    if user_input2.lower() == "n":
        api_call(web_scraper_second(cont_input))
        print("thank you for using dev_BFF, see you next time!")
        return
    if user_input2.lower() == "l":
        url = web_scraper(cont_input)
        print(f"{url}\n")
        print("thank you for using dev_BFF, see you next time!")
        return
    if user_input2.lower() == "q":
        print("thank you for using dev_BFF, see you next time!")
        return


if __name__ == '__main__':
    audio_assistant()
    welcome()
    link = web_scraper("query")
    user_input = api_call(link)
    what_next(link)
