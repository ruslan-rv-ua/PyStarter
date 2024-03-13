from notifiers import get_notifier
from snoop import install
install(columns='')

telegram = get_notifier('telegram')

BOT_TOKEN = "7079500117:AAG0piBqaC62hQ8Q0GqE3NF19gi1Liarg84"


def test_chat(chat_id, message='Test the bot!'):
    telegram.notify(message='Hi!', token=BOT_TOKEN, chat_id=chat_id)

@snoop
def get_chat_id():
    print('type something to bot')
    updates = telegram.updates(token=BOT_TOKEN)
    # pp(updates)
    print(f'{updates=}')
    return updates
    
# u = get_chat_id()

test_chat('802354749')
