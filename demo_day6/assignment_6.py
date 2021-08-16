#question no -1
def show_messages(messages):
    for message in messages:
        print(f"You have {message.title()}")
messages = ['spam message', 'inbox message', 'sent message']
show_messages(messages)


#question no-2

def current_message(messages,sent_messages):
        while messages:
          current_msg=messages.pop()
          print(f"current message: {current_msg.title()}")
          sent_messages.append(current_msg)




def send_messages(sent_messages):
    print(" messages have been sent:")
    for sent_message in sent_messages:
        print(f"sent messages:{sent_message.title()}")
messages = ['spam message', 'inbox message', 'sent message']
sent_messages = []
current_message(messages,sent_messages)
send_messages(sent_messages)
print("messages were moved correctly")


















