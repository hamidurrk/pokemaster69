# PokeMaster69: The Ultimate Socializing Tool

PokeMaster69 is an automated tool designed to streamline the process of poking people on Facebook. By leveraging Selenium WebDriver, it simulates user interactions to poke back those who poked the user and initiate pokes with new people. It provides a convenient way to engage in this casual form of interaction on the platform.

## Installation Process

1. **Python Environment Setup**:
   - Ensure you have Python installed on your system.
   
2. **Install Required Packages**:
   - Run `pip install selenium tqdm webdriver_manager` to install necessary packages.

3. **Download WebDriver**:
   - Ensure you have the appropriate WebDriver for your browser installed or installed automatically. This script uses Firefox, and it manages the WebDriver automatically using `GeckoDriverManager` from `webdriver_manager`.

4. **Facebook Credentials**:
   - Provide your Facebook username and password in the script or store them in a secure file. Update the `username` variable and provide the path to your credentials file in the `with open()` statement. Alternatively, insert the password directly.

## Usage 

1. **Initialize PokeMaster69**:
   - Create an instance of the `PokeMaster69` class by providing your Facebook username, password, and optionally the browser type.

2. **Login to Facebook**:
   - Use the `login()` method to log in to your Facebook account.

3. **Start Poking**:
   - Use the `poke()` method to start the poking process. You can specify the number of new people to poke as an argument.

## Functionality

Here's an overview of its functionalities:

1. **Using Marionette**:
   - Upon initialization, the script sets up a WebDriver instance (Firefox) using Selenium in a marionette port that always stays logged in. It also provides a welcome message.

2. **Logging In**:
   - The `login()` method navigates to Facebook's login page and enters the provided username and password. After logging in, it waits for a few seconds before proceeding.

3. **Poking People**:
   - The `poke()` method navigates to the user's poke page on Facebook.
   - It then iterates through the list of people who poked the user back and pokes them back in return. It displays the number of people poked back.
   - Next, it iterates through a specified number of new people to poke and pokes them. It scrolls the page to ensure all elements are visible.
   - After poking, it reloads the poke page and repeats the process.

4. **Highlighting Elements**:
   - The `highlight_element()` method is used to visually highlight elements on the page. It's primarily used to highlight people being poked.

5. **Dynamic Waiting Functionality**:
   - The `wait()` function is used to create a loading indicator while waiting for a certain duration. It uses tqdm for a progress bar.

