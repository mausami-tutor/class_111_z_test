import pandas as pd
import statistics
import plotly.figure_factory as ff
import random
import plotly.graph_objects as go


df=pd.read_csv("studentMarks.csv")
data=df["Math_score"].tolist()



def show_fig(mean_list):
    df=mean_list
    mean=statistics.mean(df)
    fig=ff.create_distplot([df], ["Math Score"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0,0.20], mode="lines",name="MEAN"))
    
    fig.show()


def random_set_of_mean(counter):
    sample_data=[]
    for i in range(0, counter):
        random_index=random.randint(0, len(data)-1)
        value=data[random_index]
        sample_data.append(value)

    mean=statistics.mean(sample_data)
    return mean

def setup():
    mean_list=[]
    for i in range (0,1000):
        set_of_means=random_set_of_mean(100)
        mean_list.append(set_of_means)
    
    final_mean=statistics.mean(mean_list)
    print("The mean of samples is: ",final_mean)
    final_stdev=statistics.stdev(mean_list)
    print("The std dev of samples is: ", final_stdev)

    first_std_dev_start, first_std_dev_end= final_mean-final_stdev, final_mean+final_stdev
    second_std_dev_start, second_std_dev_end= final_mean-(2*final_stdev), final_mean+(2*final_stdev)
    third_std_dev_start, third_std_dev_end= final_mean-(3*final_stdev), final_mean+(3*final_stdev)
    
    fig=ff.create_distplot([mean_list], ["Math Score"], show_hist=False)
    #fig.add_trace(go.Scatter(x=[final_mean,final_mean], y=[0,0.2], mode="lines",name="MEAN"))

    df1= pd.read_csv("data1.csv")
    data1=df1["Math_score"].tolist()
    mean_of_sample1=statistics.mean(data1)

    df2= pd.read_csv("data2.csv")
    data2=df2["Math_score"].tolist()
    mean_of_sample2=statistics.mean(data2)

    df3= pd.read_csv("data3.csv")
    data3=df3["Math_score"].tolist()
    mean_of_sample3=statistics.mean(data3)

    fig.add_trace(go.Scatter(x=[mean_of_sample1, mean_of_sample1], y=[0,0.2], mode="lines", name= "Mean of sample 1"))
    
    fig.add_trace(go.Scatter(x=[mean_of_sample2, mean_of_sample2], y=[0,0.2], mode="lines", name= "Mean of sample 2"))

    fig.add_trace(go.Scatter(x=[mean_of_sample3, mean_of_sample3], y=[0,0.2], mode="lines", name= "Mean of sample 3"))

    fig.add_trace(go.Scatter(x=[first_std_dev_start, first_std_dev_start], y=[0,0.2], mode="lines", name="First Std deviation start"))
    fig.add_trace(go.Scatter(x=[first_std_dev_end, first_std_dev_end], y=[0,0.2], mode="lines", name="First Std deviation end"))
    # fig.add_trace(go.Scatter(x=[second_std_dev_start, second_std_dev_start], y=[0,0.2], mode="lines", name="Second Std deviation start"))
    fig.add_trace(go.Scatter(x=[second_std_dev_end, second_std_dev_end], y=[0,0.2], mode="lines", name="Second Std deviation end"))
    # fig.add_trace(go.Scatter(x=[third_std_dev_start, third_std_dev_start], y=[0,0.2], mode="lines", name="Third Std deviation start"))
    fig.add_trace(go.Scatter(x=[third_std_dev_end, third_std_dev_end], y=[0,0.2], mode="lines", name="Third Std deviation end"))
    fig.show()
    
setup()