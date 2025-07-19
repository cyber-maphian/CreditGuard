import streamlit as st
import pandas as pd
import joblib
from datetime import datetime

st.set_page_config(
    page_icon="💰",
    page_title="CreditGuard",
    initial_sidebar_state="expanded"
)


st.subheader(":red[CreditGuard]")
st.markdown('Vench:red[Funds] Credit Risk Analyzer.')

default,credit_worthiness,amount_,dataset,about = st.tabs(['Default Rate',"Credit Worthiness",'Amount Prediction',"Dataset","About"])

with default:
    try:
        st.markdown(":red[Predict default rate of applicant.]")
        with st.form(key='form',clear_on_submit=False): 
            age = st.number_input("Applicant's Age",min_value=18,max_value=100)
            occupation = st.selectbox("Applicant's Occupation",options=["Student","Small business/artisan","Employed"])
            amount = st.number_input("Loan Amount",min_value=1000,max_value=200000)
            month  = st.selectbox("Loan duration (months)",options=['1 month','2 months','3 months']) 
            late = st.slider("On a scale of (0-100), how late does this applicant repay.",min_value=0,max_value=100,value=50)
            application = st.slider("On a scale of (0-100), how frequently does this applicant request for loan.",min_value=0,max_value=100,value=50)
            previous = st.slider("On a scale of (0-100), have this applicant defaulted before.",min_value=0,max_value=100,value=50)
            interest = st.number_input("Interest rate.",min_value=20,max_value=60)
            payday = st.selectbox("Pay back day (0: first 15 days of the month, 1: otherwise.)",[0,1])
            dayofmonth = st.date_input("day of the month",disabled=True)
            submit = st.form_submit_button('Analyze',icon="⚔️")

            
            if submit:
                if int(age) >= 18:
                    date_string = str(dayofmonth)
                    date_object =datetime.strptime(date_string,"%Y-%m-%d")
                    day_of_the_month = date_object.day
                    dayofmonth = day_of_the_month
                    map_occupation = {"Student":0,"Small business/artisan":1,"Employed":2}
                    occupation = map_occupation[occupation]
                    map_month = {'1 month':1,'2 months':2,'3 months':3}
                    month = map_month[month]
                        
                    features = [int(age),int(occupation),int(amount),int(month),int(late),int(application),int(previous),int(interest),int(payday),int(dayofmonth)]
                    #print(f"age:{age},occupation:{occupation},amount:{amount},month:{month},late:{late},application:{application},previous:{previous},interest:{interest},payday:{payday},dayofmonth:{dayofmonth}")
                    model = joblib.load("default_loan_prediction_model")
                    prediction = model.predict([features])

                    if int(dayofmonth) >=25 and int(occupation)==2:
                        if prediction < 50:
                            output = float(prediction)
                            st.subheader(f"Default Rate: :green[{output}%]")
                            adjust = prediction - 10
                            adjust = float(adjust)
                            if adjust >50:
                                st.subheader(f"Adjusted Default Rate: :red[{adjust}%]")
                            else:
                                st.subheader(f"Adjusted Default Rate: :green[{adjust}%]")

                            
                        else:
                            output = float(prediction)
                            st.subheader(f"Default Rate: :red[{output}%]")
                            adjust = prediction - 10
                            adjust = float(adjust)
                            if adjust > 50:
                                st.subheader(f"Adjusted Default Rate: :red[{adjust}%]")
                            else:
                                st.subheader(f"Adjusted Default Rate: :green[{adjust}%]")
                            

                    else:
                        if prediction < 50:
                            output = float(prediction)
                            st.subheader(f"Default Rate: :green[{output}%]")
                            
                        else:
                            output = float(prediction)
                            st.subheader(f"Default Rate: :red[{output}%]")
                else:
                        st.error("Error occured 'age must be greater then or equal to 18'",icon="🚨")                
    except:
        st.error("Error occured 'either an empty field or string value'",icon="🚨")      



            #st.metric("Default Rate",output,"1.2%")
with dataset:
    try:
        st.markdown(":red[We trained this model on the following real word dataset.]")
        data = pd.read_csv("loan_dataset.csv")
        data = st.dataframe(data)
    except:
            st.error("Error occured 'either an empty field or string value'",icon="🚨")    


with credit_worthiness:
    try:
        st.markdown(" :red[Predict loan applicant's credit worthiness.]")
        with st.form(key='credit_score_form',clear_on_submit=False):
            age = st.number_input("Applicant's Age",min_value=18,max_value=100)
            occupation = st.selectbox("Applicant's Occupation",options=["Student","Small business/artisan","Employed"])
            amount = st.number_input("Loan Amount",min_value=1000,max_value=200000)
            month  = st.selectbox("Loan duration (months)",options=['1 month','2 months','3 months']) 
            late = st.slider("On a scale of (0-100), how late does this applicant repay.",min_value=0,max_value=100,value=50)
            application = st.slider("On a scale of (0-100), how frequently does this applicant request for loan.",min_value=0,max_value=100,value=50)
            previous = st.slider("On a scale of (0-100), have this applicant defaulted before.",min_value=0,max_value=100,value=50)
            interest = st.number_input("Interest rate.",min_value=20,max_value=60)
            payday = st.selectbox("Pay back day (0: first 15 days of the month, 1: otherwise.)",[0,1])
            dayofmonth = st.date_input("day of the month",disabled=True)
            submit = st.form_submit_button('Analyze',icon="⚔️")

            if submit:
                date_string = str(dayofmonth)
                date_object =datetime.strptime(date_string,"%Y-%m-%d")
                day_of_the_month = date_object.day
                dayofmonth = day_of_the_month
                if int(age) >= 18:
                    map_occupation = {"Student":0,"Small business/artisan":1,"Employed":2}
                    occupation = map_occupation[occupation]
                    map_month = {'1 month':1,'2 months':2,'3 months':3}
                    month = map_month[month]
                        
                    features = [int(age),int(occupation),int(amount),int(month),int(late),int(application),int(previous),int(interest),int(payday),int(dayofmonth)]
                    #print(f"age:{age},occupation:{occupation},amount:{amount},month:{month},late:{late},application:{application},previous:{previous},interest:{interest},payday:{payday},dayofmonth:{dayofmonth}")
                    model = joblib.load("default_loan_prediction_model")
                    prediction = model.predict([features])

                    credit_score = 100 - prediction
                    if credit_score > 50:
                        st.subheader(f"Credit Worthy: :green[{credit_score}]")

                    else:
                        st.subheader(f"Credit Worthy: :red[{credit_score}]")


                
                else:
                    st.error("Error occured 'age must be greater then or equal to 18'",icon="🚨")
    except:
            st.error("Error occured 'either an empty field or string value'",icon="🚨")
with amount_:
    try:
        st.markdown(":red[Predict the amount an applicant should get.]")    
        #amount_prediction_model
        with st.form("amount_form"):
            age = st.number_input("Applicant's Age",min_value=18,max_value=100)
            occupation = st.selectbox("Applicant's Occupation",options=["Student","Small business/artisan","Employed"])
            previous = st.slider("On a scale of (0-100), have this applicant defaulted before.",min_value=0,max_value=100,value=50)
            application = st.slider("On a scale of (0-100), how frequently does this applicant request for loan.",min_value=0,max_value=100,value=50)
            interest = st.number_input("Interest rate.",min_value=20,max_value=60,disabled=True)
            days_ = st.selectbox("How long do you plan to hold the money for", options=["15 Days","30 Days"])
            payday = st.selectbox("Pay back day (0: first 15 days of the month, 1: otherwise.)",[0,1])
            dayofmonth = st.date_input("day of the month",disabled=True)#number_input("Day of the month",min_value=0,max_value=31)
            submit = st.form_submit_button("Analyze",icon="⚔️")

            if submit:
                date_string = str(dayofmonth)
                date_object =datetime.strptime(date_string,"%Y-%m-%d")
                day_of_the_month = date_object.day
                dayofmonth = day_of_the_month
                #DAY OF HOLDING
                maped = {"15 Days":15,"30 Days":30}
                days_ = maped[days_]
                #days of holding.
                if int(age) >= 18:
                    map_occupation = {"Student":0,"Small business/artisan":1,"Employed":2}
                    occupation = map_occupation[occupation]

                    features = [int(age),int(occupation),int(previous),int(dayofmonth),int(application),int(interest),int(payday)]
                    model = joblib.load('amount_prediction_model')
                    prediction = model.predict([features])
                    prediction = int(prediction)
                #optimization and thresh hold technique
                    if occupation == 0 and prediction >20000:
                          if days_ == 30:
                            money = 20000
                            repay = (20000 * 0.2) + money
                            st.subheader(f"Amount: :green[N{money}]")
                            st.subheader(f"Repayment: :green[N{repay}]")
                          else:
                                money = 20000
                                repay = (20000 * 0.1) + money
                                st.subheader(f"Amount: :green[N{money}]")
                                st.subheader(f"Repayment: :green[N{repay}]")
                                  
                    elif  "-" in str(prediction):
                         st.subheader(f"Amount: :green[N0]")  
                         
                    elif occupation == 1:
                         if previous <=20 and application >=60:
                                if days_ == 30:
                                    money = 150000
                                    repay = (150000 * 0.2) + money
                                    st.subheader(f"Amount: :green[N{money}]")
                                    st.subheader(f"Repayment: :green[N{repay}]")
                                else:
                                     money = 20000
                                     repay = (20000 * 0.1) + money
                                     st.subheader(f"Amount: :green[N{money}]")
                                     st.subheader(f"Repayment: :green[N{repay}]")    

                         elif previous <=30 and application >=50:
                                if days_ == 30:
                                    money = 100000
                                    repay = (100000 * 0.2) + money
                                    st.subheader(f"Amount: :green[N100000]")
                                    st.subheader(f"Repayment: :green[N{repay}]")
                                else:
                                     money = 100000
                                     repay = (100000 * 0.1) + money
                                     st.subheader(f"Amount: :green[N100000]")
                                     st.subheader(f"Repayment: :green[N{repay}]") 

                         else:
                                if days_ == 30: 
                                    prediction = prediction
                                    repay = (prediction * 0.2) + prediction
                                    st.subheader(f"Amount: :green[N{prediction}]")
                                    st.subheader(f"Repayment: :green[N{repay}]")   
                                else:
                                     prediction = prediction
                                     repay = (prediction * 0.1) + prediction
                                     st.subheader(f"Amount: :green[N{prediction}]")
                                     st.subheader(f"Repayment: :green[N{repay}]") 
                                                                      
                    else:
                        if days_ == 30:   
                            prediction = prediction
                            repay = (prediction * 0.2) + prediction
                            st.subheader(f"Amount: :green[N{prediction}]")
                            st.subheader(f"Repayment: :green[N{repay}]")
                        else:   
                            prediction = prediction
                            repay = (prediction * 0.1) + prediction
                            st.subheader(f"Amount: :green[N{prediction}]")
                            st.subheader(f"Repayment: :green[N{repay}]")         



                else:
                    st.error("Error occured 'age must be greater then or equal to 18'",icon="🚨")    
            #Age,Occupation,Previous_default_%,Day_of_month,Loan_application_%,Interest_rate_%,Payday_indicator,Amount
    except:
            st.error("Error occured 'either an empty field or string value'",icon="🚨")

with about:
    try:
        st.markdown(":red[About this application software.]")
        text = ("""
                :red[CreditGuard] is a cutting-edge software solution designed to empower financial 
                lenders with data-driven insights to make informed lending decisions. Leveraging the
                 power of machine learning, CreaditGuard helps lenders predict an individual's default
                 rate, credit worthiness, and optimal loan amount, ensuring a more secure and efficient 
                lending process.
                <p></p>
                At VenchFund our lending company, we pride ourselves on providing responsible and informed lending practices.
                 As part of our commitment to prudent lending, we utilize our proprietary software, CreaditGuard, to assess 
                the credit worthiness of loan applicants. This advanced tool enables us to make more accurate lending decisions,
                ensuring that we provide loans to individuals who are likely to repay them.
                <p></p>
                CreaditGuard uses sophisticated machine learning algorithms to evaluate an applicant's credit profile, taking into account various factors such as credit history, and employment status.
                This analysis generates three key metrics that inform our lending decisions:
                <p></p>
                <p> <span style="color:red">Default Rate :</span> This metric represents the likelihood of an applicant defaulting on their loan payments. A lower default rate indicates a lower risk of default.</p>
                <p> <span style="color:red">Credit Worthiness:</span> This assessment evaluates an applicant's overall credit profile, considering factors such as payment history, credit utilization, and credit age. A higher credit worthiness score indicates a more reliable borrower.</p>
                <p> <span style="color:red">Adjusted Default Rate:</span> For employed applicants whose repayment date falls between the 25th and 30th of the month, we apply an adjusted default rate. This adjustment reflects the increased likelihood of repayment during this period, as applicants are likely to receive their salaries and make timely payments.</p>

                <p>How we offer loan at VenchFunds:</p>
                <li>Student: N20,000</li>
                <li>Small scale business/artisan:N50,000-N150,000</li>
                <li>Employed:N30,000-100,000</li>

                <p>Software Accuracy:</p>
                While CreaditGuard achieved 90% accuracy during training, we recognize that perfection is the goal, and by combining our software with human analyst expertise, we strive to achieve 100%
                 accuracy in credit assessments.


        """)
        st.markdown(text,unsafe_allow_html=True)
    except:
            st.error("Error occured 'either an empty field or string value'",icon="🚨")    