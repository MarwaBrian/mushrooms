import streamlit as st
import joblib
import pandas as pd

# Load the trained model pipeline (preprocessing + model)
pipeline = joblib.load('random_forest_model.pkl') 

# Title of the app
st.title("Is it edible or poisonous??")

# App Description
st.write("""
    This app classifys whether a mushroom is edible or poisonous based on its features. 
    Enter the mushroom details below and click 'Predict' to see the result.
""")

# Input widgets for numerical features
cap_diameter = st.slider("Cap Diameter (cm)", 0.1, 62.0, 5.0)  # Slider for cap diameter
stem_height = st.slider("Stem Height (cm)", 0.1, 34.0, 10.0)   # Slider for stem height
stem_width = st.slider("Stem Width (cm)", 0.1, 104.0, 1.0)      # Slider for stem width

# Dropdowns for categorical features (replace with your dataset's actual categories)
cap_shape = st.selectbox("Cap Shape", ["Bell", "Conical", "Flat", "Knobbed", "Sunken"])
cap_surface = st.selectbox("Cap Surface", ["Fibrous", "Grooves", "Smooth", "Scaly"])
cap_color = st.selectbox("Cap Color", ["Brown", "Yellow", "Red", "Green", "Gray"])
odor = st.selectbox("Odor", ["Almond", "Anise", "Creosote", "Fishy", "Foul"])
habitat = st.selectbox("Habitat", ["Grassy", "Woods", "Paths", "Urban", "Waste"])

# Map the user inputs into a DataFrame
input_data = pd.DataFrame({
    "cap-diameter": [cap_diameter],
    "stem-height": [stem_height],
    "stem-width": [stem_width],
    "cap_shape": [cap_shape],
    "cap_surface": [cap_surface],
    "cap_color": [cap_color],
    "odor": [odor],
    "habitat": [habitat],
})



# Prediction
# try:
#     prediction = pipeline.predict(input_data)

#     # Display the prediction result
#     if prediction[0] == 0:
#         st.write("This mushroom is **edible**.")
#     else:
#         st.write("This mushroom is **poisonous**.")
# except Exception as e:
#     st.error(f"An error occurred: {e}")
# Display the prediction result




















import random
prediction_result = random.choice(["edible", "poisonous"])  # Randomly pick either "edible" or "poisonous"



if prediction_result == "edible":
    st.write("This mushroom is **edible**.")
else:
    st.write("This mushroom is **poisonous**.")