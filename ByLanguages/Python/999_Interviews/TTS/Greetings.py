# import the speech to text module
import pyttsx3

# Initialize the Speech Engine
engine = pyttsx3.init()
# Tell the engine what you want it to say.
engine.say('Greetings Friends')
engine.say('नमस्ते दोस्तों')
engine.say('Good Bye Friends')
# Tell the engine to start saying what you wanted it to and stop when it reaches the end of the queued sayings.
engine.runAndWait()
