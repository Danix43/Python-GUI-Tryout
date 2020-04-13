from backend import Grabber
# switch to pyqt5
import tkinter
# use matplotlib for graphs with the temperature data


def display_data(identifier, scale_choose="Celsius"):
    grabber = Grabber()
    grabber.send_request(name=identifier)

    data_name_label = tkinter.Label(display_frame, text=grabber.content["name"]).grid(row=0, column=1)
    data_location_label = tkinter.Label(display_frame, text=grabber.content["location"]).grid(row=1, column=1)
    data_last_update_label = tkinter.Label(display_frame, text=grabber.content["lastInsert"]).grid(row=2, column=1)
    data_temperature_label = tkinter.Label(display_frame, text=grabber.content["temperatureInCelsius"]).grid(row=3, column=1)
    data_heat_index_label = tkinter.Label(display_frame, text=grabber.content["heatIndexCelsius"]).grid(row=4, column=1)
    data_humidity_label = tkinter.Label(display_frame, text=grabber.content["humidity"]).grid(row=5, column=1)


# main window intialization
main_window = tkinter.Tk()

main_window.title("HerculesAPI")
main_window.geometry("1000x480-20-200")
main_window["padx"] = 20
main_window["pady"] = 30

input_frame = tkinter.Frame(main_window)
input_frame.grid(row=0, column=0, sticky="nw")

# the label and the entry where the user sends the request with the name specified
user_input = tkinter.StringVar()

input_label = tkinter.Label(input_frame, text="Enter the name:")
input_label.grid(row=0, column=0, sticky="ne")

input_text = tkinter.Entry(input_frame, textvariable=user_input)
input_text.grid(row=0, column=1, sticky="ne")

button = tkinter.Button(input_frame, text="Send Request", command=lambda: display_data(user_input.get(), scale_choise.get()))
button.grid(row=0, column=2, sticky="ne")


scale_choise = tkinter.StringVar()
scales = {"Celsius", "Kelvin", "Fahrenheit"}

scale_choise.set("Select a scale")
scale_drop_box = tkinter.OptionMenu(input_frame, scale_choise, *scales)
scale_drop_box.grid(row=1, column=0, columnspan=2, sticky="nw")


# display the information part
display_frame = tkinter.Frame(main_window)
display_frame.grid(row=2, column=0, sticky="nw", pady=30)

# data labels
name_label = tkinter.Label(display_frame, text="Name: ").grid(row=0, column=0)
location_label = tkinter.Label(display_frame, text="Location: ").grid(row=1, column=0)
last_update_label = tkinter.Label(display_frame, text="Last update at: ").grid(row=2, column=0)
temperature_label = tkinter.Label(display_frame, text="Temperature: ").grid(row=3, column=0)
heat_index_label = tkinter.Label(display_frame, text="Heat Index: ").grid(row=4, column=0)
humidity_label = tkinter.Label(display_frame, text="Relative humidity: ").grid(row=5, column=0)


main_window.mainloop()
