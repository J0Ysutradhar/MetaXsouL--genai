# MetaXsouL Generative AI

This project is a simple demo of MetaXsouL AI using Streamlit and Google's Generative AI. It allows users to ask questions and get answers from the AI model.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/J0Ysutradhar/MetaXsouL--genai.git
    cd MetaXsouL--genai
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    .\venv\Scripts\activate  # On Windows
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit app:
    ```sh
    streamlit run MetaXsouL.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

3. Enter your question in the text input field and click the "Ask" button to get a response from the AI model.

## Configuration

Make sure to replace the placeholder API key in [MetaXsouL.py](http://_vscodecontentref_/0) with your actual Google Generative AI API key:
```python
genai.configure(api_key="YOUR_API_KEY_HERE")
## OBB 
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
Contributions are welcome! Please open an issue or submit a pull request for any changes.

Acknowledgements
Streamlit
Google Generative AI
Contact
For any inquiries, please contact J0Ysutradhar.

Make sure to add a `requirements.txt` file with the necessary dependencies for your project.
Make sure to add a `requirements.txt` file with the necessary dependencies for your project.
