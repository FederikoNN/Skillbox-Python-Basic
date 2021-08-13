import json

import requests

dict_out = {"episode_id": None,
            "season": None,
            "episode": None,
            "count_of_deaths": None,
            "list_of_dead": None
            }

deaths = requests.get('https://www.breakingbadapi.com/api/death/')
episodes = requests.get('https://www.breakingbadapi.com/api/episodes')

data_deaths = json.loads(deaths.text)
data_episodes = json.loads(episodes.text)

deaths_in_episode = {}
for i_dict in data_deaths:
    if (i_dict['season'], i_dict['episode']) in deaths_in_episode.keys():
        deaths_in_episode[(i_dict['season'], i_dict['episode'])] += 1
    else:
        deaths_in_episode[(i_dict['season'], i_dict['episode'])] = 1

dict_out["count_of_deaths"] = max(deaths_in_episode.values())

dict_out['season'], dict_out['episode'] = \
    [key for key in deaths_in_episode.keys() if deaths_in_episode[key] == max(deaths_in_episode.values())][0]

dict_out['episode_id'] = [x['episode_id'] for x in data_episodes if
                          int(x['season']) == dict_out['season'] and int(x['episode']) == dict_out['episode']][0]

dict_out["list_of_dead"] = [x['death'] for x in data_deaths if
                            int(x['season']) == dict_out['season'] and int(x['episode']) == dict_out['episode']]
print(json.dumps(dict_out, indent=4))

with open('episode_with_max_deaths.json', 'w') as file:
    json.dump(dict_out, file, indent=4)
