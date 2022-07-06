# import the requests module for interacting with web
import requests

# define the url of the image
image_url = "https://www.google.com/search?q=docker&sxsrf=ALiCzsaW4Y0l9RS4IqJqtC0pJMhnN9CeXw:1657095690551&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjZzfm_6uP4AhWkTmwGHXV_Du4Q_AUoAXoECAIQAw&biw=1846&bih=984&dpr=1#imgrc=aa-fGYlRTuYwAM"

# define the image filename
image_filename = "image1.png"

# define HTTP headers
http_headers = {"User-Agent" : "Chrome/51.0.2704.103"}

# creating a function to download any image using it's url.
def download_image(url, file_name, headers):

    # send a GET request
    response = requests.get(url, headers=headers)

    # save the image
    if response.status_code == 200:
        with open(file_name, "wb") as file_write:
            file_write.write(response.content)
    else:
        print(response.status_code)

# download image

download_image(image_url, image_filename, http_headers)