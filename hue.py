import tkinter as tk
from phue import Bridge

# Connect to the Philips Hue bridge
b = Bridge("192.168.0.15")

# Get the list of lights
lights = b.lights

def turn_on():
  # Turn on the selected light
  b.set_light(selected_light.get(), 'on', True)

def turn_off():
  # Turn off the selected light
  b.set_light(selected_light.get(), 'on', False)

def set_brightness(value):
  # Set the brightness of the selected light
  b.set_light(selected_light.get(), 'bri', value)

def set_color_temp(value):
  # Set the color temperature of the selected light
  b.set_light(selected_light.get(), 'ct', value)

# Create the main window
root = tk.Tk()
root.title("Philips Hue Control")

# Create a dropdown menu to select the light
selected_light = tk.StringVar(root)
selected_light.set(lights[0].name)  # default value
light_menu = tk.OptionMenu(root, selected_light, *[light.name for light in lights])
light_menu.pack()

# Create buttons to turn the light on and off
on_button = tk.Button(root, text="On", command=turn_on)
on_button.pack()

off_button = tk.Button(root, text="Off", command=turn_off)
off_button.pack()

# Create a slider to adjust the brightness
brightness_slider = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL, command=set_brightness)
brightness_slider.pack()

# Create a slider to adjust the color temperature
color_temp_slider = tk.Scale(root, from_=0, to=65535, orient=tk.HORIZONTAL, command=set_color_temp)
color_temp_slider.pack()

# Run the main loop
root.mainloop()