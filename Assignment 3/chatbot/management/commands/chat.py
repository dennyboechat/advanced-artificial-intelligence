from django.core.management.base import BaseCommand
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


class Command(BaseCommand):
    help = 'Starts an interactive terminal chat session with the ChatterBot'

    def handle(self, *args, **options):
        chatbot = ChatBot(
            'ChatBot',
            logic_adapters=[
                {
                    'import_path': 'chatterbot.logic.BestMatch',
                    'default_response': 'I am sorry, but I do not understand. Could you rephrase that?',
                    'maximum_similarity_threshold': 0.90,
                },
                'chatterbot.logic.MathematicalEvaluation',
            ],
        )

        trainer = ChatterBotCorpusTrainer(chatbot)
        self.stdout.write(self.style.WARNING('Training the chatbot... This may take a moment.'))
        trainer.train('chatterbot.corpus.english')
        self.stdout.write(self.style.SUCCESS('Training complete!'))

        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS('='*50))
        self.stdout.write(self.style.SUCCESS('  ChatterBot Terminal Client'))
        self.stdout.write(self.style.SUCCESS('  Type your message and press Enter'))
        self.stdout.write(self.style.SUCCESS('  Type "quit" or "exit" to end the session'))
        self.stdout.write(self.style.SUCCESS('='*50))
        self.stdout.write('')

        while True:
            try:
                user_input = input('user: ')
            except (KeyboardInterrupt, EOFError):
                self.stdout.write('')
                self.stdout.write(self.style.WARNING('Goodbye!'))
                break

            if user_input.strip().lower() in ('quit', 'exit'):
                self.stdout.write(self.style.WARNING('Goodbye!'))
                break

            if not user_input.strip():
                continue

            response = chatbot.get_response(user_input)
            self.stdout.write(f'bot: {response}')
