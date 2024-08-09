from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

chatbot = ChatBot(
    'Water Conservation Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.MathematicalEvaluation'
    ],
    database_uri='sqlite:///database.sqlite3'
)

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train('chatterbot.corpus.english')

conversation = [
    "Hello",
    "Hi there!",
    "How can I save water?",
    "You can save water by taking shorter showers, fixing leaks, and using water-efficient appliances.",
    "What are some water conservation techniques?",
    "Some techniques include using rain barrels, xeriscaping, and installing low-flow fixtures.",
    "Why is it important to save water?",
    "Saving water is crucial because it helps preserve our environment, reduces the strain on water treatment facilities, and ensures a sustainable supply for future generations.",
    "What is xeriscaping?",
    "Xeriscaping is a landscaping method that reduces or eliminates the need for irrigation by using drought-tolerant plants.",
    "How can I reduce water usage at home?",
    "You can reduce water usage by turning off the tap while brushing your teeth, running full loads of laundry, and using a broom instead of a hose to clean driveways."
]

list_trainer = ListTrainer(chatbot)
list_trainer.train(conversation)


def get_response(user_input):
    return chatbot.get_response(user_input)

if __name__ == "_main_":
    print("Water Conservation Bot is running. Type 'exit' to stop.")
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                break
            response = get_response(user_input)
            print(f"Bot: {response}")
        except(KeyboardInterrupt, EOFError, SystemExit):
            break