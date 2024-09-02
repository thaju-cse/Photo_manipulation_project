import re
import sys

def main():
    print(parse(input("HTML: ")))
def parse(s):
    pattern = r'<iframe[^>]*src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"[^>]*>'
    match = re.search(pattern, s)
    if match:
        #Extract the videoID from the match
        video_id = match.group(1)
        #Construct the shorten URL
        return f"https://youtu.be/{video_id}"
    else:
        return None

if __name__ == "__main__":
    main()
