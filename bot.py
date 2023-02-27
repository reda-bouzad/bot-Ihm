from chatterbot import ChatBot
from colorama import Fore, Back, Style
from chatterbot.trainers import ListTrainer


# Uncomment the following lines to enable verbose logging
# import logging
# logging.basicConfig(level=logging.INFO)

# Create a new instance of a ChatBot
bot = ChatBot(
    'Terminal',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
    database_uri='sqlite:///database.db'
    
)

# Define a list of sample dialogues to train the bot
training_data = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
    "What is your name?",
    "My name is Bot.",
    "Who created you?",
    "I was created by Reda , Tarik , Abdelillah.",

]

# Use the ListTrainer to train the bot on the sample dialogues
trainer = ListTrainer(bot)
trainer.train(training_data)

print('')
print(Fore.GREEN + Style.BRIGHT + "Fst-bot :" + Style.RESET_ALL + " what is your name "  )
name = input("User    : ")
print(f"{Fore.GREEN}{Style.BRIGHT}Fst-bot :{Style.RESET_ALL} nice to meet you {name} ")



# The following loop will execute each time the user enters input
while True:
    try:
        user_input = input(name + "    : ")

        bot_response = bot.get_response(user_input)

        print (f"{Fore.GREEN}{Style.BRIGHT}Fst-bot :{Style.RESET_ALL} {bot_response}")

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
