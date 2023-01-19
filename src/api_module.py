import openai
import os
from dotenv import load_dotenv

# Getting .env to process
load_dotenv()
API_KEY = os.getenv('OPENAI_API_KEY')

# sample article text for testing purposes - can delete later
article_sample = "Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. Jupiter is one of the brightest objects visible to the naked eye in the night sky, and has been known to ancient civilizations since before recorded history. It is named after the Roman god Jupiter. When viewed from Earth, Jupiter can be bright enough for its reflected light to cast visible shadows, and is on average the third-brightest natural object in the night sky after the Moon and Venus."


# function to call api
def api_call(full_article_url):
    openai.api_key = API_KEY

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Summarize the following in 2-3 paragraphs:\n\n'''{full_article_url}'''",
        temperature=0.7,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    api_summary_text = response["choices"][0]["text"]
    print(f'\n**** article summary ****')
    print(api_summary_text)
    return api_summary_text



if __name__ == "__main__":
    pass
