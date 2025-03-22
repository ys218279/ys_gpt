# ys_gpt

`ys_gpt` is a personal project that utilizes the OpenAI API to generate feedback on Python scripts by providing a prompt based on the script's content.

## Project Overview

`ys_gpt` is designed to provide quick feedback on your Python scripts using OpenAI's GPT-3. Whether you're writing a new script, maintaining an existing one, or looking for ways to improve your code, this tool helps by analyzing your code and providing recommendations on its structure, readability, and best practices.

## How It Works

1. **Run the Script:**
   - In your terminal, execute the script and provide the file path of the Python script you want to have reviewed.
   
   Example usage:
   ```bash
   python ys_gpt.py /path/to/your/script.py


2. **The Process:**
   - The script will read the contents of the provided file and use it as a prompt to ask questions about the script.
   - Once the API processes the prompt, the feedback will be generated and printed in the terminal.

3. **Expected Output:**
   - You will see the AI-generated response containing feedback on your script.

## Key Requirements

### 1. API Key Configuration

The script requires an OpenAI API key to function. Here’s how to configure it:

- Create a `.env` file in the same directory as the script.
- In the `.env` file, add the following line to store your API key:
  
  ```
  api_key=your_openai_api_key
  ```
  (Replace `your_openai_api_key` with your actual OpenAI API key.)

- The script will automatically load the API key from this `.env` file using the `python-dotenv` package.

> **Important:** Do **not** share your `.env` file publicly, as it contains sensitive information. Keep it private to avoid unauthorized use of your API key.

### 2. Python Dependencies

To run this script, you’ll need the following dependencies:
- `openai` — for interacting with the OpenAI API
- `python-dotenv` — for securely loading the API key from the `.env` file
- `argparse` — for handling command-line arguments

You can install the required dependencies using `pip`:

```bash
pip install openai python-dotenv
```

## Example Usage

1. Create a `.env` file as described above.
2. Save the Python script to your machine.
3. In your terminal, run the following command:

   ```bash
   python ys_gpt.py /path/to/your/script.py
   ```

4. The script will read the contents of the provided file and send a prompt to the OpenAI API to generate feedback.

### Example Output:
```
Sending prompt to GPT-3...

Your script looks well-organized and functional. However, here are some suggestions to improve it:
- Add more error handling to manage file reading issues.
- Consider using more descriptive function names to enhance readability.
...
```

## Troubleshooting

**Q: What should I do if I get an "API key not found" error?**  
A: Make sure the `.env` file is in the same directory as the script and that it contains the correct `api_key` value.

**Q: What if the script fails to run due to missing dependencies?**  
A: Run the following command to install all the required dependencies:
   ```bash
   pip install openai python-dotenv
   ```

## Acknowledgements

- Thanks to [OpenAI](https://openai.com/) for providing the GPT-3 API.
- Special thanks to [python-dotenv](https://pypi.org/project/python-dotenv/) for the easy-to-use dotenv functionality.
- **Inspiration:** This project was inspired by the [pylint](https://pypi.org/project/pylint/) extension, which is used for analyzing Python code and providing feedback on code quality, style, and potential issues.
