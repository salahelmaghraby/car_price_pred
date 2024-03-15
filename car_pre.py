import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
import pickle
df = pd.read_csv("cleaned_data.csv")
pages = st.sidebar.radio("Select Page", ["Learn About data", "Descriptive Statistics", "Analysis" , "Model"])
if pages == "Learn About data":
    def main():
        st.header('Learn About data')
        st.image("OIP.jpg")
        st.header("Used Car Price prediction")
        st.write("""In the ever-evolving automotive landscape, the market for used cars is expanding rapidly, driven by factors such as economic considerations, changing consumer preferences, and a desire for sustainability. As consumers increasingly turn to the pre-owned car market, the need for accurate and transparent pricing information becomes paramount. The Used Car Price Prediction project seeks to address this need by employing cutting-edge machine learning techniques to forecast the prices of used cars based on a myriad of influencing factors.""")
        st.header("Data Columns")
        st.write("""Price:The target variable, representing the resale price of the used car. This is the primary value we aim to predict using machine learning models based on other features.
Color:The color of the car, which can significantly impact its perceived value in the resale market. Certain colors may be more popular or desirable, influencing the pricing dynamics.

Mileage:The distance the car has traveled, a crucial factor in determining its wear and tear. Higher mileage often correlates with a lower resale value, as it indicates more extensive usage.

Make:The manufacturer or brand of the car. Different brands may have varying reputations for reliability and durability, affecting the perceived value in the used car market.

Model:The specific model of the car, providing details about its features, specifications, and market segment. The model plays a key role in determining the resale price.

City:The city where the car is located or was previously used. Regional preferences, market demand, and local economic factors can influence used car prices.

Automatic Transmission:A binary indicator (Yes/No) representing whether the car has an automatic transmission. Automatic transmissions can impact resale values based on buyer preferences.

Air Conditioner:A binary indicator representing the presence of an air conditioner. Comfort features like air conditioning can influence the perceived value of a used car.

Power Steering:A binary indicator representing the presence of power steering. Power steering is considered a convenience feature and may affect the resale price.

Remote Control:A binary indicator representing the presence of remote control features, such as keyless entry. Modern convenience features can contribute to a higher resale value.

Year:The manufacturing year of the car. Newer cars often command higher prices in the used car market due to factors like technology upgrades and overall condition.

Full Option:A categorical variable indicating whether the car is classified as a "full option" vehicle. Full-option cars typically include a wide range of features and accessories, potentially impacting resale values.

Understanding the nuances of these columns is essential for developing a comprehensive used car price prediction model. By leveraging advanced machine learning techniques, this project aims to provide an accurate and valuable tool for both buyers and sellers navigating the intricate world of pre-owned vehicle transactions. """)
    if __name__ == "__main__":
        main()
if pages == "Descriptive Statistics":
    def main():
        tab1, tab2 = st.tabs(["Statistics For Categorical", "Statistics For Numerical "])
        with tab1:
            st.dataframe(df.describe(include="O"))
            st.header("Value Counts For Each Categorical Column")
            categoricals = df.describe(include="O").columns
            for cat in categoricals:
                st.write(f"Value Counts For {cat} :")
                dff = pd.DataFrame(df[cat].value_counts())
                dff.reset_index(inplace=True)
                dff.rename(columns={"index":cat,cat:f"count of {cat}"}, inplace=True)
                st.dataframe(dff)
        with tab2:
            st.dataframe(df.describe())
            st.header("Value Counts For Each Numerical Column")
            numericals = df.describe().columns
            for num in numericals:
                dff = pd.DataFrame(df[num].value_counts())
                dff.reset_index(inplace=True)
                dff.rename(columns={"index":num,num:f"count of {num}"}, inplace=True)
                st.dataframe(dff)
    if __name__ == "__main__":
        main()
if pages == "Analysis":
    def main():
        tab1, tab2 = st.tabs(["Uni-Variate Analysis", "Bi-Variate Analysis"])
        with tab1:
            st.header("Uni-Variate Analysis")
            st.image("vs.png")
            st.header("what is the range of prices ?")
            fig = px.histogram(df, x=df["Price"])
            st.plotly_chart(fig)
            st.header("what is the most frequancy prices ?")
            dff_price = df.groupby("Price")["Color"].count().sort_values(ascending = False).reset_index()
            dff_price.rename(columns={"Color":"count of price"}, inplace=True)
            fig = px.histogram(dff_price, x=dff_price["Price"].head(35), y=dff_price["count of price"].head(35), color_discrete_sequence=px.colors.qualitative.Dark24)
            fig.update_layout(xaxis_title_text='', yaxis_title_text="count of price", bargap = 0.2)
            st.plotly_chart(fig)
            st.header("what is the top colors ?")
            dff_color = df.groupby("Color")["Price"].count().sort_values(ascending = False).reset_index()
            dff_color.rename(columns={"Price":"count of color"}, inplace=True)
            fig = px.histogram(dff_color, x=dff_color["Color"].head(25), y=dff_color["count of color"].head(25), color_discrete_sequence=px.colors.qualitative.Dark24)
            fig.update_layout(xaxis_title_text='', yaxis_title_text='Count Of color',bargap = 0.2)
            st.plotly_chart(fig)
            st.header("what is the range of mileage ?")
            fig = px.histogram(df, x=df["Mileage"])
            st.plotly_chart(fig)
            st.header("what are the top brands ?")
            dff_make = df.groupby("Make")["Color"].count().sort_values(ascending = False).reset_index()
            dff_make.rename(columns={"Color":"count of Brand"}, inplace=True)
            fig = px.histogram(dff_make, x=dff_make["Make"].head(25), y=dff_make["count of Brand"].head(25), color_discrete_sequence=px.colors.qualitative.Dark24)
            fig.update_layout(xaxis_title_text='', yaxis_title_text='Count Of brand')
            st.plotly_chart(fig)
            st.header("what are the top Models ?")
            dff_model = df.groupby("Model")["Color"].count().sort_values(ascending = False).reset_index()
            dff_model.rename(columns={"Color":"count of model"}, inplace=True)
            fig = px.histogram(dff_make, x=dff_model["Model"].head(25), y=dff_model["count of model"].head(25), color_discrete_sequence=px.colors.qualitative.Dark24)
            fig.update_layout(xaxis_title_text='', yaxis_title_text='Count Of model')
            st.plotly_chart(fig)
            st.header("what are the top cities ?")
            dff_city = df.groupby("City")["Color"].count().sort_values(ascending = False).reset_index()
            dff_city.rename(columns={"Color":"count of city"}, inplace=True)
            fig = px.histogram(dff_city, x=dff_city["City"].head(25), y=dff_city["count of city"].head(25), color_discrete_sequence=px.colors.qualitative.Dark24)
            fig.update_layout(xaxis_title_text='', yaxis_title_text='Count Of city')
            st.plotly_chart(fig)
            st.header("is most cars have Automatic Transmission ?")
            at_pie = df["Automatic Transmission"].value_counts()
            fig = px.pie(names=at_pie.index, values=at_pie.values,)
            st.plotly_chart(fig)
            st.header(" is most cars have Air Conditioner ?")
            ar_pie = df["Air Conditioner"].value_counts()
            fig = px.pie(names=ar_pie.index, values=ar_pie.values)
            st.plotly_chart(fig)
            st.header(" is most cars have Power Steering ?")
            ps_pie = df["Power Steering"].value_counts()
            fig = px.pie(names=ps_pie.index, values=ps_pie.values)
            st.plotly_chart(fig)
            st.header("is most cars have Remote Control ?")
            rc_pie = df["Remote Control"].value_counts()
            fig = px.pie(names=rc_pie.index, values=rc_pie.values)
            st.plotly_chart(fig)
            st.header("is most cars have full option ?")
            fo_pie = df["full_option"].value_counts()
            fig = px.pie(names=fo_pie.index, values=fo_pie.values)
            st.plotly_chart(fig)
        with tab2:
            st.header("Bi-Variate Analysis")
            st.image("vs.png")
            st.header("Is the price affected by Mileage ?")
            fig = px.scatter(df ,x=df["Price"] ,y=df["Mileage"])
            st.plotly_chart(fig)
            dff_year_by_price = df.groupby('year')['Price'].mean().reset_index().sort_values(by='Price',ascending=False)
            st.header("Is There A Relation Between Price And Car Model ?")
            fig = px.line(dff_year_by_price  ,y=dff_year_by_price ["Price"] ,x=dff_year_by_price ["year"])
            st.plotly_chart(fig)
            st.header("are most cars haveAutomatic Transmission have also Air Conditioner ?")
            fig = px.histogram(df ,x=df["Automatic Transmission"] ,color=df["Air Conditioner"] ,color_discrete_sequence=["rgb(55,126,184)", "rgb(228,26,28)"], barmode="group" )
            fig.update_layout(xaxis_title_text='Automatic Transmission And Air Conditioner')
            st.plotly_chart(fig)
            st.header("are most cars have Power Steering have also Remote Control ?")
            fig = px.histogram(df ,x=df["Power Steering"] ,color=df["Remote Control"] ,color_discrete_sequence=["rgb(55,126,184)", "rgb(228,26,28)"], barmode="group" )
            fig.update_layout(xaxis_title_text='Power Steering And Remote Control')
            st.plotly_chart(fig)
    if __name__ == "__main__":
        main()
if pages == "Model":
    def main():
        st.title('Car Price Prediction\n')
        pipeline = pickle.load(open('pipeline.pkl', 'rb'))
        make = st.selectbox('Make', df['Make'].unique())
        filtered_df = df[df['Make'] == make]
        car_model = st.selectbox('Select Model', filtered_df['Model'].unique())
        color = st.selectbox('Select Color', filtered_df['Color'].unique())
        city = st.selectbox('Select City', filtered_df['City'].unique())
        milage = st.number_input('Enter Milage', df.Mileage.min(), df.Mileage.max())
        year = st.selectbox('year', filtered_df['year'].unique())
        auto_transmission = st.selectbox('Automatic Transmission', df['Automatic Transmission'].unique())
        air_conditioner = st.selectbox('Air Conditioner', df['Air Conditioner'].unique())
        power_steering = st.selectbox('Power Steering', df['Power Steering'].unique())
        remote_control = st.selectbox('Remote Control', df['Remote Control'].unique())
        full_option = st.selectbox('full_option', df['full_option'].unique())
        car_category = st.selectbox('Select Car Category', filtered_df['Car Category'].unique())
        new_data = {'Color': color, 'Mileage': milage, 'Make': make,"Model" :car_model  ,'City': city, 'Automatic Transmission': auto_transmission,
                 'Air Conditioner': air_conditioner, 'Power Steering': power_steering, 'Remote Control': remote_control, 'year': year,"full_option" : full_option, "Car Category": car_category}
        new_data = pd.DataFrame(new_data, index=[0])
        price = pipeline.predict(new_data)
        if st.button('Predict'):
            st.markdown('# Price in EGP:')
            st.markdown(int(price))
    if __name__ == "__main__":
        main()
