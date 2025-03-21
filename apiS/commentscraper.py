from googleapiclient.discovery import build
import pandas as pd
api_key = "AIzaSyAhvccJbupqnxCDH8_tb8vH6aqSVDnnXgo"
youtube = build("youtube", "v3", developerKey=api_key)

def get_comments(video_id):
    comments = []
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=1000
    )
    response = request.execute()

    while response:
        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            author = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
            comments.append({"Author": author, "Comment": comment})
        
        if 'nextPageToken' in response:
            request = youtube.commentThreads().list(
                part="snippet",
                videoId=video_id,
                pageToken=response['nextPageToken'],
                maxResults=1000
            )
            response = request.execute()
        else:
            break
    return comments


video_id = "sURiqfEnMVw"
comments = get_comments(video_id)
df = pd.DataFrame(comments)
df.to_csv("youtube_comments.csv", index=False)
print("Comments saved to youtube_comments.csv")
