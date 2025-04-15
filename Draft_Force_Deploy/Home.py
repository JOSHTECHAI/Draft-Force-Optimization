import streamlit as st
import base64

# Load background image
background_image_path = "Images/disc-plough-optimization-3.jpg"
with open(background_image_path, "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode()
    
# Load logo image
logo_image_path = "Images/draft_force_optimization_logo1.png"
with open(logo_image_path, "rb") as image_file:
    encoded_logo = base64.b64encode(image_file.read()).decode()

st.image("Images/draft_force_optimization_logo1.png")
# Define the HTML template with inline CSS for background and button
html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Optimization of Draft Force Demands of Disc Plough</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-image: url(data:image/jpg;base64,{encoded_image});
            background-size: contain;
            background-repeat: no-repeat;
            background-position: center;
            height: 100vh;
            width: 100vw;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .container {{
            width: 60%;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            background: rgba(255, 255, 255, 0.8);
            border-radius: 10px;
        }}
        .container h1 {{
            font-size: 24px;
            margin-bottom: 20px;
        }}
        .container button {{
            display: inline-block;
            background-color: #4CAF50;
            color: #ffffff;
            text-decoration: none;
            padding: 10px 20px;
            font-size: 16px;
            font-weight: bold;
            font-family: "Times New Roman";
            border: none;
            border-radius: 6px;
            cursor: pointer;
            transition: background-color 0.3s ease, transform 0.2s ease;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        .container button:hover {{
            background-color: #45a049;
            transform: scale(1.05);
            box-shadow: 0 6px 12px rgba(0,0,0,0.2);
        }}
    </style>
    <style>
    .bottom-text{{
        position:fixed;
        bottom:0;
        width:86%;
        background-color:#E2E2EC ;
        color:#45a049;               
        text-align:center;
        padding:10px;
        font-size:22px;
        z-index: 100;
        font-family: "Times New Roman", sans-serif;
        background: rgba(255, 255, 255, 0.75);
    }}
    </style>
</head>
<body>
    <div class="container">
        <h1>DRAFT FORCE DEMANDS OF DISC PLOUGH</h1>
    </div>  
</body>
</html>
"""

# Use Streamlit to render the HTML template
import streamlit.components.v1 as components
components.html(html_template, height=600)
def image():
  st.sidebar.image("Images/disc-plough-optimization-1.jpg")
  st.sidebar.image("Images/disc-plough-optimization-3.jpg")
  st.sidebar.image("Images/disc-plough-optimization-2.jpg")

image()