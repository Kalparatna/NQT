import threading
import requests

def download_image(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)
    print(f'Downloaded {filename}')

def main():
    image_urls = [
        "https://www.google.com/imgres?imgurl=https%3A%2F%2Fimages.pexels.com%2Fphotos%2F414612%2Fpexels-photo-414612.jpeg%3Fcs%3Dsrgb%26dl%3Dpexels-james-wheeler-414612.jpg%26fm%3Djpg&tbnid=0Yr2UV2AytexjM&vet=12ahUKEwixneCWp6GEAxUUu2MGHd2LB30QMygBegQIARB3..i&imgrefurl=https%3A%2F%2Fwww.pexels.com%2Fsearch%2Fbeautiful%2F&docid=B51x0PBR9KNzvM&w=5306&h=3770&q=images&ved=2ahUKEwixneCWp6GEAxUUu2MGHd2LB30QMygBegQIARB3",

        "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.freepik.com%2Ffree-photos-vectors%2Fbackground&psig=AOvVaw1LmNM63KPAoLf-7Qri9CvX&ust=1707672834371000&source=images&cd=vfe&opi=89978449&ved=0CBMQjRxqFwoTCMCdk5inoYQDFQAAAAAdAAAAABAE",

        "https://www.google.com/imgres?imgurl=https%3A%2F%2Fimages.pexels.com%2Fphotos%2F414612%2Fpexels-photo-414612.jpeg%3Fcs%3Dsrgb%26dl%3Dpexels-james-wheeler-414612.jpg%26fm%3Djpg&tbnid=0Yr2UV2AytexjM&vet=12ahUKEwixneCWp6GEAxUUu2MGHd2LB30QMygBegQIARB3..i&imgrefurl=https%3A%2F%2Fwww.pexels.com%2Fsearch%2Fbeautiful%2F&docid=B51x0PBR9KNzvM&w=5306&h=3770&q=images&ved=2ahUKEwixneCWp6GEAxUUu2MGHd2LB30QMygBegQIARB3"
    ]

    threads = []
    for i, url in enumerate(image_urls):
        filename = f"image_{i+1}.jpg"
        thread = threading.Thread(target=download_image, args=(url, filename))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print("All downloads completed!")

if __name__ == "__main__":
    main()
