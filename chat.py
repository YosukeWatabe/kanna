command_file = open('chat.txt', encoding='utf-8')
raw_data = command_file.read()
command_file.close()
lines = raw_data.splitlines()



bot_dict = {}
for line in lines:
    word_list = line.split(',')
    key = word_list[0]
    response = word_list[1]
    bot_dict[key] = response

def chat(command):
    response = ''
    for key in bot_dict:
        if key in command:
            response = bot_dict[key]
            break

    if not response:
        response = '何ヲ言ッテイルカ、ワカラナイ'
    return response