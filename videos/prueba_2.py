# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os

# The text that you want to convert to audio
mytext = "Hola. Vamos a probar a configurar Visual Studio Code"
#'Hola, Lola, ¿cómo estás? Esto es una prueba. Instalaremos Visual Studio Code.'

# Language in which you want to convert
language = 'es'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False, tld='ie')

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("prueba-1.mp3")

# Playing the converted file
#os.system("mpg321 welcome.mp3")
