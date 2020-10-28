# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
csv_path = "Resources/purchase_data.csv"
Heroes_df = pd.read_csv(csv_path)
Heroes_df.head()


# %%
Heroes_player_renamed_df = Heroes_df.rename(columns={"SN": "Players"})
Heroes_player_renamed_df


# %%
Player_Count_df = Heroes_player_renamed_df["Players"].value_counts()
Player_Count_df


# %%
Heroes_frame_df = pd.DataFrame({"Total Players": [576]})
Heroes_frame_df


# %%
Heroes_item_df = Heroes_player_renamed_df["Item Name"].nunique()
Heroes_average_price_df = Heroes_player_renamed_df["Price"].mean()
Heroes_item_count_df = Heroes_player_renamed_df["Item Name"].count()
Heroes_total_price_df = Heroes_player_renamed_df["Price"].sum()


# %%
Heroes_summary_df = pd.DataFrame({"Number of Unique Items": [Heroes_item_df],"Average Price": [Heroes_average_price_df], "Number of Purchases": [Heroes_item_count_df], "Total Revenue": [Heroes_total_price_df]})
Heroes_summary_df


# %%
print(Heroes_summary_df)


# %%



# %%



