import time
import requests
import json
import urllib.parse


# for testing your headers you may use user_id = 44196397
print("Be sure to update your headers.json file with your own headers before running this script. To get headers one may know how to use browser developer tools.")
user_id = input("Enter the user ID (no fancy parsing here, be careful): ")


variables = {
    "userId": str(user_id),
    "count": 20,
    "includePromotedContent": False,
    "cursor": None
}


with open('headers.json') as f:
    headers = json.load(f)

followers = []
unhealthy = 0  

while True:
    encoded_variables = urllib.parse.quote(json.dumps(variables))
    url = f"https://x.com/i/api/graphql/eWTmcJY3EMh-dxIR7CYTKw/Following?variables={encoded_variables}&features=%7B%22rweb_tipjar_consumption_enabled%22%3Atrue%2C%22responsive_web_graphql_exclude_directive_enabled%22%3Atrue%2C%22verified_phone_label_enabled%22%3Afalse%2C%22creator_subscriptions_tweet_preview_api_enabled%22%3Atrue%2C%22responsive_web_graphql_timeline_navigation_enabled%22%3Atrue%2C%22responsive_web_graphql_skip_user_profile_image_extensions_enabled%22%3Afalse%2C%22communities_web_enable_tweet_community_results_fetch%22%3Atrue%2C%22c9s_tweet_anatomy_moderator_badge_enabled%22%3Atrue%2C%22articles_preview_enabled%22%3Atrue%2C%22responsive_web_edit_tweet_api_enabled%22%3Atrue%2C%22graphql_is_translatable_rweb_tweet_is_translatable_enabled%22%3Atrue%2C%22view_counts_everywhere_api_enabled%22%3Atrue%2C%22longform_notetweets_consumption_enabled%22%3Atrue%2C%22responsive_web_twitter_article_tweet_consumption_enabled%22%3Atrue%2C%22tweet_awards_web_tipping_enabled%22%3Afalse%2C%22creator_subscriptions_quote_tweet_preview_enabled%22%3Afalse%2C%22freedom_of_speech_not_reach_fetch_enabled%22%3Atrue%2C%22standardized_nudges_misinfo%22%3Atrue%2C%22tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled%22%3Atrue%2C%22rweb_video_timestamps_enabled%22%3Atrue%2C%22longform_notetweets_rich_text_read_enabled%22%3Atrue%2C%22longform_notetweets_inline_media_enabled%22%3Atrue%2C%22responsive_web_enhance_cards_enabled%22%3Afalse%7D"


    response = requests.get(url, headers=headers)


    if response.status_code != 200:
        unhealthy += 1
        if unhealthy == 5:
            print("\nseems your cookies are overcooked.\n")
            break
        time.sleep(5) 
        continue

    
    unhealthy = 0
    
    json_data = json.loads(response.text)
    if "errors" in json_data:
        print("\nseems your cookies are overcooked.\n")
        print(json_data)
        break


    try:
        entries = json_data["data"]["user"]["result"]["timeline"]["timeline"]["instructions"][-1]["entries"]
        if len(entries) == 2:
            print("No more followers to retrieve.")
            break


        for entry in entries:
            try:
                screen_name = entry["content"]["itemContent"]["user_results"]["result"]["legacy"]["screen_name"]
                followers.append(screen_name)
            except KeyError:
                followers.append("Account maybe banned in your country")
                continue  

        next_cursor = entries[-2]["content"]["value"]
        variables["cursor"] = next_cursor

    except Exception as e:
        print(f"Error parsing response: {e}")
        continue


    print(f"Number of followers retrieved: {len(followers)}", end="\r")

    time.sleep(1.5)

print(f"\nTotal followers retrieved: {len(followers)}")

file_path = f"{user_id}.txt"
with open(file_path, 'w') as file:
    file.write("Contact me: https://www.upwork.com/freelancers/~01419e1fc0370fdce8\n")
    for follower in followers:
        file.write(f"{follower}\n")
    file.write(f"Total followers retrieved: {len(followers)}")
