import pandas as pd
import os

def swap_players_based_on_outcome(input_csv, output_csv):

    df = pd.read_csv(input_csv)
    df_processed = df.copy()
    
    # Find rows where outcome is -1
    neg_outcome_mask = df['outcome'] == -1
    
    # swap home and away team names
    temp_home_team = df.loc[neg_outcome_mask, 'home_team'].copy()
    df_processed.loc[neg_outcome_mask, 'home_team'] = df.loc[neg_outcome_mask, 'away_team']
    df_processed.loc[neg_outcome_mask, 'away_team'] = temp_home_team
    
    # swap players
    for i in range(5):  
        home_col = f'home_{i}'
        away_col = f'away_{i}'
        
        temp_home = df.loc[neg_outcome_mask, home_col].copy()
        df_processed.loc[neg_outcome_mask, home_col] = df.loc[neg_outcome_mask, away_col]
        df_processed.loc[neg_outcome_mask, away_col] = temp_home
    
    df_processed.drop(columns=["outcome"], inplace=True)
    df_processed.to_csv(output_csv, index=False)
    
    total_rows = len(df)
    swapped_rows = neg_outcome_mask.sum()
    print(f"Processing complete!")
    print(f"Total rows: {total_rows}")
    print(f"Rows with swapped players (outcome = -1): {swapped_rows}")
    print(f"Output saved to: {output_csv}")

if __name__ == "__main__":
    for file in os.listdir("C:/Users/hannest/Desktop/NBA prediction/data"):
        print(file)
        if file.endswith(".csv"):
            input_file = os.path.join("C:/Users/hannest/Desktop/NBA prediction/data", file)
            output_file = os.path.join("C:/Users/hannest/Desktop/NBA prediction/data/all_winning_home", f"swapped_{file}")
            swap_players_based_on_outcome(input_file, output_file)
