import pandas as pd
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go
import random

df1=pd.read_csv("school1.csv")
data1= df1["Math_score"].tolist()
df1_sample=pd.read_csv("school_1_sample.csv")
data_1_sample=df1_sample["Math_score"].tolist()

df2=pd.read_csv("school2.csv")
data2= df2["Math_score"].tolist()
df2_sample=pd.read_csv("school_2_sample.csv")
data_2_sample=df2_sample["Math_score"].tolist()

df3=pd.read_csv("school3.csv")
data3= df3["Math_score"].tolist()
df3_sample=pd.read_csv("school_3_sample.csv")
data_3_sample=df3_sample["Math_score"].tolist()

school1_mean=statistics.mean(data1)
school1_stdev=statistics.stdev(data1)
print("The mean and standard deviation fro school 1 are {} and {}: ".format
(school1_mean,school1_stdev)) 
school1_mean_sample=statistics.mean(data_1_sample)

school2_mean=statistics.mean(data2)
school2_stdev=statistics.stdev(data2)
print("The mean and standard deviation for school 2 are {} and {}: ".format(school2_mean,school2_stdev)) 
school2_mean_sample=statistics.mean(data_2_sample)

school3_mean=statistics.mean(data3)
school3_stdev=statistics.stdev(data3)
print("The mean and standard deviation for school 3 are {} and {}: ".format(school3_mean,school3_stdev)) 
school3_mean_sample=statistics.mean(data_3_sample)


def random_set_of_mean(counter,data):
    sample_data=[]
    for i in range(0, counter):
        random_index=random.randint(0, len(data)-1)
        value=data[random_index]
        sample_data.append(value)

    mean=statistics.mean(sample_data)
    return mean

def setup(data):
    mean_list=[]
    for i in range (0,1000):
        set_of_means=random_set_of_mean(100,data )
        mean_list.append(set_of_means)

    pop_mean= statistics.mean(data)
    pop_std_dev=statistics.stdev(data)    
    final_mean=statistics.mean(mean_list)
    print("The mean of samples is: ",final_mean)
    final_stdev=statistics.stdev(mean_list)
    print("The std dev of samples is: ", final_stdev)

    zscore=(school3_mean_sample-final_mean)/final_stdev
    print("The zscore for school {} is {}:".format(2, zscore))

    first_std_dev_start, first_std_dev_end= final_mean-final_stdev, final_mean+final_stdev
    second_std_dev_start, second_std_dev_end= final_mean-(2*final_stdev), final_mean+(2*final_stdev)
    third_std_dev_start, third_std_dev_end= final_mean-(3*final_stdev), final_mean+(3*final_stdev)
    

    fig=ff.create_distplot([mean_list],["Math Scores"], show_hist=False)
    fig.add_trace(go.Scatter(x=[final_mean, final_mean], y=[0,0.15], mode="lines", name="MEAN"))
    #fig.add_trace(go.Scatter(x=[first_std_dev_start, first_std_dev_start], y=[0,0.17], mode="lines", name="First Std deviation start"))
    fig.add_trace(go.Scatter(x=[first_std_dev_end, first_std_dev_end], y=[0,0.17], mode="lines", name="First Std deviation end"))
    #fig.add_trace(go.Scatter(x=[second_std_dev_start, second_std_dev_start], y=[0,0.17], mode="lines", name="Second Std deviation start"))
    fig.add_trace(go.Scatter(x=[second_std_dev_end, second_std_dev_end], y=[0,0.17], mode="lines", name="Second Std deviation end"))
    #fig.add_trace(go.Scatter(x=[third_std_dev_start, third_std_dev_start], y=[0,0.17], mode="lines", name="Third Std deviation start"))
    fig.add_trace(go.Scatter(x=[third_std_dev_end, third_std_dev_end], y=[0,0.17], mode="lines", name="Third Std deviation end"))
    fig.add_trace(go.Scatter(x=[school3_mean_sample, school3_mean_sample], y=[0, 0.15], mode="lines", name="Mean of samples after internevtion"))
    fig.show()

    

setup(data3)


