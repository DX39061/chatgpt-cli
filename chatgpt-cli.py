#!/usr/bin/env python3
import openai
import termcolor
from prompt_toolkit import prompt

# import api key
api_key = ""

presets = {
    "Q&A": {
        "message": "", 
        "inject": {
            "state": True,
            "start": "",
            "end": "> "
        },
    }
}

def check_api_key_validity(api_key):
    try:
        openai.api_key = api_key
        openai.Model.list()
        print(termcolor.colored(f"API key is valid", 'light_green', attrs=["bold"]))
    except:
        print(termcolor.colored(f"Invalid API key", 'light_red', attrs=["bold"]) + "\nGrab your API key from: "+termcolor.colored(f"https://beta.openai.com/account/api-keys", 'light_blue', attrs=["underline"]))
        exit()

def main():
    check_api_key_validity(api_key)

    # set model and temperature
    model = "text-davinci-003"
    temperature = 0.9

    # Initialize conversation_history
    conversation_history = ""

    try:
        chosen_preset = "Q&A"
            
        # Replace #END# and #START# with preset's end and start's string if available
        if "inject" in presets[chosen_preset] and presets[chosen_preset]["inject"]["state"]:
            state = True
            end_string = presets[chosen_preset]["inject"]["end"]
            start_string = presets[chosen_preset]["inject"]["start"]
        else:
            state = False
            end_string = ">"
            start_string = ">"
            
        # start chat loop
        while True:
            # get user input
            user_input = prompt(end_string)

            if user_input.lower() in ["quit","exit","q"]:
                break
            # generate response
            response = openai.Completion.create(
                engine=model,
                prompt=conversation_history + end_string + user_input + "\n" + start_string,
                temperature=temperature,
                max_tokens=1024,
            )
            if (state):
                conversation_history += end_string + user_input + "\n" + response.choices[0].text + "\n"
            else:
                conversation_history = presets[chosen_preset]["message"]
            # print response with termcolor
            print(termcolor.colored(f"{start_string}{response.choices[0].text}", 'light_blue'))

    except KeyboardInterrupt:
        print("Exiting...")
        exit(0)

if __name__ == '__main__':
    main()