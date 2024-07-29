# encoder/utils.py

def encode_message_odd_day(message):
    encoding_dict = {chr(i + 65): str(i + 1).zfill(2) for i in range(26)}
    encoded_message = ''.join([encoding_dict[char] if char.isalpha() else char for char in message.upper()])
    return encoded_message

def encode_message_even_day(message):
    encoding_dict = {chr(i + 65): f'5{i + 1:02}' for i in range(26)}
    encoded_message = ''.join([encoding_dict[char] if char.isalpha() else char for char in message.upper()])
    return encoded_message
