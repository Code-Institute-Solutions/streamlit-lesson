import streamlit as st
st.write("Hello world!!!!")
st.write("---")





######### Learning Sections #########
# Display text
# Display data
# Display plots
# Optimize performance
# Display widgets 
# Display media


################################################################################
### Display text ###
################################################################################
# st.write("# This is a major section")  # use markdown to create headers and sub headers
# st.write("## This is subsection 1")
# st.write("* Here is content for subsection 1")
# st.write("## This is subsection 2")
# st.write("* Here is content for subsection 2")
# st.write("### This is sub-subsection 2") # you can play around by adding more sub-sections
# st.write("Here other content")
# st.info("* This is made with st.info()") # Display a text with informational style.
# st.success("* This is made with st.success()") # Display a text with success style.
# st.warning("* This is made with st.warning()") # Display a text with warning style.
# st.error("* This is made with st.error()") # Display a text with error style.
# st.write("---")  # creates a horizontal line, useful to separate the content in the page



################################################################################
### Display data ###
################################################################################
###### We will generate some data

# my_list = [10,50,409] # Python list
# my_dict = {'Number':[1,2,3], 'Color': ['Blue', 'Yellow', 'Green']} # python dictionary

##### we will use pandas and numpy to generate a DataFrame. 
##### For now, think of a DataFrame as a table with columns, rows and data.
# import numpy as np
# import pandas as pd 
# np.random.seed(1)
# df = pd.DataFrame(data={"Col1":np.random.randint(low=-100,high=100,size=10),
#                         "Col2":np.random.randint(low=25,high=80,size=10)
#                         })

# st.write("This is a list")
# st.write(my_list)
# st.write("This is a dict")
# st.write(my_dict)
# st.write("This is a DataFrame")
# st.write(df)
# st.write("Alternatively, you can display a DataFrame using st.table()")
# st.table(df)
# st.write('---')






################################################################################
### Display plots ###
################################################################################

##### We will use matplotlib, seaborn and plotly  for data visualization
##### for now, we just need to understand the plotting capability
##### the commands and their usability will come clear across the lessons and walkthrough project
##### we will use a generated DataFrame
# import numpy as np
# import pandas as pd 
# np.random.seed(1)
# df = pd.DataFrame(data={"Col1":np.random.randint(low=-100,high=100,size=10),
#                         "Col2":np.random.randint(low=25,high=80,size=10)
#                         })

#### and will plot the data
# import matplotlib.pyplot as plt
# import seaborn as sns  
# st.write("* Plot with Matplotlib/Seaborn") # we create a figure and plot the data
# sns.set_style("whitegrid")
# fig, axes = plt.subplots()
# sns.scatterplot(data=df, x='Col1', y='Col2', ax=axes)
# st.pyplot(fig) # When you render a Matplotlib or Seaborn plot, you wil use st.pyplot()
#                # for example, in a jupyter notebook, we render with plt.show()
#                # don't worry; we will see that in more detail soon 
# st.write("---")

# st.write("* This example uses Plotly - an interactive data visualization library")
# import plotly.express as px
# fig = px.scatter(data_frame=df, x='Col1', y='Col2',width=800,height=400)
# st.plotly_chart(fig) # When you render a Plotly plot, you wil use st.plotly_chart()
#                      # in a jupyter notebook, we render with plt.show() 
# st.write("---")





################################################################################
### Optimize performance ###
################################################################################

#### Currently, every time you reload the dashboard page so is the script
#### this may cause a delay in your app, i.e.: you may reload multiple time the same data 
#### to solve that, you can cache your data by adding a decorator @st.cache in a function that loads your data
#### in this example, you might not notice the speed difference, but in real applications, this difference is noticeable

# import numpy as np
# import pandas as pd 

# @st.cache
# def load_your_data():
#     np.random.seed(1)
#     df = pd.DataFrame(data={"Col1":np.random.randint(low=-100,high=100,size=10),
#                         "Col2":np.random.randint(low=25,high=80,size=10)
#                         })
#     return df

# df = load_your_data()
# st.write(df)




################################################################################
### Display widgets ###
################################################################################

##### Feel free to play around with all widgets options
# if st.button('Hit me'):  # if you click the button, it is True.
#     st.write("Oh, you did!")
# else:
#     st.write("Still waiting")
# st.write("---")

# if st.checkbox('Check me out'):
#     st.write("You are brave")
# else:
#     st.write("What are you waiting for?")
# st.write("---")

# st.radio(label='Radio button options', options=[1,2,3])
# st.write("---")

# st.selectbox(label='Select one single option', options=[1,2,3], key="1")
# st.write("---")

# st.multiselect(label='Select multiple options', options=[1,2,3])
# st.write("---")

# st.slider(label='Slide me', min_value=0, max_value=10)
# st.write("---")


# st.text_input(label='Enter some text')
# st.write("---")

# st.number_input(label='Enter a number')
# st.write("---")

# st.text_area(label='Area for textual entry')
# st.write("---")

# st.date_input(label='Date input')
# st.write("---")

# st.time_input('Time entry')
# st.write("---")

# st.file_uploader(label='File uploader')
# st.write("---")



#### You probably noticed there is not much value when you randomly create widgets
#### The idea is to assign them to a variable, and this variable is used to interact with the application
# option = st.selectbox(label='Pick one:', options=[1,2,3,'A'], key="2")
# st.write(f"* I see you selected {option}, and its type is {type(option)}")
# st.write("---")



#### you can create 'columns' (or split the row space) and assign multiple items/widgets
#### you should use st.beta_columns() and inform amount of columns
#### that will be assigned to individual variables, i.e.: if there were three columns, you would have col1, col2, col3
#### you will define the content on each variable with the command "with:"
#### this example prints a list in the first column and display a widget in the second column

# col1, col2 = st.beta_columns(2)
# with col1:
#     st.write([1,2,3])
# with col2:
#     option = st.selectbox(label='Pick one:', options=[1,2,3,'A'], key="3")

# st.write(f"* I see you selected {option}, and its type is {type(option)}")


################################################################################
### Display media ###
################################################################################


# st.image(image="https://static.streamlit.io/examples/cat.jpg",
#         caption='My first image', width=300)
# st.write("---")

# st.write("Some song to bring light to your day")
# st.audio(data="https://www2.cs.uic.edu/~i101/SoundFiles/StarWars60.wav",
#         start_time=0)
# st.write("---")   

# st.write("You probably have seen this video already :)")
# st.video(data="https://www.youtube.com/watch?v=4jzdvYBA--Q",
#         start_time=0)
# st.write("---")