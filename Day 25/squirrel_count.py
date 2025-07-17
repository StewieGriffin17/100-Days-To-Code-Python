import pandas

data = pandas.read_csv("/content/sample_data/Squirrel_Data.csv")

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"]) 
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"]) 
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])  

data_dist = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dist)
df.to_csv("squirrel_count.csv")