import requests
import orjson
username="elonmusk"

def get_userid(username):
        url = f"https://api.x.com/graphql/BQ6xjFU6Mgm-WhEP3OiT9w/UserByScreenName?variables=%7B%22screen_name%22%3A%22{username}%22%7D&features=%7B%22hidden_profile_subscriptions_enabled%22%3Atrue%2C%22rweb_tipjar_consumption_enabled%22%3Atrue%2C%22responsive_web_graphql_exclude_directive_enabled%22%3Atrue%2C%22verified_phone_label_enabled%22%3Afalse%2C%22subscriptions_verification_info_is_identity_verified_enabled%22%3Atrue%2C%22subscriptions_verification_info_verified_since_enabled%22%3Atrue%2C%22highlights_tweets_tab_ui_enabled%22%3Atrue%2C%22responsive_web_twitter_article_notes_tab_enabled%22%3Atrue%2C%22subscriptions_feature_can_gift_premium%22%3Atrue%2C%22creator_subscriptions_tweet_preview_api_enabled%22%3Atrue%2C%22responsive_web_graphql_skip_user_profile_image_extensions_enabled%22%3Afalse%2C%22responsive_web_graphql_timeline_navigation_enabled%22%3Atrue%7D&fieldToggles=%7B%22withAuxiliaryUserLabels%22%3Afalse%7D"

        payload = {}
        headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        'content-type': 'application/json',
        'cookie': 'guest_id=172961515689951325; night_mode=2; guest_id_marketing=v1%3A172961515689951325; guest_id_ads=v1%3A172961515689951325; personalization_id="v1_9F70OrjHM0jDnBwiF4mS2g=="; gt=1848766083265691812',
        'origin': 'https://x.com',
        'priority': 'u=1, i',
        'referer': 'https://x.com/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Opera GX";v="113", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 OPR/113.0.0.0',
        'x-client-transaction-id': 'C8ujDRWGqfjLie6ILmV31/ip+cadrgJvqoWeUYUN8SrhRuz1CD3BVONgwVae2GV2Dc16wwmYCg9ooHKEHvhZnwHkH1zwCA',
        'x-guest-token': '1848766083265691812',
        'x-twitter-active-user': 'yes',
        'x-twitter-client-language': 'en'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        if response.status_code != 200:
            return False
        response = orjson.loads(response.text)
        return response["data"]["user"]["result"]["rest_id"]