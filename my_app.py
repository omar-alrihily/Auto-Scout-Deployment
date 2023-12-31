import streamlit as st
import pickle
import pandas as pd
from sklearn.linear_model import Lasso
from git import Object


#title
st.title("CAR PRICE PREDICTION")

# images
from PIL import Image
im = Image.open("car.png")
st.image(im, width=500)


st.text("    ")

#pickles
model = pickle.load(open("final_model","rb"))
columns = pickle.load(open("columns", 'rb'))
final_scale = pickle.load(open("final_scale", 'rb'))


st.sidebar.header("*Enter the Features of Your Car*")

hp=st.sidebar.slider("What is the horsepower of your car",40,300,step=5)
age=st.sidebar.selectbox("What is the age of your car?",(0,1,2,3))
km = st.sidebar.slider("What is the km of your car?",0,100000,step=500)

make_model = st.sidebar.selectbox("Select model of your car", ('Audi A1', 'Audi A3',
                                                     'Opel Astra','Opel Corsa', 'Opel Insignia',
                                                     'Renault Clio','Renault Duster', 'Renault Espace'))





gearing_type = st.sidebar.selectbox("Select gearing type of your car", ('Automatic', 'Manual', 'Semi-automatic'))
gears = st.sidebar.selectbox("What is the gear of your car?",(5,6,7,8)) 

#data
my_dict = {
	"hp_kW": hp,	
    	"age": age,
    	"km": km,
    	"make_model": make_model,
	"Gearing_Type": gearing_type,
	"Gears": gears
}



df = pd.DataFrame([my_dict])
df = pd.get_dummies(df)
df = df.reindex(columns=columns, fill_value=0)
df = final_scale.transform(df)

#evaluation
if st.button("Predict", type="primary"):
    pred = model.predict(df)
    st.markdown("## *your car's estimated price is* €{}. ".format(int(pred)))
    

    


    