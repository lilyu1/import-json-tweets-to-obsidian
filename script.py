import json
import os
import sys
from datetime import datetime

def json_to_md(json_file, output_dir):
    with open(json_file, 'r') as file:
        data = json.load(file)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for tweet in data:
        tweet_id = tweet['id']
        username = tweet['screen_name']
        md_file = os.path.join(output_dir, f"{username}-{tweet_id}.md")
        with open(md_file, 'w') as file:
            # Format the date
            created_at = tweet['created_at']
            date_obj = datetime.strptime(created_at, '%Y-%m-%d %H:%M:%S %z')
            formatted_date = date_obj.strftime('%Y-%m-%d %H:%M')

            # Write tweet content
            file.write(tweet['full_text'] + "\n\n")


            # Write metadata
            file.write("## Metadata\n")
            file.write(f"- Author: {tweet['name']}\n")
            file.write(f"- Username: [@{username}](https://twitter.com/{username})\n")
            file.write(f"- Date: {formatted_date}\n")
            file.write(f"- URL: [Link]({tweet['url']})\n")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <json_file>")
        sys.exit(1)

    json_file = sys.argv[1]
    output_dir = 'tweets'

    json_to_md(json_file, output_dir)
    print(f"Markdown files generated in the '{output_dir}' folder.")