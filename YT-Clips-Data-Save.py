import requests
import configparser
import os

def get_clip_info(clip_id):
    url = f"https://yt.lemnoslife.com/videos?part=id,clip&clipId={clip_id}"
    response = requests.get(url)
    return response.json()

def save_to_file(data, clipid, olddata):
    config = configparser.ConfigParser()
    config.read("clip_info.ini")
    clip_data = data
    config[clipid] = {
        'videoId': clip_data.get('videoId'),
        'title': clip_data.get('clip').get("title").encode('ascii', errors='ignore').decode('ascii'),
        'startTimeMs': str(clip_data.get('clip').get('startTimeMs')),
        'endTimeMs': str(clip_data.get('clip').get('endTimeMs'))
    }
    
    with open("clip_info.ini", "w", encoding='utf-8') as file:
        config.write(file)

def load_from_file():
    saved_data = {}
    if os.path.exists("clip_info.ini"):
        config = configparser.ConfigParser()
        config.read("clip_info.ini")
        for section in config.sections():
            saved_data[section] = {
                'videoId': config[section]['videoId'],
                'title': config[section]['title'],
                'startTimeMs': int(config[section]['startTimeMs']),
                'endTimeMs': int(config[section]['endTimeMs'])
            }
    return saved_data

def main(clip_ids):
    for clip_id in clip_ids:
        saved_data = load_from_file()

        if clip_id in saved_data:
            print("Data for this clip ID is already saved.")
        else:
            clip_info: dict = get_clip_info(clip_id)
            new_data = clip_info.get("items", [])[0]
            print(new_data)
            save_to_file(new_data, clip_id, saved_data)
            print("Data saved to file.")

if __name__ == "__main__":
    with open(r"C:\Users\shaur\Master Folder\Main Apps\SAMMI\MyFiles\YTClipsList.txt", "r") as file:
        clip_ids = [line.strip() for line in file.readlines()]
    main(clip_ids)
