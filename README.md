# chatgpt-cli
source code from https://github.com/slithery0/gpt-chatbot-cli

a simplified version only reserves "Q&A" preset, which is enough for daily use.

## Install
Firstly, recomand to create a python virtual environment using [venv](https://docs.python.org/3/library/venv.html) or [VirtualFish](https://virtualfish.readthedocs.io/en/latest/)(for fish shell) or something else.

Then install python dependencies.
``` shell
pip3 install -r requirments.txt
```
Edit `chatgpt-cli.py` to add your api_key in the flowwing line.
```
api_key = ""
```
Grant the script execution authority.
```
chmod +x ./chatgpt-cli.py
```
Finally, you can copy the script to `/usr/bin` directory.
```
sudo cp ./chatgpt-cli.py /usr/bin/chatgpt-cli
```
## Usage
just run `chatgpt-cli` command and start your journey.
