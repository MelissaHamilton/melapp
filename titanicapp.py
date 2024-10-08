import streamlit as st
import pickle



st.image('image.png')

pickle_in = open('titanicpickle.pkl', 'rb')
classifier = pickle.load(pickle_in)

#Defining the function which will make the prediction using the data the user will input
def Prediction(Pclass, Sex, Age, SibSp, Parch, Fare, Embarked):
    prediction = classifier.predict([[Pclass, Sex, Age, SibSp, Parch, Fare, Embarked]])
    print(prediction)
    return(prediction)

def main():
    st.title('Welcome to My Titanic Prediction App')
    #The following code creates the text boxes in which the user can enter the data.
    Pclass = st.text_input('Passenger Class')
    Sex = st.text_input('Sex')
    Age = st.text_input('Age')
    SibSp = st.text_input('Sibling')
    Parch = st.text_input('Parent/Child')
    Fare = st.text_input('Fare')
    Embarked = st.text_input('Embarked')
    result = ''
    if st.button('Predict'):
        #convert the input to appropriate data types
        Pclass = int(Pclass)
        
        Age = float(Age)
        SibSp = int(SibSp)
        Parch = int(Parch)
        Fare = float(Fare)
        result = Prediction(Pclass, Sex, Age, SibSp, Parch, Fare, Embarked)
    st.success(f'This output is: {result}')
main()
