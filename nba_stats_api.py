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
	"""Returns the games played for a team during |season|
        in [|start_date|, |end_date|]. If no start and end dates
        are given then the games from the entire season are
        returned. The dates should be formatted as mm/dd/yyyy.
        The season should be formatted as 'yyyy-yy'.

        team: string
        season: string, yyyy-yy
        start_date: string, mm/dd/yyyy.
        end_date: string, mm/dd/yyyy.
        """
        parameters = dict(constants.GAMELOG_PARAMS)
	# TODO: error check for bad team names
	parameters['TeamID'] = constants.TEAM_TO_ID_MAP[team]
	# TODO: error check for formatting
	parameters['Season'] = season
	if start_date:
		parameters['DateFrom'] = start_date
	if end_date:
        parameters['DateTo'] = end_date
	print(parameters)
	return _RequestUrl(constants.GAMELOG_URL, parameters)

if __name__ == "__main__":
	pp.pprint(GetTeamGameLog('Boston Celtics', '2016-17'))

