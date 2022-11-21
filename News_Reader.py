# f7aa997f445946dba1906621f368f74c
# News Reader program
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    voices = speak.GetVoices()
    speak.Voice = voices[1]
    speak.Speak(str)


def getnews():
    import requests
    import time
    url = ('https://newsapi.org/v2/top-headlines?'
           'country=us&'
           'apiKey=f7aa997f445946dba1906621f368f74c')
    response = requests.get(url)
    news = response.json()['articles']
    x = 1
    for index, article in enumerate(news):
        if (x < 10 and len(article['title']) > 55):
            print(f"{x}. {article['title']}\n")
            speak(f"{x}{article['title']}\n")
            x += 1
            time.sleep(1)


if __name__ == "__main__":
    print("\t\t\t\tHey Buddy! WELCOME TO OUR NEWS READER APP.\n")
    speak("Hey Buddy! WELCOME TO OUR NEWS READER APP.")
    getnews()
