import streamlit as st

# set page config
st.set_page_config(page_title="Group 1 Data Science",
                   page_icon=":bar_chart:",
                   layout='centered',
                   initial_sidebar_state="auto")

# Display the title of the web app

# Display a subheader that indicates the author of the web apps, with a sunglasses emoji
st.write(':memo: By Group 1')

st.write('')
st.write('')
# Display a markdown bullet point with a emoji and a link to "AQI_Prediction" app
url = "./AQI_Prediction"
git_url = "https://github.com/markchweya/AQI-PREDICT"
st.subheader(":wind_blowing_face: [AQI Prediction App](%s)" % url,
             help = "Learn more about this app at my [github repository](%s)" % git_url)
# Display a markdown bullet point with a computer emoji and a link to app 2
#st.markdown('- **[:computer: App 2](./App_2)**')

# Display an empty line
st.text('')
# Display an image from the 'assets' folder named 'cover-page.gif'
#st.image('assets/cover-page.gif')
