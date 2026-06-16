try:
    import requests
    import argparse
except ImportError:
    print("the following modules are missing: requests , argparse")


class Finder:
    def __init__(self):
              pass


    def search(self , username:str , timeout:float):
        platforms: list = [
                {"name" : "Github" , "url" : "https://github.com/{username}"},
                {"name": "Instagram", "url": f"https://www.instagram.com/{username}"},
                {"name": "Twitter", "url": f"https://www.x.com/{username}/"},
                {"name": "Facebook", "url": f"https://www.facebook.com/{username}/"},
                {"name": "Youtube", "url": f"https://www.youtube.com/{username}/"},
                {"name": "Snapchat", "url": f"https://story.snapchat.com/@{username}/"},
                {"name": "Spotify", "url": f"https://open.spotify.com/user/{username}/"},
                {"name": "Pinterest", "url": f"https://www.pinterest.com/{username}/"},
                {"name": "Reddit", "url": f"https://www.reddit.com/{username}/"},
                {"name": "Tinder", "url": f"https://www.tinder.com/@{username}/"},
                {"name": "Github", "url": f"https://www.github.com/{username}/"},
                {"name": "Linkedin", "url": f"https://www.linkedin.com/{username}/"}
            ]


        try:
            for platform in platforms:
                name = platform["name"]
                url = platform["url"]

                result = requests.get(url , timeout=timeout)

                match (result.status_code):
                    case 200:
                        print(f"(\033[32mfound\033[0m) \033[35m{name}\033[0m : {url}")
                    case 301 | 302:
                        print(f"(\033[33mredirected\033[0m) \033[35m{name}\033[0m : {url}")
                    case _:
                        pass

        except Exception as e:
            pass


def parse_args():
    parser = argparse.ArgumentParser(description="a simple Username-Hunter")

    parser.add_argument("-u" , "--usernames" , type=str , required=True , help="specifiy usernames (e.g: user1,user2,user3)")
    parser.add_argument("-t" , "--timeout" , type=float , default=1.0)

    return parser.parse_args()

def main() -> None:
    args = parse_args()

    #sanitize usernames
    usernames: list = (args.usernames).split(",")
    print(f"(IO) received {len(usernames)} usernames")
    finder = Finder()

    print("*" * 25)

    for username in usernames:
        finder.search(username , args.timeout)


if __name__ == "__main__":
    main()
