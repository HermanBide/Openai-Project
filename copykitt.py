import os
import openai
import argparse
import re
from dotenv import load_dotenv
from typing import List


Max_input_len = 32
load_dotenv()

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument( "--input", "-i", type=str, required=True)
    args = parser.parse_args()
    user_input = args.input

    # input_client = input("enter you item ")
    # print(f" {input_client}")
    print(f"User input: {user_input}")
    if validate_len(user_input):
        generate_brand_snippet(user_input)
        generate_keywords(user_input)
    else:
        raise ValueError(f"Input length is too long. Must be under {Max_input_len}. submitted input is {user_input}")

def validate_len(prompt: str) -> bool:
    return len(prompt) <= Max_input_len

def generate_keywords(prompt: str) -> List[str]:
    # try to get .env to work here. dont want key showing. 
    openai.api_key = os.getenv("OPENAI_API_KEY")
    brand_prompt = f"Generate related branding keywords for {prompt}: "
    print(brand_prompt)
    response = openai.Completion.create(
        engine="davinci-instruct-beta-v3", 
        temperature=0.1,
        prompt=brand_prompt, 
        max_tokens=38
    )

    keywords_text: str = response["choices"][0]["text"]
    keywords_text = keywords_text.strip()
    keywords_array = re.split(",|\n|;|-", keywords_text)
    print(f"keywords: {keywords_array}")
    return keywords_array

def generate_brand_snippet(prompt: str):
    # try to get .env to work here. dont want key showing. 
    openai.api_key = os.getenv("OPENAI_API_KEY")
    brand_prompt = f"Generate upbeat branding snippet for {prompt}: "
    print(brand_prompt)
    response = openai.Completion.create(
        engine="davinci-instruct-beta-v3", 
        temperature=0.1,
        prompt=brand_prompt, 
        max_tokens=38
    )
    # print(response)
    brand_text = response["choices"][0]["text"]
    brand_text = brand_text.strip()
    last_char = brand_text[-1]

    if last_char not in {".","!","?"}:
        brand_text += "..."
        print(f" snippet: {brand_text}")
    return brand_text

if __name__ == "__main__":
    main()

