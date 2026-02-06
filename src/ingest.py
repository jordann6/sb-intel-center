import nfl_data_py as nfl
import pandas as pd

def harvest_sb_data():
    years = [2025]
    p_stats = nfl.import_player_stats(years)
    sb_teams = ['NE', 'SEA']
    return p_stats[p_stats['recent_team'].isin(sb_teams)]

if __name__ == "__main__":
    data = harvest_sb_data()
    print(f"Stats ingested for {len(data)} records.")