import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def draw_stick_figure(ax, x, y, pose='standing', scale=1.0, color='#2c3e50', flip=False):
    """Draw a simple stick figure with different poses."""
    s = scale
    flip_mult = -1 if flip else 1

    head_radius = 0.08 * s

    # Head
    head = plt.Circle((x, y + 0.85*s), head_radius, fill=False, color=color, linewidth=2)
    ax.add_patch(head)

    if pose == 'standing':
        # Torso
        ax.plot([x, x], [y + 0.77*s, y + 0.4*s], color=color, linewidth=2)
        # Arms
        ax.plot([x - 0.15*s, x + 0.15*s], [y + 0.65*s, y + 0.65*s], color=color, linewidth=2)
        # Legs
        ax.plot([x, x - 0.1*s], [y + 0.4*s, y], color=color, linewidth=2)
        ax.plot([x, x + 0.1*s], [y + 0.4*s, y], color=color, linewidth=2)

    elif pose == 'squat':
        # Torso (angled forward slightly)
        ax.plot([x, x], [y + 0.77*s, y + 0.45*s], color=color, linewidth=2)
        # Arms forward
        ax.plot([x, x + 0.2*s*flip_mult], [y + 0.65*s, y + 0.55*s], color=color, linewidth=2)
        ax.plot([x, x - 0.2*s*flip_mult], [y + 0.65*s, y + 0.55*s], color=color, linewidth=2)
        # Legs bent
        ax.plot([x, x - 0.18*s], [y + 0.45*s, y + 0.25*s], color=color, linewidth=2)
        ax.plot([x - 0.18*s, x - 0.08*s], [y + 0.25*s, y], color=color, linewidth=2)
        ax.plot([x, x + 0.18*s], [y + 0.45*s, y + 0.25*s], color=color, linewidth=2)
        ax.plot([x + 0.18*s, x + 0.08*s], [y + 0.25*s, y], color=color, linewidth=2)

    elif pose == 'squat_rotate':
        # Torso rotated
        ax.plot([x, x + 0.08*s*flip_mult], [y + 0.77*s, y + 0.45*s], color=color, linewidth=2)
        # One arm up, one down
        ax.plot([x + 0.08*s*flip_mult, x + 0.25*s*flip_mult], [y + 0.65*s, y + 0.9*s], color=color, linewidth=2)
        ax.plot([x + 0.08*s*flip_mult, x - 0.1*s*flip_mult], [y + 0.65*s, y + 0.45*s], color=color, linewidth=2)
        # Legs bent
        ax.plot([x, x - 0.18*s], [y + 0.45*s, y + 0.25*s], color=color, linewidth=2)
        ax.plot([x - 0.18*s, x - 0.08*s], [y + 0.25*s, y], color=color, linewidth=2)
        ax.plot([x, x + 0.18*s], [y + 0.45*s, y + 0.25*s], color=color, linewidth=2)
        ax.plot([x + 0.18*s, x + 0.08*s], [y + 0.25*s, y], color=color, linewidth=2)
        # Rotation arrow
        arrow_style = patches.FancyArrowPatch((x + 0.3*s*flip_mult, y + 0.7*s),
                                               (x + 0.35*s*flip_mult, y + 0.85*s),
                                               arrowstyle='->', mutation_scale=10, color='#e74c3c')
        ax.add_patch(arrow_style)

    elif pose == 'knee_push':
        # Squat with knees out
        ax.plot([x, x], [y + 0.77*s, y + 0.45*s], color=color, linewidth=2)
        ax.plot([x, x + 0.15*s], [y + 0.65*s, y + 0.55*s], color=color, linewidth=2)
        ax.plot([x, x - 0.15*s], [y + 0.65*s, y + 0.55*s], color=color, linewidth=2)
        # Legs bent outward
        ax.plot([x, x - 0.25*s], [y + 0.45*s, y + 0.25*s], color=color, linewidth=2)
        ax.plot([x - 0.25*s, x - 0.15*s], [y + 0.25*s, y], color=color, linewidth=2)
        ax.plot([x, x + 0.25*s], [y + 0.45*s, y + 0.25*s], color=color, linewidth=2)
        ax.plot([x + 0.25*s, x + 0.15*s], [y + 0.25*s, y], color=color, linewidth=2)
        # Push arrows
        ax.annotate('', xy=(x - 0.35*s, y + 0.25*s), xytext=(x - 0.25*s, y + 0.25*s),
                    arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=1.5))
        ax.annotate('', xy=(x + 0.35*s, y + 0.25*s), xytext=(x + 0.25*s, y + 0.25*s),
                    arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=1.5))

    elif pose == 'internal_rotation':
        # Seated/kneeling position
        ax.plot([x, x], [y + 0.77*s, y + 0.5*s], color=color, linewidth=2)
        ax.plot([x, x + 0.15*s], [y + 0.65*s, y + 0.5*s], color=color, linewidth=2)
        ax.plot([x, x - 0.15*s], [y + 0.65*s, y + 0.5*s], color=color, linewidth=2)
        # Legs with internal rotation
        ax.plot([x, x - 0.15*s], [y + 0.5*s, y + 0.25*s], color=color, linewidth=2)
        ax.plot([x - 0.15*s, x - 0.25*s], [y + 0.25*s, y + 0.1*s], color=color, linewidth=2)
        ax.plot([x, x + 0.15*s], [y + 0.5*s, y + 0.25*s], color=color, linewidth=2)
        ax.plot([x + 0.15*s, x + 0.05*s], [y + 0.25*s, y + 0.1*s], color=color, linewidth=2)
        # Rotation indicator
        theta = np.linspace(0, np.pi/2, 20)
        arc_x = x + 0.1*s + 0.08*s * np.cos(theta)
        arc_y = y + 0.15*s + 0.08*s * np.sin(theta)
        ax.plot(arc_x, arc_y, color='#e74c3c', linewidth=1.5)

    elif pose == 'toe_raise':
        # Standing on heels
        ax.plot([x, x], [y + 0.82*s, y + 0.45*s], color=color, linewidth=2)
        ax.plot([x, x + 0.12*s], [y + 0.7*s, y + 0.55*s], color=color, linewidth=2)
        ax.plot([x, x - 0.12*s], [y + 0.7*s, y + 0.55*s], color=color, linewidth=2)
        ax.plot([x, x - 0.05*s], [y + 0.45*s, y + 0.05*s], color=color, linewidth=2)
        ax.plot([x, x + 0.05*s], [y + 0.45*s, y + 0.05*s], color=color, linewidth=2)
        # Feet with toes up
        ax.plot([x - 0.05*s, x - 0.12*s], [y + 0.05*s, y + 0.12*s], color=color, linewidth=2)
        ax.plot([x + 0.05*s, x + 0.12*s], [y + 0.05*s, y + 0.12*s], color=color, linewidth=2)
        # Up arrows
        ax.annotate('', xy=(x - 0.12*s, y + 0.2*s), xytext=(x - 0.12*s, y + 0.1*s),
                    arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=1.5))
        ax.annotate('', xy=(x + 0.12*s, y + 0.2*s), xytext=(x + 0.12*s, y + 0.1*s),
                    arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=1.5))

    elif pose == 'hami_extension':
        # Forward bend / hinge
        head2 = plt.Circle((x + 0.3*s, y + 0.55*s), head_radius, fill=False, color=color, linewidth=2)
        ax.add_patch(head2)
        head.remove()
        ax.plot([x + 0.22*s, x], [y + 0.55*s, y + 0.4*s], color=color, linewidth=2)
        ax.plot([x + 0.15*s, x + 0.35*s], [y + 0.5*s, y + 0.35*s], color=color, linewidth=2)
        ax.plot([x, x - 0.05*s], [y + 0.4*s, y], color=color, linewidth=2)
        ax.plot([x, x + 0.15*s], [y + 0.4*s, y], color=color, linewidth=2)

    elif pose == 'knee_drive':
        # One knee up
        ax.plot([x, x], [y + 0.77*s, y + 0.4*s], color=color, linewidth=2)
        ax.plot([x, x + 0.1*s], [y + 0.65*s, y + 0.5*s], color=color, linewidth=2)
        ax.plot([x, x - 0.1*s], [y + 0.65*s, y + 0.5*s], color=color, linewidth=2)
        # Standing leg
        ax.plot([x, x + 0.05*s], [y + 0.4*s, y], color=color, linewidth=2)
        # Driving knee
        ax.plot([x, x - 0.15*s], [y + 0.4*s, y + 0.5*s], color=color, linewidth=2)
        ax.plot([x - 0.15*s, x - 0.15*s], [y + 0.5*s, y + 0.3*s], color=color, linewidth=2)
        # Drive arrow
        ax.annotate('', xy=(x - 0.15*s, y + 0.6*s), xytext=(x - 0.15*s, y + 0.45*s),
                    arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=2))

    elif pose == 'straddle':
        # Wide stance with rotation
        ax.plot([x, x + 0.1*s*flip_mult], [y + 0.77*s, y + 0.5*s], color=color, linewidth=2)
        ax.plot([x + 0.1*s*flip_mult, x + 0.25*s*flip_mult], [y + 0.65*s, y + 0.85*s], color=color, linewidth=2)
        ax.plot([x + 0.1*s*flip_mult, x - 0.1*s*flip_mult], [y + 0.65*s, y + 0.5*s], color=color, linewidth=2)
        # Wide legs
        ax.plot([x, x - 0.3*s], [y + 0.5*s, y + 0.15*s], color=color, linewidth=2)
        ax.plot([x - 0.3*s, x - 0.35*s], [y + 0.15*s, y], color=color, linewidth=2)
        ax.plot([x, x + 0.3*s], [y + 0.5*s, y + 0.15*s], color=color, linewidth=2)
        ax.plot([x + 0.3*s, x + 0.35*s], [y + 0.15*s, y], color=color, linewidth=2)

    elif pose == 'wrist':
        # Tabletop position focusing on wrists
        head3 = plt.Circle((x, y + 0.5*s), head_radius * 0.8, fill=False, color=color, linewidth=2)
        ax.add_patch(head3)
        head.remove()
        # Back horizontal
        ax.plot([x, x + 0.3*s], [y + 0.45*s, y + 0.4*s], color=color, linewidth=2)
        # Arms down
        ax.plot([x + 0.05*s, x], [y + 0.42*s, y + 0.2*s], color=color, linewidth=2)
        ax.plot([x + 0.2*s, x + 0.15*s], [y + 0.4*s, y + 0.2*s], color=color, linewidth=2)
        # Hands on ground
        ax.plot([x, x + 0.08*s], [y + 0.2*s, y + 0.2*s], color=color, linewidth=2)
        ax.plot([x + 0.15*s, x + 0.23*s], [y + 0.2*s, y + 0.2*s], color=color, linewidth=2)
        # Legs
        ax.plot([x + 0.3*s, x + 0.35*s], [y + 0.4*s, y + 0.2*s], color=color, linewidth=2)
        # Wrist circles
        circle1 = plt.Circle((x + 0.04*s, y + 0.2*s), 0.04*s, fill=False, color='#e74c3c', linewidth=1.5, linestyle='--')
        circle2 = plt.Circle((x + 0.19*s, y + 0.2*s), 0.04*s, fill=False, color='#e74c3c', linewidth=1.5, linestyle='--')
        ax.add_patch(circle1)
        ax.add_patch(circle2)

    elif pose == 'shift':
        # Weight shifting stance
        ax.plot([x, x + 0.05*s*flip_mult], [y + 0.77*s, y + 0.4*s], color=color, linewidth=2)
        ax.plot([x + 0.05*s*flip_mult, x + 0.15*s*flip_mult], [y + 0.65*s, y + 0.5*s], color=color, linewidth=2)
        ax.plot([x + 0.05*s*flip_mult, x - 0.1*s*flip_mult], [y + 0.65*s, y + 0.55*s], color=color, linewidth=2)
        # Legs - weight shifted
        ax.plot([x, x - 0.15*s], [y + 0.4*s, y], color=color, linewidth=2)
        ax.plot([x, x + 0.2*s], [y + 0.4*s, y], color=color, linewidth=2)
        # Shift arrow
        ax.annotate('', xy=(x + 0.2*s*flip_mult, y + 0.5*s), xytext=(x - 0.1*s*flip_mult, y + 0.5*s),
                    arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=2))


# Create figure
fig, axes = plt.subplots(3, 4, figsize=(16, 14))
fig.patch.set_facecolor('#fefefe')

exercises = [
    ('1. Shift Weights', 'shift', 'Weight transfer side-to-side'),
    ('2. Squat Rotation', 'squat_rotate', 'Squat + thoracic twist'),
    ('3. Knee Push Out', 'knee_push', 'Knees drive outward'),
    ('4. Knee Push Shifts', 'knee_push', 'Add lateral weight shift'),
    ('5. Internal Rotation', 'internal_rotation', 'Hip IR mobility'),
    ('6. Toe Raises', 'toe_raise', 'Toes up, heels down'),
    ('7. Hami Extension', 'hami_extension', 'Hamstring lengthening'),
    ('8. Knee Drives', 'knee_drive', 'Dynamic hip flexion'),
    ('9. Squat Flexion', 'squat', 'Deep squat hold'),
    ('10. Straddle Rotation', 'straddle', 'Wide stance + rotate'),
    ('11. Wrist Routine', 'wrist', 'Wrist circles & stretches'),
]

for idx, (title, pose, description) in enumerate(exercises):
    row = idx // 4
    col = idx % 4
    ax = axes[row, col]

    ax.set_xlim(-0.5, 0.5)
    ax.set_ylim(-0.1, 1.1)
    ax.set_aspect('equal')
    ax.axis('off')

    # Sketchy background
    rect = patches.FancyBboxPatch((-0.45, -0.05), 0.9, 1.1,
                                   boxstyle="round,pad=0.02",
                                   facecolor='#f8f9fa',
                                   edgecolor='#bdc3c7',
                                   linewidth=1.5,
                                   linestyle='-')
    ax.add_patch(rect)

    # Draw figure
    draw_stick_figure(ax, 0, 0, pose=pose, scale=0.9)

    # Title
    ax.text(0, 1.02, title, ha='center', va='bottom', fontsize=11, fontweight='bold', color='#2c3e50')
    ax.text(0, -0.02, description, ha='center', va='top', fontsize=9, color='#7f8c8d', style='italic')

# Hide last empty subplot
axes[2, 3].axis('off')
axes[2, 3].set_visible(False)

# Main title
fig.suptitle('10-Minute Mobility Routine - Exercise Sketches', fontsize=18, fontweight='bold', color='#2c3e50', y=0.98)
fig.text(0.5, 0.94, 'Hips • Spine • Full Body', ha='center', fontsize=12, color='#7f8c8d')

plt.tight_layout(rect=[0, 0, 1, 0.93])
plt.savefig('/home/nixos/temp/mobility_sketches.png', dpi=150, bbox_inches='tight', facecolor='#fefefe')
plt.savefig('/home/nixos/temp/mobility_sketches.pdf', bbox_inches='tight', facecolor='#fefefe')
print("Saved: mobility_sketches.png and mobility_sketches.pdf")
