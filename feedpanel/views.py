from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import admin,shop,googleshop,fbshop,yelpshop,category,reviewdata,aspectdata,pricing,shopaspectarchive
from django.db.models import F, Q, When
from django.db.models import Avg
import pandas as pd
import pickle

from datetime import datetime, date, timezone
import random



def home(request):
        
        return render(request,"loanprediction.html")





def aspect_analysis(request):
    train=pd.read_csv("File Name.csv")
    user_input=train
    user_input=user_input.drop(user_input.index) 
    user_input.loc[len(user_input.index)] = [5, 1, 1,0,0,50000,20000,50,1,1,480,1.32,0.08,0.004,0.009,0.0234,48904.675199,3.0,0.1] 


    gender2 = request.POST.get("gender")
    if gender2=="Male":
        model_gender2=0
    else:
        model_gender2=1

    Married = request.POST.get("Married")
    if Married=="Yes":
        model_Married=1
    else:
        model_Married=0


    Dependents = request.POST.get("Dependents")
    if Dependents=="0":
        model_Dependents=0
    elif Dependents=="1":
        model_Dependents=1
    elif Dependents=="2":
        model_Dependents=2
    else:
        model_Dependents=3



    Education = request.POST.get("Education")
    if Education=="Graduated":
        model_Education=1
    else:
        model_Education=0


    Self_Employed = request.POST.get("Self_Employed")
    if Self_Employed=="Yes":
        model_Self_Employed=1
    else:
        model_Self_Employed=0



    ApplicantIncome = request.POST.get("ApplicantIncome")
    CoapplicantIncome = request.POST.get("CoapplicantIncome")
    loanamount = request.POST.get("loanamount")
 
    Property_Area = request.POST.get("Property_Area")
    if Property_Area=="Semiurban":
        model_Property_Area=2
    elif Property_Area=="Rural":
        model_Property_Area=1
    else:
        model_Property_Area=0

    Loan_Amount_Term = request.POST.get("Loan_Amount_Term")
    
    

    user_input['Gender']= model_gender2               
    user_input['Married']=   model_Married         
    user_input['Dependents']=  model_Dependents           
    user_input['Education']=       model_Education       
    user_input['Self_Employed']=   model_Self_Employed      
    user_input['ApplicantIncome']=ApplicantIncome
    user_input['CoapplicantIncome']=  CoapplicantIncome
    user_input['LoanAmount']=    loanamount  
    user_input['Credit_History']=    0    
    user_input['Property_Area']=     model_Property_Area   
    user_input['Loan_Amount_Term']=Loan_Amount_Term 

    r=0.00833
    user_input['EMI']=user_input.apply(lambda x:(float(x['LoanAmount'])*r*((1+r)**float(x['Loan_Amount_Term'])))/
    ((1+r)**((float(x['Loan_Amount_Term']))-1)),axis=1)
    user_input['Dependents_EMI_mean']=user_input.groupby(['Dependents'])['EMI'].transform('mean')
    

    for i in [user_input]:
        i["TotalIncome"]=int(i["ApplicantIncome"])+int(i["CoapplicantIncome"])
    user_input['LoanAmount_Term_per_TotalIncome']=int(user_input['Loan_Amount_Term'])/int(user_input['TotalIncome'])
    


    user_input['EMI_per_Loan_Amount_Term']=float(user_input['EMI'])/float(user_input['Loan_Amount_Term'])
    user_input['EMI_per_LoanAmount']=float(user_input['EMI'])/float(user_input['LoanAmount'])
    

    user_input['LoanAmount_per_TotalIncome']=float(user_input['LoanAmount'])/float(user_input['TotalIncome'])
    user_input['Property_Area_LoanAmount_per_TotalIncome_mean']=user_input.groupby(['Property_Area'])['LoanAmount_per_TotalIncome'].transform('mean')

    user_input['Dependents_LoanAmount_Sum']=user_input.groupby(['Dependents'])['LoanAmount'].transform('sum')

    from sklearn.preprocessing import KBinsDiscretizer
    TotalIncome_discretizer = KBinsDiscretizer(n_bins=5, encode='ordinal', strategy='quantile')
    user_input[ 'TotalIncome_Bins'] = TotalIncome_discretizer.fit_transform(user_input['TotalIncome'].values.reshape(-1,1)).astype(float)

    Loan_Amount_Term_discretizer = KBinsDiscretizer(n_bins=5, encode='ordinal', strategy='quantile')
    user_input['Loan_Amount_Term_Bins'] = Loan_Amount_Term_discretizer.fit_transform(user_input['Loan_Amount_Term'].values.reshape(-1,1)).astype(float)



    user_input=user_input.drop(['TotalIncome'],axis=1)
    user_input=user_input.drop(['EMI'],axis=1)
    user_input=user_input.drop(['LoanAmount_per_TotalIncome'],axis=1)

   

    print("##########################",user_input)
    filename = 'finalized_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    result=loaded_model.predict(user_input)
    finalresult=result[0]

    return render(request,'loanprediction2.html',{"result":finalresult,
    "gender":gender2,
    "Married":Married,
       "Dependents":Dependents,
    "Education":Education,
       "Self_Employed":Self_Employed,
    "ApplicantIncome":ApplicantIncome,
       "CoapplicantIncome":CoapplicantIncome,
    "loanamount":loanamount,
    "Property_Area":Property_Area,
       "Loan_Amount_Term":Loan_Amount_Term
    
    })
    
