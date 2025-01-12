import pandas as pd
from datetime import datetime
from geopy.distance import geodesic

# Team location mapping (example with some teams; add the rest)
team_locations = {
    'ARI': (33.4455, -112.0667),  # Arizona Cardinals
    'ATL': (33.7557, -84.4000),   # Atlanta Falcons
    'BAL': (39.2780, -76.6227),   # Baltimore Ravens
    'BUF': (42.7738, -78.7868),   # Buffalo Bills
    'CAR': (35.2251, -80.8392),   # Carolina Panthers
    'CHI': (41.8625, -87.6166),   # Chicago Bears
    'CIN': (39.0975, -84.5070),   # Cincinnati Bengals
    'CLE': (41.5055, -81.6813),   # Cleveland Browns
    'DAL': (32.7473, -97.0945),   # Dallas Cowboys
    'DEN': (39.7439, -105.0201),  # Denver Broncos
    'DET': (42.3314, -83.0458),   # Detroit Lions
    'GB': (44.5013, -88.0622),    # Green Bay Packers
    'HOU': (29.7604, -95.3698),   # Houston Texans
    'IND': (39.7684, -86.1581),   # Indianapolis Colts
    'JAX': (30.3239, -81.6373),   # Jacksonville Jaguars
    'KC': (39.0489, -94.4839),    # Kansas City Chiefs
    'LV': (36.0908, -115.1830),   # Las Vegas Raiders
    'LA': (34.0522, -118.2437),   # Los Angeles Rams
    'LAC': (34.0689, -118.4483),  # Los Angeles Chargers
    'MIA': (25.9580, -80.2389),   # Miami Dolphins
    'MIN': (44.9738, -93.2578),   # Minnesota Vikings
    'NE': (42.0909, -71.2643),    # New England Patriots
    'NO': (29.9511, -90.0715),    # New Orleans Saints
    'NYG': (40.8135, -74.0745),   # New York Giants
    'NYJ': (40.8135, -74.0745),   # New York Jets
    'PHI': (39.9526, -75.1652),   # Philadelphia Eagles
    'PIT': (40.4468, -80.0128),   # Pittsburgh Steelers
    'SF': (37.7749, -122.4194),   # San Francisco 49ers
    'SEA': (47.5952, -122.3316),  # Seattle Seahawks
    'TB': (27.9759, -82.5033),    # Tampa Bay Buccaneers
    'TEN': (36.1665, -86.7713),   # Tennessee Titans
    'WAS': (38.9076, -77.0200)    # Washington Commanders
}

# Load the dataset
file_path = r'NFL - Data App\games.csv'  # Update this to the correct file path
output_path = r'NFL - Data App\games_transformed.csv'  # Output file path
games = pd.read_csv(file_path)

# Convert gameDate to datetime for processing
games['gameDate'] = pd.to_datetime(games['gameDate'])

# 1. Add Day of Week
games['dayOfWeek'] = games['gameDate'].dt.day_name()

# 4. Determine the Winning Team
def determine_winner(row):
    if row['homeFinalScore'] > row['visitorFinalScore']:
        return row['homeTeamAbbr']
    elif row['homeFinalScore'] < row['visitorFinalScore']:
        return row['visitorTeamAbbr']
    else:
        return 'TIE'

games['winningTeam'] = games.apply(determine_winner, axis=1)

# 5. Calculate Point Differential
games['pointDifferential'] = abs(games['homeFinalScore'] - games['visitorFinalScore'])

# 6. Categorize Game Time
def game_time_category(time):
    hour = int(time.split(':')[0])
    if hour < 18:
        return 'Afternoon'
    else:
        return 'Evening'

games['gameTimeCategory'] = games['gameTimeEastern'].apply(game_time_category)

# 7. Label Week Type
def week_type(week):
    if week <= 17:
        return 'Regular Season'
    else:
        return 'Playoffs'

games['weekType'] = games['week'].apply(week_type)

# 8. Add Home Advantage Indicator
games['homeAdvantage'] = games['homeFinalScore'] > games['visitorFinalScore']

# Save the transformed dataset
games.to_csv(output_path, index=False)

print(f"Transformed dataset saved to: {output_path}")
