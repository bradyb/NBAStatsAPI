import constants

import pandas as pd
import pprint as pp
import requests

def _RequestUrl(url, parameters):
	response = requests.get(url, params=parameters, headers=constants.REQUEST_HEADERS)
	headers = response.json()['resultSets'][0]['headers']
	stats = response.json()['resultSets'][0]['rowSet']
	return pd.DataFrame(stats, columns=headers)

def GetTeamGameLog(team, season, start_date=None, end_date=None):
	parameters = dict(constants.GAMELOG_PARAMS)
	# TODO: error check for bad team names
	parameters['TeamID'] = constants.TEAM_TO_ID_MAP[team]
	# TODO: error chech for formatting
	parameters['Season'] = season
	if start_date:
		pass
		# TODO: set start_date
	if end_date:
		pass
		# TODO: set end_date
	print(parameters)
	return _RequestUrl(constants.GAMELOG_URL, parameters)

if __name__ == "__main__":
	pp.pprint(GetTeamGameLog('Boston Celtics', '2016-17'))

