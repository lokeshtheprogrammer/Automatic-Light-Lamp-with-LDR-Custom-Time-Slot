
# 🔌 Automatic Light Lamp Simulator with LDR & Custom Time Slot

This interactive Python notebook simulates an automatic lamp system that:

✅ Measures **ambient light level** (simulated via slider)  
✅ Allows you to set a **custom ON time window** (even overnight)  
✅ Turns the lamp ON if:
- The light level is below a threshold, or
- The current time is within the configured schedule.

---

## ✨ Features

- 📊 **Interactive Sliders** to adjust:
  - Light level (0–1023)
  - Current time (hour and minute)
  - Start and end hours/minutes for scheduled ON time
- 🌈 **Dynamic Lamp Visualization**
  - Yellow lamp = ON
  - Gray lamp = OFF
- 🕒 **Overnight Scheduling**
  - Handles schedules that cross midnight (e.g., 18:00–06:00)

---

## 🛠️ Requirements

This simulation uses:
- Python
- Jupyter Notebook
- The following Python packages:

```bash
pip install ipywidgets matplotlib
````

---

## 🚀 How to Run

1. Launch **Jupyter Notebook**:

   ```bash
   jupyter notebook
   ```

2. Create a new notebook and copy the script into a cell.

3. Run the cell to display the interactive UI.

---

## 📋 Usage

* **Light Slider**: Simulates LDR reading (0 = dark, 1023 = bright)
* **Current Time**: Set the hour and minute you want to simulate
* **Start/End Time**: Define your lamp's scheduled ON window

💡 The lamp **turns ON** if:

* Ambient light < 300, **OR**
* Current time is within the defined start–end time slot.

---

## 🖼️ Example

**Dark Environment + Scheduled Time:**

```
🌞 Ambient Light Level: 200 (0 = Dark, 1023 = Bright)
🕒 Current Time: 20:00
⏰ Scheduled ON Time: 18:00 → 06:00
💡 Lamp Status: ON
```

**Bright Environment + Outside Scheduled Time:**

```
🌞 Ambient Light Level: 900
🕒 Current Time: 14:00
⏰ Scheduled ON Time: 18:00 → 06:00
🌑 Lamp Status: OFF
```

---

## 📄 License

This project is provided for educational purposes. Feel free to adapt and use it in your own experiments.

---

## 🙏 Acknowledgments

Built using:

* [ipywidgets](https://ipywidgets.readthedocs.io/)
* [matplotlib](https://matplotlib.org/)
* Jupyter Notebook

````

---

✅ **How to Use**

1. Create a `README.md` file in your project folder.
2. Copy the above Markdown.
3. Paste it into the file.
4. Commit and push:

```bash
git add README.md
git commit -m "Add project README"
git push
````
