import openai
import argparse
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()
    openai.api_key = os.getenv('api_key')
    
def generate_text(prompt, max_tokens=2048, temperature=0.5, top_p=1, frequency_penalty=0, presence_penalty=0):
    '''Generate text using the OpenAI GPT-3 API'''
    # Set the API key
    configure()

    # Set the model and prompt
    model_engine = "text-davinci-003"

    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty
    )

    # Print the response
    return completion.choices[0].text


def parse_args():
    """Setup and parse arguments"""
    parser = argparse.ArgumentParser(
        description='Read a file which is passed by an argument.')
    parser.add_argument('file_path')
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    path = args.file_path

    with open(path, 'r', encoding="utf-8") as file:
        lines = file.readlines()

    # Define the prompt
    prompt = "Could you rate my python script out of 10 and give me feedback on ow I could improve it?\n\n" + \
        "".join(lines) + "\n\n"
    print(prompt)

    # Print the response
    print(generate_text(prompt))


if __name__ == '__main__':
    main()
