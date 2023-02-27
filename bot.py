from chatterbot import ChatBot
from colorama import Fore, Back, Style
from chatterbot.trainers import ListTrainer


# Uncomment the following lines to enable verbose logging
# import logging
# logging.basicConfig(level=logging.INFO)

# Create a new instance of a ChatBot
# Create a new instance of a ChatBot
bot = ChatBot(
    'Terminal',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.6
        }
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
    "Who created you",
    "I was created by Reda , Tarik , Abdelillah.",
    "Qui t'a créé",
    "par Reda , Tarik , Abdelillah",
    "Qui a créé ce chatBot ?",
    "j'étais créé par Reda bouzad et Abdelillah boulgha et Tariq elqari .",
    "Quelle est la date de création de ce chatBot ?",
    "Ce chatbot a été créer en février 2023.",
    "Quel est le but de créer ce chatBot?",
    "Ce chatbot recommande des documentaires.",
    "Dans quelle filière étudient Reda, Abdelilah et Tariq ?",
    "ils étudient dans la filiére SIR",
    "Qu'est-ce que SIR",
    "SIR est l'abréviation de SYSTEMES INFORMATIQUES REPARTIS",
    "Dans quelle faculté se trouve cette branche ?",
    "C'est qui le doyen de cette faculté ?"
    "Le doyen de cette faculté est M. Mohamed JBILOU."
















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

bot.storage.drop()
