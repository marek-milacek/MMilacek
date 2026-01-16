import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta

# Nastavení stylu grafů
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['figure.figsize'] = (14, 10)

# Vytvoření vzorových dat o letech po světě
np.random.seed(42)

# Světové letiště a jejich průměrné délky letů
letisteData = {
    'Praha': {'počet_letů': 450, 'průměrná_délka': 3.5, 'počet_destinací': 120},
    'Londýn': {'počet_letů': 1200, 'průměrná_délka': 5.2, 'počet_destinací': 250},
    'Franfurt': {'počet_letů': 980, 'průměrná_délka': 4.8, 'počet_destinací': 240},
    'Paříž': {'počet_letů': 800, 'průměrná_délka': 4.3, 'počet_destinací': 200},
    'Amsterdam': {'počet_letů': 650, 'průměrná_délka': 4.1, 'počet_destinací': 180},
    'New York': {'počet_letů': 1500, 'průměrná_délka': 9.5, 'počet_destinací': 300},
    'Tokio': {'počet_letů': 900, 'průměrná_délka': 11.2, 'počet_destinací': 200},
    'Sydney': {'počet_letů': 600, 'průměrná_délka': 13.5, 'počet_destinací': 150},
    'Dubaj': {'počet_letů': 1100, 'průměrná_délka': 6.8, 'počet_destinací': 280},
    'Singapur': {'počet_letů': 750, 'průměrná_délka': 7.2, 'počet_destinací': 170},
}

# Převod na DataFrame
letisteDF = pd.DataFrame.from_dict(letisteData, orient='index')
letisteDF = letisteDF.reset_index().rename(columns={'index': 'Letiště'})

# Data o typech letů a jejich průměrných délkách (v hodinách)
typyLetů = {
    'Domácí lety': 2.0,
    'Evropské': 3.5,
    'Transatlantické': 7.5,
    'Asijské': 10.0,
    'Australské': 13.0,
    'Dlouhé trasy (USA-Asie)': 14.5,
}

# Generování dat o letošních letech
měsíce = ['Leden', 'Únor', 'Březen', 'Duben', 'Květen', 'Červen', 
          'Červenec', 'Srpen', 'Září', 'Říjen', 'Listopad', 'Prosinec']
měsíční_letů = np.random.randint(800, 2000, size=12)

# Vytvoření figury s více subploty
fig = plt.figure(figsize=(16, 12))
fig.suptitle('Analýza Letů Po Celém Světě - 2026', fontsize=18, fontweight='bold', y=0.995)

# 1. Graf: Počet letů na jednotlivých letištích
ax1 = plt.subplot(2, 3, 1)
colors1 = plt.cm.viridis(np.linspace(0, 1, len(letisteDF)))
bars1 = ax1.bar(letisteDF['Letiště'], letisteDF['počet_letů'], color=colors1, edgecolor='black', linewidth=1.5)
ax1.set_title('Počet Letů na Letištích', fontsize=12, fontweight='bold')
ax1.set_ylabel('Počet Letů za Měsíc', fontsize=10)
ax1.set_xlabel('Letiště', fontsize=10)
plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45, ha='right')
ax1.grid(axis='y', alpha=0.3)
# Přidání hodnot na sloupce
for bar in bars1:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height,
             f'{int(height)}', ha='center', va='bottom', fontsize=8)

# 2. Graf: Průměrná délka letu na letištích
ax2 = plt.subplot(2, 3, 2)
colors2 = plt.cm.plasma(np.linspace(0, 1, len(letisteDF)))
bars2 = ax2.barh(letisteDF['Letiště'], letisteDF['průměrná_délka'], color=colors2, edgecolor='black', linewidth=1.5)
ax2.set_title('Průměrná Délka Letu', fontsize=12, fontweight='bold')
ax2.set_xlabel('Délka Letu (hodiny)', fontsize=10)
ax2.grid(axis='x', alpha=0.3)
# Přidání hodnot na sloupce
for bar in bars2:
    width = bar.get_width()
    ax2.text(width, bar.get_y() + bar.get_height()/2.,
             f'{width:.1f}h', ha='left', va='center', fontsize=8, fontweight='bold')

# 3. Graf: Počet destinací na letištích
ax3 = plt.subplot(2, 3, 3)
scatter = ax3.scatter(letisteDF['počet_letů'], letisteDF['počet_destinací'], 
                     s=letisteDF['průměrná_délka']*50, alpha=0.6, 
                     c=letisteDF['průměrná_délka'], cmap='coolwarm', edgecolors='black', linewidth=1.5)
ax3.set_title('Vztah: Počet Letů vs Destinací', fontsize=12, fontweight='bold')
ax3.set_xlabel('Počet Letů', fontsize=10)
ax3.set_ylabel('Počet Destinací', fontsize=10)
ax3.grid(alpha=0.3)
# Přidání jmen letišť
for idx, row in letisteDF.iterrows():
    ax3.annotate(row['Letiště'][:3], (row['počet_letů'], row['počet_destinací']),
                fontsize=8, ha='center')
cbar = plt.colorbar(scatter, ax=ax3)
cbar.set_label('Průměr. Délka (h)', fontsize=9)

# 4. Graf: Typy letů a jejich délky
ax4 = plt.subplot(2, 3, 4)
typy = list(typyLetů.keys())
delky = list(typyLetů.values())
colors4 = plt.cm.Set3(np.linspace(0, 1, len(typy)))
pie = ax4.pie(delky, labels=typy, autopct='%1.1f%%', colors=colors4, startangle=90,
             textprops={'fontsize': 9})
ax4.set_title('Distribuce Typů Letů', fontsize=12, fontweight='bold')

# 5. Graf: Měsíční počet letů v roce 2026
ax5 = plt.subplot(2, 3, 5)
line = ax5.plot(měsíce, měsíční_letů, marker='o', linewidth=2.5, markersize=8, 
               color='#2ecc71', markerfacecolor='#27ae60', markeredgecolor='black', markeredgewidth=1.5)
ax5.fill_between(range(len(měsíce)), měsíční_letů, alpha=0.3, color='#2ecc71')
ax5.set_title('Počet Letů po Měsících v 2026', fontsize=12, fontweight='bold')
ax5.set_ylabel('Počet Letů', fontsize=10)
ax5.set_xlabel('Měsíc', fontsize=10)
plt.setp(ax5.xaxis.get_majorticklabels(), rotation=45, ha='right')
ax5.grid(alpha=0.3)
# Přidání hodnot na body
for i, (m, val) in enumerate(zip(měsíce, měsíční_letů)):
    ax5.text(i, val + 30, str(val), ha='center', va='bottom', fontsize=8, fontweight='bold')

# 6. Graf: Box plot - Porovnání délky letů
ax6 = plt.subplot(2, 3, 6)
data_pro_box = [np.random.normal(typyLetů[typ], typyLetů[typ]*0.2, 100) for typ in typy]
bp = ax6.boxplot(data_pro_box, labels=[t.replace(' ', '\n') for t in typy], patch_artist=True)
# Obarvení box plotů
for patch, color in zip(bp['boxes'], plt.cm.Pastel1(np.linspace(0, 1, len(typy)))):
    patch.set_facecolor(color)
    patch.set_edgecolor('black')
    patch.set_linewidth(1.5)
for whisker in bp['whiskers']:
    whisker.set_linewidth(1.5)
for cap in bp['caps']:
    cap.set_linewidth(1.5)
ax6.set_title('Variabilita Délky Letů', fontsize=12, fontweight='bold')
ax6.set_ylabel('Délka Letu (hodiny)', fontsize=10)
ax6.grid(axis='y', alpha=0.3)
plt.setp(ax6.xaxis.get_majorticklabels(), rotation=45, ha='right', fontsize=8)

plt.tight_layout()
plt.show()

# Tisk souhrnu dat
print("\n" + "="*70)
print("SOUHRN LETŮ PO CELÉM SVĚTĚ - 2026")
print("="*70)
print("\nStatistika Letišť:")
print(letisteDF.to_string(index=False))
print("\n" + "-"*70)
print(f"Celkový počet letů: {letisteDF['počet_letů'].sum():,}")
print(f"Průměrná délka letu: {letisteDF['průměrná_délka'].mean():.2f} hodin")
print(f"Celkový počet destinací: {letisteDF['počet_destinací'].sum():,}")
print(f"Nejrušnější letiště: {letisteDF.loc[letisteDF['počet_letů'].idxmax(), 'Letiště']} ({letisteDF['počet_letů'].max()} letů)")
print(f"Nejdelší průměrný let: {letisteDF.loc[letisteDF['průměrná_délka'].idxmax(), 'Letiště']} ({letisteDF['průměrná_délka'].max():.2f} hodin)")
print("="*70)