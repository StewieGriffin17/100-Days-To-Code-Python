import colorgram

colors = colorgram.extract('image.jpg', 10)

color_list = []

for i in range(0, 10):
    color = colors[i]
    rgb = color.rgb
    color_list.append((rgb.r, rgb.g, rgb.b))

print(color_list)


# this code shows error in vs code but runs perfectly in PyCharm, can't figure out the issue. 😕
