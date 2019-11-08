import speech_recognition as sr 
import webbrowser as wb

#Initialize the recognizer
r=sr.Recognizer()
r2=sr.Recognizer()

with sr.Microphone() as source: 
    #wait for a second to let the recognizer adjust the  
    #energy threshold based on the surrounding noise level 
    r.adjust_for_ambient_noise(source) 
    print ("Say Something")
    #listens for the user's input 
    audio = r.listen(source) 
          
    try: 
        text = r.recognize_google(audio) 
        print ("you said: " + text )
        if 'Ok Google' in text:
            print('hi')
            r2=sr.Recognizer()
            url='https://www.google.com/search?q='
            with sr.Microphone() as source:
                print('search your query')
                audio=r2.listen(source)
            try:
                get=r2.recognize_google(audio)
                print(get)
                wb.get().open_new(url+get)
            except sr.UnknownValueError: 
                    print("Google Speech Recognition could not understand audio") 
      
            except sr.RequestError as e:
                     print("Could not request results from Google  Speech Recognition service; {0}".format(e)) 
    #error occurs when google could not understand what was said 
      
    except sr.UnknownValueError: 
        print("Google Speech Recognition could not understand audio") 
      
    except sr.RequestError as e: 
        print("Could not request results from Google  Speech Recognition service; {0}".format(e)) 