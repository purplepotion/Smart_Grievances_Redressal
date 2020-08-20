from googletrans import Translator

def translateText(string):
    translator = Translator()
    return translator.translate(string,dest='en').text
 