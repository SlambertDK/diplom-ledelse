import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

fig, ax = plt.subplots(1, 1, figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')
fig.patch.set_facecolor('#F8F9FA')

def box(ax, x, y, w, h, label, sublabel=None, color='#2C3E50', textcolor='white', fontsize=9):
    rect = mpatches.FancyBboxPatch((x - w/2, y - h/2), w, h,
        boxstyle="round,pad=0.1", linewidth=1.5,
        edgecolor='#BDC3C7', facecolor=color)
    ax.add_patch(rect)
    if sublabel:
        ax.text(x, y + 0.12, label, ha='center', va='center',
                fontsize=fontsize, fontweight='bold', color=textcolor)
        ax.text(x, y - 0.18, sublabel, ha='center', va='center',
                fontsize=7, color=textcolor, style='italic')
    else:
        ax.text(x, y, label, ha='center', va='center',
                fontsize=fontsize, fontweight='bold', color=textcolor)

def line(ax, x1, y1, x2, y2, style='-', color='#7F8C8D', lw=1.5):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
        arrowprops=dict(arrowstyle='->', color=color, lw=lw, linestyle=style))

# Titel
ax.text(7, 9.5, 'Energinet — Organisatorisk placering', ha='center', va='center',
        fontsize=13, fontweight='bold', color='#2C3E50')
ax.text(7, 9.1, 'Digital Accelerators position og adoptionsflow', ha='center', va='center',
        fontsize=9, color='#7F8C8D', style='italic')

# Top — CTO
box(ax, 7, 8.3, 3.2, 0.65, 'Signe Horn Rosted', 'CTO', color='#1A252F')

# Niveau 2
box(ax, 7, 7.2, 3.4, 0.65, 'Nicolaj Nørgaard Peulicke', 'Tech & Innovation', color='#2C3E50')

# Niveau 3
box(ax, 7, 6.1, 3.4, 0.65, 'Jesper Søgaard', 'Innovation & Digital Core', color='#34495E')

# Niveau 4 — Jonas (Henriks chef)
box(ax, 7, 5.0, 3.4, 0.65, 'Jonas Lundgaard Hvelplund', 'CPO — Business Acceleration & Digitalisation', color='#2980B9')

# Niveau 5 — Henrik + Helle side om side
box(ax, 4.5, 3.8, 3.2, 0.65, 'Henrik Lambert', 'Product Owner — Digital Accelerator', color='#E74C3C')
box(ax, 9.5, 3.8, 3.2, 0.65, 'Helle Olesen', 'APL — Personaleleder', color='#8E44AD')

# Modtagende enheder (tre bokse)
box(ax, 2.0, 2.2, 2.6, 0.65, 'Driftsafdelinger', 'Modtagende enhed', color='#27AE60', fontsize=8)
box(ax, 7,   2.2, 2.6, 0.65, 'Forretningsenheder', 'Modtagende enhed', color='#27AE60', fontsize=8)
box(ax, 12.0,2.2, 2.6, 0.65, 'Støttefunktioner', 'Modtagende enhed', color='#27AE60', fontsize=8)

# Hierarki linjer
for y1, y2 in [(8.0, 7.55), (6.9, 6.45), (5.8, 5.35)]:
    line(ax, 7, y1, 7, y2, color='#2C3E50')

# Jonas til Henrik og Helle
line(ax, 7, 4.68, 4.5, 4.15, color='#2C3E50')
line(ax, 7, 4.68, 9.5, 4.15, color='#8E44AD')

# Adoptionslinjer (stiplet, rød)
for xto in [2.0, 7, 12.0]:
    ax.annotate('', xy=(xto, 2.55), xytext=(4.5, 3.47),
        arrowprops=dict(arrowstyle='->', color='#E74C3C', lw=1.5,
                        linestyle='dashed'))

# Label på adoptionslinjer
ax.text(4.0, 3.0, 'Adoptionsproces\n(ingen formel autoritet)', ha='center', va='center',
        fontsize=7.5, color='#E74C3C', style='italic')

# Legende
from matplotlib.patches import Rectangle
legend_handles = [
    Rectangle((0,0), 1, 1, color='#2C3E50', label='Ledelseshierarki'),
    Rectangle((0,0), 1, 1, color='#E74C3C', label='Digital Accelerator'),
    Rectangle((0,0), 1, 1, color='#27AE60', label='Modtagende enheder'),
]
ax.legend(handles=legend_handles, loc='lower left', fontsize=8, framealpha=0.8)

plt.tight_layout()
plt.savefig('/home/henrik/.openclaw/workspace/org-diagram.png', dpi=180, bbox_inches='tight',
            facecolor='#F8F9FA')
print('Gemt: org-diagram.png')
