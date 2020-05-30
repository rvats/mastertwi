# Working towards creating packages
# import the speech to text module
import pyttsx3


# Initialize the Speech Engine
engine = pyttsx3.init()

# Set the words per minute rate of the Speech engine
engine.setProperty('rate', 105)
# Tell the engine what you want it to say.
engine.say('Good morning.')

# Tell the engine to start saying what you wanted it to and stop when it reaches the end of the queued sayings.
engine.runAndWait()
