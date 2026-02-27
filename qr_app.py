import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import qrcode
import re
import qrcode.image.svg as svg
app = ttk.Window(themename="flatly")
app.title("QR Utility")
app.geometry("1000x620")
app.resizable(False, False)

qr_image_pil = None
qr_preview = None
last_qr_data = None
status_var = ttk.StringVar(value="Ready")

def set_status(msg):
    status_var.set(msg)

# ---------- VALIDATION ----------
def valid_upi(upi):
    return "@" in upi and len(upi) > 3

def valid_amount(a):
    if not a:
        return True
    try:
        float(a)
        return True
    except:
        return False

def valid_latlon(lat, lon):
    try:
        lat = float(lat)
        lon = float(lon)
        return -90 <= lat <= 90 and -180 <= lon <= 180
    except:
        return False

# ---------- QR BUILD ----------
def build_qr(data):
    global qr_image_pil, qr_preview, last_qr_data

    if not data.strip():
        messagebox.showerror("Error", "No data provided")
        return

    last_qr_data = data

    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=2,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    qr_image_pil = img

    preview = img.resize((320, 320))
    qr_preview = ImageTk.PhotoImage(preview)
    preview_label.configure(image=qr_preview)

    set_status("QR generated")

# ---------- GENERATORS ----------
def gen_text():
    build_qr(text_entry.get())

def gen_wifi():
    ssid = wifi_ssid.get()
    pwd = wifi_pass.get()
    enc = wifi_enc.get()
    data = f"WIFI:T:{enc};S:{ssid};P:{pwd};;"
    build_qr(data)

def gen_contact():
    name = c_name.get()
    phone = c_phone.get()
    email = c_email.get()

    vcard = (
        "BEGIN:VCARD\nVERSION:3.0\n"
        f"FN:{name}\nTEL:{phone}\nEMAIL:{email}\nEND:VCARD"
    )
    build_qr(vcard)

def gen_upi():
    upi_id = u_upi.get().strip()
    name = u_name.get().strip()
    amount = u_amount.get().strip()

    if not valid_upi(upi_id):
        messagebox.showerror("Error", "Invalid UPI ID")
        return

    if not valid_amount(amount):
        messagebox.showerror("Error", "Invalid amount")
        return

    data = f"upi://pay?pa={upi_id}"
    if name:
        data += f"&pn={name}"
    if amount:
        data += f"&am={amount}"
    data += "&cu=INR"

    build_qr(data)

def gen_location():
    raw = loc_input.get().strip()

    pattern = r'(\d+)°(\d+)\'([\d.]+)"([NS])\s+(\d+)°(\d+)\'([\d.]+)"([EW])'
    m = re.match(pattern, raw)

    if not m:
        messagebox.showerror(
            "Error",
            "Invalid DMS format\nExample:\n12°14'27.7\"N 79°03'26.1\"E"
        )
        return

    lat_deg, lat_min, lat_sec, lat_dir, lon_deg, lon_min, lon_sec, lon_dir = m.groups()

    lat = float(lat_deg) + float(lat_min)/60 + float(lat_sec)/3600
    lon = float(lon_deg) + float(lon_min)/60 + float(lon_sec)/3600

    if lat_dir == "S":
        lat = -lat
    if lon_dir == "W":
        lon = -lon

    data = f"https://maps.google.com/?q={lat},{lon}"
    build_qr(data)

# ---------- SAVE ----------
def save_png():
    if qr_image_pil is None:
        messagebox.showerror("Error", "Generate QR first")
        return

    path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG", "*.png")]
    )
    if path:
        qr_image_pil.save(path)
        set_status("Saved PNG")

def save_svg():
    if not last_qr_data:
        messagebox.showerror("Error", "Generate QR first")
        return

    path = filedialog.asksaveasfilename(
        defaultextension=".svg",
        filetypes=[("SVG", "*.svg")]
    )
    if path:
        factory = svg.SvgImage
        img = qrcode.make(last_qr_data, image_factory=factory)
        img.save(path)
        set_status("Saved SVG")

# ---------- LAYOUT ----------
main = ttk.Frame(app, padding=15)
main.pack(fill=BOTH, expand=True)

left = ttk.Frame(main)
left.grid(row=0, column=0, sticky="ns")

right = ttk.Frame(main)
right.grid(row=0, column=1, sticky="nsew", padx=30)

main.columnconfigure(1, weight=1)

tabs = ttk.Notebook(left, width=360)
tabs.pack()

# TEXT
tab_text = ttk.Frame(tabs, padding=10)
tabs.add(tab_text, text="Text")
ttk.Label(tab_text, text="Text / URL").pack(anchor="w")
text_entry = ttk.Entry(tab_text, width=36)
text_entry.pack(pady=5)
ttk.Button(tab_text, text="Generate", bootstyle=PRIMARY,
           command=gen_text).pack(fill=X)

# WIFI
tab_wifi = ttk.Frame(tabs, padding=10)
tabs.add(tab_wifi, text="WiFi")
ttk.Label(tab_wifi, text="SSID").pack(anchor="w")
wifi_ssid = ttk.Entry(tab_wifi, width=36)
wifi_ssid.pack(pady=3)
ttk.Label(tab_wifi, text="Password").pack(anchor="w")
wifi_pass = ttk.Entry(tab_wifi, width=36)
wifi_pass.pack(pady=3)
ttk.Label(tab_wifi, text="Encryption").pack(anchor="w")
wifi_enc = ttk.Combobox(tab_wifi, values=["WPA", "WEP", "nopass"])
wifi_enc.set("WPA")
wifi_enc.pack(pady=3)
ttk.Button(tab_wifi, text="Generate", bootstyle=PRIMARY,
           command=gen_wifi).pack(fill=X)

# CONTACT
tab_contact = ttk.Frame(tabs, padding=10)
tabs.add(tab_contact, text="Contact")
ttk.Label(tab_contact, text="Name").pack(anchor="w")
c_name = ttk.Entry(tab_contact, width=36)
c_name.pack(pady=3)
ttk.Label(tab_contact, text="Phone").pack(anchor="w")
c_phone = ttk.Entry(tab_contact, width=36)
c_phone.pack(pady=3)
ttk.Label(tab_contact, text="Email").pack(anchor="w")
c_email = ttk.Entry(tab_contact, width=36)
c_email.pack(pady=3)
ttk.Button(tab_contact, text="Generate", bootstyle=PRIMARY,
           command=gen_contact).pack(fill=X)

# UPI
tab_upi = ttk.Frame(tabs, padding=10)
tabs.add(tab_upi, text="UPI")
ttk.Label(tab_upi, text="UPI ID").pack(anchor="w")
u_upi = ttk.Entry(tab_upi, width=36)
u_upi.pack(pady=3)
ttk.Label(tab_upi, text="Name (optional)").pack(anchor="w")
u_name = ttk.Entry(tab_upi, width=36)
u_name.pack(pady=3)
ttk.Label(tab_upi, text="Amount (optional)").pack(anchor="w")
u_amount = ttk.Entry(tab_upi, width=36)
u_amount.pack(pady=3)
ttk.Button(tab_upi, text="Generate", bootstyle=PRIMARY,
           command=gen_upi).pack(fill=X)

# LOCATION
tab_loc = ttk.Frame(tabs, padding=10)
tabs.add(tab_loc, text="Location")

ttk.Label(tab_loc, text="Coordinates (DMS)").pack(anchor="w")

loc_input = ttk.Entry(tab_loc, width=36)
loc_input.pack(pady=5)

ttk.Label(
    tab_loc,
    text='Example: 12°14\'27.7"N 79°03\'26.1"E',
    font=("Segoe UI", 8),
    foreground="gray"
).pack(anchor="w", pady=(0,5))

ttk.Button(
    tab_loc,
    text="Generate",
    bootstyle=PRIMARY,
    command=gen_location
).pack(fill=X)

# SAVE
save_frame = ttk.Frame(left)
save_frame.pack(fill=X, pady=10)

ttk.Button(save_frame, text="Save PNG",
           command=save_png,
           bootstyle=SUCCESS).pack(fill=X, pady=2)

ttk.Button(save_frame, text="Save SVG",
           command=save_svg,
           bootstyle=INFO).pack(fill=X, pady=2)

# PREVIEW
preview_container = ttk.Frame(right)
preview_container.pack(expand=True)
preview_label = ttk.Label(preview_container)
preview_label.pack(expand=True)

# STATUS
status = ttk.Label(app, textvariable=status_var,
                   relief="sunken", anchor="w")
status.pack(fill=X, side=BOTTOM)

app.mainloop()