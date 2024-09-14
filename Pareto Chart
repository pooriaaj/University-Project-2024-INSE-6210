import matplotlib.pyplot as plt
import pandas as pd

data = {'Issue': ['Wrong Batch', 'Late Delivery', 'Damaged Orders', 'Others'],
        'Count': [3546, 1234, 567, 300]}
df = pd.DataFrame(data)

df = df.sort_values(by='Count', ascending=False)

df['cum_percentage'] = df['Count'].cumsum() / df['Count'].sum() * 100

fig, ax = plt.subplots()
ax.bar(df['Issue'], df['Count'], color='C0')
ax2 = ax.twinx()
ax2.plot(df['Issue'], df['cum_percentage'], color='C1', marker="D", ms=7)
ax2.set_ylim(0, 110)

plt.show()
