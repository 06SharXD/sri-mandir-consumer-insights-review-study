from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"data"/"reviews.csv"
OUT=ROOT/"analysis"/"outputs"
OUT.mkdir(parents=True,exist_ok=True)
df=pd.read_csv(DATA,keep_default_na=False)
# Exact counts of coded records in this convenience corpus, not market prevalence.
category=df.groupby("primary_category",dropna=False).size().sort_values(ascending=False).rename("review_count").reset_index()
sentiment=df.groupby("sentiment_or_intent").size().sort_values(ascending=False).rename("review_count").reset_index()
category.to_csv(OUT/"theme_counts.csv",index=False)
sentiment.to_csv(OUT/"intent_counts.csv",index=False)
fig,ax=plt.subplots(figsize=(10,5.5)); category.sort_values("review_count").plot.barh(x="primary_category",y="review_count",legend=False,ax=ax,color="#315a73")
ax.set(title="Coded theme counts (n=10 public reviews)",xlabel="Review records",ylabel="Primary code"); fig.tight_layout();fig.savefig(OUT/"theme_counts.png",dpi=180);plt.close(fig)
fig,ax=plt.subplots(figsize=(6,4)); sentiment.set_index("sentiment_or_intent")["review_count"].plot.bar(ax=ax,color="#d58b45")
ax.set(title="Review intent in this corpus (n=10)",xlabel="Coded intent",ylabel="Review records");fig.tight_layout();fig.savefig(OUT/"intent_counts.png",dpi=180);plt.close(fig)
print(f"rows={len(df)} unique_ids={df.review_id.nunique()} categories={df.primary_category.nunique()}")