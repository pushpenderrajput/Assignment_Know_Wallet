Technical Document for ChatGPT Integration

Introduction:
The ChatGPT Integration is a simple application that uses OpenAI's GPT-3 model to generate text responses based on user input. The application is built using the Flask web framework in Python and uses HTML templates to render the front-end.

Files:
The application consists of three files: app.py, index.html, and results.html.

app.py:
The app.py file contains the main code for the application. It imports the necessary modules and libraries, sets up the OpenAI API key, defines a function to generate responses using the GPT-3 model, and sets up the Flask routes. The routes include the home page, which displays a form for the user to enter a prompt, and the results page, which displays the prompt and the generated response.

index.html:
The index.html file contains the HTML code for the home page. It includes a form with a single input field for the user to enter a prompt and a submit button. The form is set up to use the POST method to send the data to the Flask server.

results.html:
The results.html file contains the HTML code for the results page. It includes two sections, one displaying the user's prompt and the other displaying the generated response. The page is styled using a CSS stylesheet.

Styling:
The application includes two CSS stylesheets, style.css and style1.css, which are used to style the home page and the results page, respectively. The stylesheets use a combination of custom styles and the Roboto font from Google Fonts.
Installation:
Download all the files and acess Your OPENAI API KEY from platform.openai.com and copy that API key and set a environment variable if you are in mac use export OPENAI_API_KEY=your_secret_key if you are in windows use $env:OPENAI_API_KEY="your_api_key" to run the program successfully.
Conclusion:
The ChatGPT Integration is a simple application that demonstrates the capabilities of the OpenAI GPT-3 model. The application can be easily modified and extended to suit different use cases and requirements.

IMPORTANT NOTE:
You must need your chatGPT API key to use this app to work as expected. I didn't use my API KEY because of reached maximum Free limits.
