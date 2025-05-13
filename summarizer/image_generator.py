import os
import requests

def generate_image(summary, output_path='static/images/summary.png'):
    os.makedirs('static/images', exist_ok=True)

    # Replace 'your_api_key' with your actual DeepAI API key
    api_key = os.getenv('DEEPAI_API_KEY') or 'your_api_key'
    api_url = 'https://api.deepai.org/api/text2img'

    headers = {
        'api-key': api_key
    }

    data = {
        'text': summary
    }

    try:
        response = requests.post(api_url, data=data, headers=headers)
        response.raise_for_status()
        image_url = response.json().get('output_url')

        if image_url:
            image_response = requests.get(image_url, stream=True)
            image_response.raise_for_status()
            with open(output_path, 'wb') as out_file:
                for chunk in image_response.iter_content(chunk_size=8192):
                    out_file.write(chunk)
            return output_path
        else:
            print("No image URL returned by the API.")
            return ""
    except requests.exceptions.RequestException as e:
        print(f"Error generating image: {e}")
        return ""
    

