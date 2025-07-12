# Step 1: Install dependencies
!pip install ipywidgets --quiet
from IPython.display import display, HTML
import matplotlib.pyplot as plt
from ipywidgets import interactive, IntSlider, FloatSlider, VBox, HBox, HTML as ipyHTML, Output

# Step 2: Global threshold for light
THRESHOLD = 300

# Step 3: Output for lamp
lamp_output = Output()

# Step 4: Function to draw lamp
def draw_lamp(color):
    fig, ax = plt.subplots(figsize=(2,2))
    ax.set_facecolor("black")
    circle = plt.Circle((0.5, 0.5), 0.3, color=color)
    ax.add_artist(circle)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    plt.show()

# Step 5: Convert hour and minute to float time (e.g., 9.5 = 9:30 AM)
def time_to_float(hour, minute):
    return hour + minute / 60.0

# Step 6: Update lamp based on light and custom time slot
def update_lamp(light_level, curr_hour, curr_min, start_hour, start_min, end_hour, end_min):
    lamp_output.clear_output()
    with lamp_output:
        curr_time = time_to_float(curr_hour, curr_min)
        start_time = time_to_float(start_hour, start_min)
        end_time = time_to_float(end_hour, end_min)

        print(f"🌞 Ambient Light Level: {light_level} (0 = Dark, 1023 = Bright)")
        print(f"🕒 Current Time: {curr_hour:02}:{curr_min:02}")
        print(f"⏰ Scheduled ON Time: {start_hour:02}:{start_min:02} → {end_hour:02}:{end_min:02}")

        # Check if current time is within scheduled time (handle overnight)
        if start_time <= end_time:
            time_on = start_time <= curr_time < end_time
        else:
            time_on = curr_time >= start_time or curr_time < end_time

        # Final lamp status
        if light_level < THRESHOLD or time_on:
            print("💡 Lamp Status: ON")
            draw_lamp("yellow")
        else:
            print("🌑 Lamp Status: OFF")
            draw_lamp("gray")

# Step 7: Create sliders

light_slider = IntSlider(value=500, min=0, max=1023, step=1, description='Light:')

curr_hour = IntSlider(value=12, min=0, max=23, description='Current Hr:')
curr_min = IntSlider(value=0, min=0, max=59, description='Current Min:')

start_hour = IntSlider(value=18, min=0, max=23, description='Start Hr:')
start_min = IntSlider(value=0, min=0, max=59, description='Start Min:')

end_hour = IntSlider(value=6, min=0, max=23, description='End Hr:')
end_min = IntSlider(value=0, min=0, max=59, description='End Min:')

interactive_ui = interactive(
    update_lamp,
    light_level=light_slider,
    curr_hour=curr_hour,
    curr_min=curr_min,
    start_hour=start_hour,
    start_min=start_min,
    end_hour=end_hour,
    end_min=end_min,
)

# Step 8: Display UI
display(ipyHTML("<h2>🔌 Automatic Light Lamp with LDR & Custom Time Slot</h2>"))
display(ipyHTML("💡 Lamp turns ON if it's dark OR if current time is within user-defined ON time.<br><br>"))
display(VBox([interactive_ui, lamp_output]))
