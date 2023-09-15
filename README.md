# Twitter Fake Account Checker

This Python script allows you to check the likelihood of a Twitter account being fake based on its followers count and tweets count.

## Prerequisites

Before you begin, ensure you have the following:

- Python (3.x) installed on your machine.
- Tweepy library for accessing the Twitter API. You can install it using pip:pip install tweepy

## Getting Started

1. Clone this repository to your local machine:git clone https://github.com/imanav10/fakecheck.git
2. Navigate to the project directory:cd fakecheck
3. Open the script file `fakecheck.py` in a text editor of your choice.

4. Add your Twitter API credentials:
- `consumer_key`
- `consumer_secret`
- `access_token`
- `access_token_secret`

5. Save the file.

## Usage

1. Run the script by executing the following command:python code.py
2. Enter the Twitter username you want to check for fake followers when prompted.
3. The script will calculate a fake percentage based on the user's followers count and tweets count and display the result.

## Errors

- If the user is not found on Twitter, the script will display an Error.

## Customization

You can adjust the formula for calculating the fake percentage in the `calculate_fake_percentage` function according to your requirements.

## Contributing

Contributions to improve this script are welcome! Feel free to open issues or create pull requests.

---

**Disclaimer:** This script is for educational and informational purposes only. The accuracy of determining fake accounts may vary, and results should be interpreted with caution.






